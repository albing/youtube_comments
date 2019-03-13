import itertools
import json
import logging
import os
import string

from requests import get

from predictor import Predictor

use_api = True
API_KEY=os.getenv('API_KEY')
if not API_KEY and use_api:
    logging.error("Need an API key in $API_KEY, bucko.")
    exit(1)

logging.getLogger().setLevel(logging.INFO)

words = Predictor()
video_id = ''

def getWords(comments, i):
    for comment in comments:
        if 'Thread' in comment['kind']:
            # go deeper
            logging.debug((" "*i) + "thread")
            getWords([comment['snippet']['topLevelComment']], i+1)
            if comment['snippet']['totalReplyCount'] > 0:
                getWords(comment['replies']['comments'], i+1)

        elif 'comment' in comment['kind']:
            # collect us some words
            logging.debug((" "*i) + "comment")
            for word in comment['snippet']['textOriginal'].split():
                # remove punctuation and normalize to lower case
                word = word.translate(str.maketrans("","",string.punctuation))
                word = word.lower()
                # then save
                words.add(word)
            words.terminate()

        else:
            # thiiiiiiiis shouldn't happen... :\
            logging.warning(f"found a {comment['kind']}")


def get_pages_files():
    for i in itertools.count():

        # read the data from the file.  ignore the first 2 lines
        try:
            with open(f'savedata{i}.dat', 'r') as f:
                for line_no, line in enumerate(f):
                    if line_no == 2:   # 3rd line
                        comments = json.loads(line)
        except:
            return

        # start a'countin'
        getWords(comments['items'], 0)


def get_pages_api(token=None, i=0):
    # Step 1: fetch
    url = f'https://www.googleapis.com/youtube/v3/commentThreads?part=snippet%2Creplies&videoId={video_id}&key={API_KEY}'
    if token:
        url += f'&pageToken={token}'
    logging.info(f"fetching {i}")
    response = get(url)
    if not response.ok:
        logging.error(response.status_code)
        logging.error(response.text)
        exit(1)
    comments = response.json()

    # Step 1.5: save
    with open(f'savedata{i}.dat', 'w') as f:
        f.write(url+'\n')
        f.write(str(token)+'\n')
        f.write(json.dumps(comments))

    # Step 2: count
    getWords(comments['items'], 0)

    # Step 3: repeat
    new_token = comments.get('nextPageToken')
    if new_token:
        get_pages_api(new_token, i+1)

#video_id = 'mIKsW0FgRzQ' # vietnam = mIKsW0FgRzQ
video_id = 'EoiyJXsNerI' # defranco = EoiyJXsNerI
#video_id = 'FO0iG_P0P6M' # oliver = FO0iG_P0P6M

get_pages_api()
with open(f'results_{video_id}.dat', 'w') as f:
    f.write(json.dumps(words.dict()))
#get_pages_files()

#for word, nexts in words.dict().items():
#    print(f"{word}{' '*(20-len(word))}{nexts}")
