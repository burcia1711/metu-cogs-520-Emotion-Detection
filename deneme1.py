
from collections import Counter
import string
# import io
# #functions for reading and writing data
from csv import reader
import json
# file=io.open("keywords.txt", mode="r", encoding="utf-16")
# lines=file.readlines()

import io


def tokenize(line):
  #remove punctuation
  line = ''.join(ch for ch in line if ch not in string.punctuation)
  #tokenize
  words = line.split()
  return words





def findSimilarity(talk1, talk2):
    # count word occurrences
    a_vals = Counter(talk1)
    b_vals = Counter(talk2)

    # convert to word-vectors
    words  = list(set(a_vals.keys()) | set(b_vals.keys()))
    a_vect = [a_vals.get(word, 0) for word in words]        
    b_vect = [b_vals.get(word, 0) for word in words]        

    # find cosine
    len_a  = sum(av*av for av in a_vect) ** 0.5             
    len_b  = sum(bv*bv for bv in b_vect) ** 0.5             
    dot    = sum(av*bv for av,bv in zip(a_vect, b_vect))    
    cosine = dot / (len_a * len_b)                          
    return cosine



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


duygular = ['mutluluk', 'kizginlik', 'igrenme', 'korku', 'saskinlik', 'uzuntu']
duygu_vectorleri = []
for duygu in duygular:
    text = io.open(duygu + '.json').read()
    json_text = json.loads(text)
    temp_list = []
    for item in json_text['Term']:
        #print(item['name'])
        temp_list.append(item['name'])
    duygu_vectorleri.append(temp_list)
    temp_list = []


similarities = []
print(duygular)
for talk in talks:
    temp_similarity = []
    for duygu in duygu_vectorleri:
        temp_similarity.append(findSimilarity(talk, duygu))
    similarities.append(temp_similarity)
    print(temp_similarity)
    temp_similarity = []
