import json
import sys

from predictor import Predictor

if len(sys.argv) < 3:
    print("usage: python walker.py <output data file> <word to start with>")
    exit(1)

filename = sys.argv[1]
word = sys.argv[2]


with open(filename) as f:
    data_dict = json.load(f)
predictor = Predictor(data_dict)

output = ''
while word != '.':
    output += f'{word} '
    word = predictor.random_walk_step(word)

print(output)
