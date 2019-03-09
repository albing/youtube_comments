import json
import logging
import os
import string
from collections import defaultdict

from requests import get

API_KEY=os.getenv('API_KEY')
if not API_KEY:
    logging.error("Need an API key in $API_KEY, bucko.")
    exit(1)

logging.getLogger().setLevel(logging.INFO)

words = defaultdict(int)

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
                word = word.translate(str.maketrans("","",string.punctuation))
                word = word.lower()
                words[word] += 1

        else:
            # thiiiiiiiis shouldn't happen... :\
            logging.warning(f"found a {comment['kind']}")

def getPages(token=None, i=0):
    # Step 1: fetch
    url = f'https://www.googleapis.com/youtube/v3/commentThreads?part=snippet%2Creplies&videoId=EoiyJXsNerI&key={API_KEY}'
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
        getPages(new_token, i+1)

getPages()

for word, count in words.items():
    if count > 10:
        print(f"{word}{' '*(40-len(word))}{count}")

with open('results.dat', 'w') as f:
    f.write(json.dumps(words))
