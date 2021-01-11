import json
import io
import Main


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


#for talk in talks:
 #   for duygu in duygu_vectorleri:
  #      deneme1.findSimilarity(talk, duygu)



# for i in range(json_text):
#     print(item)
kizginlik_vector = []


#print(kizginlik_vector)