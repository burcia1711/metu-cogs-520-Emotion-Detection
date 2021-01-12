import glob
from collections import Counter
import string
# import io
# #functions for reading and writing data
from csv import reader
import json
# file=io.open("keywords.txt", mode="r", encoding="utf-16")
# lines=file.readlines()

import io



BASE_PATH = "C:\\Users\\Enes Recep ÇINAR\\PycharmProjects\\metu-cogs-520-TED-talks-emotions\\"
import FileOperations
import Utils


def tokenize(line):
  #remove punctuation
  line = ''.join(ch for ch in line if ch not in string.punctuation)
  #tokenize
  words = line.split()
  return words

def pretty(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print('\t' * (indent+1) + str(round(value, 4)))


talks = FileOperations.read_and_store_input(BASE_PATH + "\\annotated\\")
emotions = Utils.createEmotionVectors(BASE_PATH + "\\emotions\\")

similarities = {}
for talk in talks:
    similarities[talk] = {}
    for prop in talks[talk]:
        similarities[talk][prop] = {}
        for emotion in emotions:
            similarities[talk][prop][emotion] = 0
            similarities[talk][prop][emotion] = Utils.findSimilarity(talks[talk][prop], emotions[emotion])
            #print(Utils.findSimilarity(talks[talk][prop], emotions[emotion]))

pretty(Utils.findBestEmotionForProps(similarities, talks, emotions), 0)

#pretty(similarities, 1)
for s in similarities:
    print(s + " : " + str(similarities[s]))






"""
lines = []
keys = io.open('keywords.txt').readlines()
for line in keys:
    lst = tokenize(line)
    lines.append(lst)



word_count = {}

for l in lines:
    for word in l:
        #print(word)
        if(word in word_count):
            word_count[word] += 1
        else:
            word_count[word] = 1

#print(word_count)
wc = sorted(word_count.items(), key=lambda x: x[1], reverse=True)


import codecs
import json

# file = codecs.open("word_count.txt", "w", "utf-8")
# file.write(json.dumps(wc))
# file.close()

# with codecs.open('word_count.txt', 'w', 'utf-8') as f:
#         f.write(json.dumps(wc) + "\n")

#print(wc)
#print(findSimilarity(lines[657], lines[791]))


text = io.open('talks' + '.json').read()
json_text = json.loads(text)
talks  =[]

for item in json_text['talks']:
    talks.append(item['content'].split(' '))





similarities = []
print(duygular)
for talk in talks:
    temp_similarity = []
    for duygu in duygu_vectorleri:
        temp_similarity.append(findSimilarity(talk, duygu))
    similarities.append(temp_similarity)
    print(temp_similarity)
    temp_similarity = []
"""""