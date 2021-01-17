import io
import json
from collections import Counter
import zemberek


def createEmotionVectors(folder):
    duygular = ['mutluluk', 'kizginlik', 'igrenme', 'korku', 'saskinlik', 'uzuntu']
    duygu_vectorleri = {}
    for duygu in duygular:
        text = io.open(folder + duygu + '.json', encoding="utf-8").read()
        json_text = json.loads(text)
        temp_list = []
        for item in json_text['Term']:
            # print(item['name'])
            temp_list.append(item['name'])
        duygu_vectorleri[duygu] = temp_list
        temp_list = []
    return duygu_vectorleri


def findSimilarity(talk1, talk2):

    for n, i in enumerate(talk1):
            talk1[n] = zemberek.getRoot(talk1[n]) 

    for m, j in enumerate(talk2):
            talk2[m] = zemberek.getRoot(talk2[m]) 
    #s += (t + " ->" + zemberek.getRoot(t) + "   ||||  ")
   
    #print(s)
    # count word occurrences
    a_vals = Counter(talk1)
    b_vals = Counter(talk2)

    # convert to word-vectors
    words = list(set(a_vals.keys()) | set(b_vals.keys()))
    a_vect = [a_vals.get(word, 0) for word in words]
    b_vect = [b_vals.get(word, 0) for word in words]

    # find cosine

    len_a = sum(av * av for av in a_vect) ** 0.5
    len_b = sum(bv * bv for bv in b_vect) ** 0.5
    if len_a == 0 or len_b == 0:
        return 0
    dot = sum(av * bv for av, bv in zip(a_vect, b_vect))
    cosine = dot / (len_a * len_b)
    return cosine


def findBestEmotionForProps(similarities, talks, emotions):
    BestEmotions = {}
    for talk in talks:
        for prop in talks[talk]:
            if prop not in BestEmotions:
                BestEmotions[prop] = {}
            for emotion in emotions:
                if emotion not in BestEmotions[prop]:
                    BestEmotions[prop][emotion] = 0
                BestEmotions[prop][emotion] += similarities[talk][prop][emotion]

    for prop in BestEmotions:
        for emotion in BestEmotions[prop]:
            BestEmotions[prop][emotion] /= len(talks)
    return BestEmotions

#result = createEmotionVectors(
#    "C:\\Users\\Enes Recep ÇINAR\\PycharmProjects\\metu-cogs-520-TED-talks-emotions\\emotions\\")
#for r in result:
#    print(r + " " + str(result[r]))
