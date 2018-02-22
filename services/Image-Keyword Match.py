
# coding: utf-8

import pyexiv2
import nltk
import os
from nltk.stem.snowball import SnowballStemmer
from sematch.semantic.similarity import WordNetSimilarity
stemmer = SnowballStemmer("english")
keywords =list(map(stemmer.stem, ['ache','understand']))
def getDictOfKeywords(dir):
    dictOfimg = {}
    for file in os.listdir(dir):
        if file[0] == ".":
            continue
        metadata = pyexiv2.ImageMetadata(dir + '//' + file)
        metadata.read()
        if('Iptc.Application2.Keywords' in metadata.iptc_keys):
            dictOfimg[file] = metadata['Iptc.Application2.Keywords'].raw_value
        elif 'Xmp.MicrosoftPhoto.LastKeywordXMP' in metadata.keys():
            dictOfimg[file] = metadata['Xmp.MicrosoftPhoto.LastKeywordXMP'].raw_value
        else:
            dictOfimg[file] = []
        dictOfimg[file] = list(map(stemmer.stem, dictOfimg[file]))
    return dictOfimg

def getSimilarImage():
    images = getDictOfKeywords('..//..//StoryCare images')
    maxSim = 0
    imageSim = ''
    for image in images.keys():
        count = 0
        for k in keywords:
            if k in images[image]:
                count+=1
        similarity = count/float(len(keywords))
        if(similarity > maxSim):
            similarity = maxSim
            imageSim = image
    return imageSim

def getSimilarImage1():
    images = getDictOfKeywords('..//..//StoryCare images')
    maxSim = 0
    imageSim = ''
    wns = WordNetSimilarity()
    for image in images.keys():
        avg = 0
        print(images[image])
        for word in images[image]:
            max = 0
            for k in keywords:
                print(k,word)
                match = wns.word_similarity(k, word, 'li')
                print(match)
                if(max<match):
                    max = match
            avg += max
            print(avg)
        similarity = 0
        if(len(images[image]) > 0):
            similarity = avg/float(len(images[image]))
        if(similarity > maxSim):
            similarity = maxSim
            imageSim = image
    return imageSim

getSimilarImage()

#getSimilarImage1()


# In[19]:


# dictOfimg = {}
# metadata = pyexiv2.ImageMetadata('..//..//StoryCare images/shutterstock_71236504.jpg')
# metadata.read()
# print(metadata.iptc_keys)
# print(metadata['Xmp.MicrosoftPhoto.LastKeywordXMP'].raw_value)
# if('Iptc.Application2.Keywords' in metadata.iptc_keys):
#     dictOfimg[file] = metadata['Iptc.Application2.Keywords'].raw_value
# else:
#     dictOfimg[file] = []
#     dictOfimg[file] = list(map(stemmer.stem, dictOfimg[file]))
# print(dictOfimg)


# In[58]:


# wns = WordNetSimilarity()
# wns.word_similarity('relax', 'relax', 'wpath') # 0.449327301063


# In[2]:


# from nltk.corpus import wordnet
# syns = wordnet.synsets('rest')
# print(syns[0].lemmas())


# In[82]:


#  for syn in wordnet.synsets("rest"):
#     synonyms = []
#     w1 = syn
#     w2
#     w1.wup_similarity(w2)
#     for l in syn.lemmas():
#         synonyms.append(l.name())
# print(synonyms)


# In[90]:


# w1 = wordnet.synset('ache.v.01') # v here denotes the tag verb
# w2 = wordnet.synset('head.v.01')
# print(w1.wup_similarity(w2))

# print(wordnet.synsets('rest'))


# In[6]:


# from itertools import product
# import numpy as np
# allsyns1 = set(ss for word in ['understand','ache'] for ss in wordnet.synsets(word))
# allsyns2 = set(ss for word in ['understand','ache'] for ss in wordnet.synsets(word))
# best = 0.0
# word = allsyns1.pop()
# for word in allsyns1:
#     max = 0
#     for s1 in allsyns2:
#         similarity = wordnet.wup_similarity(word, s1)
#         if(similarity and similarity>max):
#             max = similarity
#     best += max
# print(best/(len(list(allsyns1)) + len(list(allsyns2))))


# In[140]:


# from nltk.corpus import wordnet

# list1 = ['head', 'ache']
# list2 = ['head', 'ache']
# list11 = []

# for word1 in list1:
#     for word2 in list2:
#         wordFromList1 = wordnet.synsets(word1)
#         wordFromList2 = wordnet.synsets(word2)
#         if wordFromList1 and wordFromList2: #Thanks to @alexis' note
#             s = wordFromList1[0].wup_similarity(wordFromList2[0])
#             if(s):
#                 list11.append(s)

# print(np.mean(list11))
