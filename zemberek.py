#Zemberek is written in Java, so we need JVM
#this code block is to set Zemberek environment
from os.path import join
from typing import List
from jpype import JClass, JString, getDefaultJVMPath, shutdownJVM, startJVM, java
from jpype._core import isJVMStarted


def init_jvm(jvmpath=None):
    if isJVMStarted():
        return
    startJVM(getDefaultJVMPath(),
    '-ea',
    f'-Djava.class.path={ZEMBEREK_PATH}',
    convertStrings=False)



def fixSentence(sentence):
    words = sentence.split(" ")
    for i, word in enumerate(words):
        if spell_checker.suggestForWord(JString(word)):
            if not spell_checker.check(JString(word)):
                words[i] = str(spell_checker.suggestForWord(JString(word))[0])

    return ' '.join(words)

#Zemberek jar dosyasının konumunu yaz.
ZEMBEREK_PATH: str = join("./zemberek-full.jar")


init_jvm()
TurkishMorphology: JClass = JClass('zemberek.morphology.TurkishMorphology')
TurkishSpellChecker: JClass = JClass('zemberek.normalization.TurkishSpellChecker')


morphology: TurkishMorphology = TurkishMorphology.createWithDefaults()

spell_checker: TurkishSpellChecker = TurkishSpellChecker(morphology)




def getRoot(word):
    try:
        result = morphology.analyze(word);
        res = {''}
        toBeReturned = word
        for analysis in result:
            res.add(str(analysis.getLemmas()))

        for r in res :
            w = str(list(res)[1])
            temp = w[1:len(w) - 1]
            if("," not in temp):
                return temp
        return toBeReturned
    except:
        return word


#words = ["oldum", "suluk", "selamlar", "koltuklara", "ağaca", "koltuğu", "merhaba"]

#for i in range(100):
#    for w in words:
#        print(getRoot(w))