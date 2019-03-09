import json
import logging
import string
from collections import defaultdict

with open('comments.json') as f:
    comments = json.load(f)['items']

words = defaultdict(int)

def getWords(comments, i):
    for comment in comments:
        if 'Thread' in comment['kind']:
            # go deeper
            logging.info((" "*i) + "thread")
            getWords([comment['snippet']['topLevelComment']], i+1)
            if comment['snippet']['totalReplyCount'] > 0:
                getWords(comment['replies']['comments'], i+1)

        elif 'comment' in comment['kind']:
            # collect us some words
            logging.info((" "*i) + "comment")
            for word in comment['snippet']['textOriginal'].split():
                word = word.translate(str.maketrans("","",string.punctuation))
                word = word.lower()
                words[word] += 1

        else:
            # thiiiiiiiis shouldn't happen... :\
            logging.warning(f"found a {comment['kind']}")

getWords(comments, 0)
for word, count in words.items():
    if count > 10:
        print(f"{word}{' '*(40-len(word))}{count}")

