
# coding: utf-8

# In[12]:

from docx import Document


# In[18]:

document = Document('./PALS-docs/Q34.docx')


# In[19]:

patientFacingPara = []


# In[20]:

paraFound=False
for para in document.paragraphs:
    if 'Patient-Facing Text:' in para.text:
        paraFound = True
        continue
    elif 'Teaser:' in para.text:
        paraFound = False
    if paraFound:
        patientFacingPara.append(para.text)


# In[21]:

patientFacingText=[]
for sentence in patientFacingPara:
    if '.' in sentence:
        for splitSentence in sentence.split('.'):
            if splitSentence== ' ' or splitSentence== '':
                continue
            else:
                patientFacingText.append(splitSentence)
    elif sentence==' ' or sentence=='':
        continue
    else:
        patientFacingText.append(sentence)


# In[22]:

print(patientFacingText)

