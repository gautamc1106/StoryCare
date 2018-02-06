from services.parser import parseText
from services.keywords import requestWatsonSentence

path = './PALS-docs/Q34.docx'

sentenceList = parseText(path)
print requestWatsonSentence(sentenceList)
