
import spacy

SPACY_NLP = spacy.load('en')
NLP = spacy.load("en_core_web_sm")

#using spacy
SAMPLE_SENTENCE = 'My name is Francis Obasi, I am data analyst, I live in lagos state, Nigeria and i work with Nigerian Breweries Plc'
INPUT_SENTENCE = input('Enter sentence here: ')
PROCESSED_SENTENCE = NLP(INPUT_SENTENCE)

#Combining both functions below
DATA_DIC = dict()

def get_items():
    def sentence_process(PROCESSED_SENTENCE):
        for element in PROCESSED_SENTENCE.ents:
            DATA_DIC[element.label_] = element
    sentence_process(PROCESSED_SENTENCE)
    print(' name '' = '+ str(DATA_DIC.get('PERSON')))
    print(' organization ' ' = ' + str(DATA_DIC.get('ORG')))
    print(' location ' ' = ' + str(DATA_DIC.get('GPE')))
get_items()























