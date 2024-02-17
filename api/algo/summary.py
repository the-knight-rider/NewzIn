import spacy
from spacy.lang.en import STOP_WORDS
from string import punctuation
from heapq import nlargest

stopwords = list(STOP_WORDS)
nlp = spacy.load('en_core_web_sm')
punctuation = punctuation + '\n'


#-----------------------Helping fun
def getWordFrequenciesFromDoc(word_frequencies,doc):
    for word in doc:
        if word.text.lower() not in stopwords:
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1
                    
def getSentenceScoreFromSentenceTokensWordFreq(sentence_scores,sentence_tokens,word_frequencies):
    for sent in sentence_tokens:
        sent_doc = nlp(sent)
        for word in sent_doc:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word.text]
                else:
                    sentence_scores[sent] += word_frequencies[word.text]
                    
def processSummary(sentence_tokens,sentence_scores,val):
    select_length = int(len(sentence_tokens)*val)
    my_summary = nlargest(select_length, sentence_scores, key = sentence_scores.get)
    final_summary = [word.text for word in my_summary for word in nlp(word)]
    my_summary = ' '.join(final_summary)
    return my_summary
    


#---------------------------------- core func



def getSummary(text):
    doc = nlp(text)
    word_frequencies = {}
    getWordFrequenciesFromDoc(word_frequencies,doc)
                    
    max_frequency = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word] / max_frequency 
    
    sentence_tokens = list({sent.text for sent in doc.sents})
    sentence_scores = {}
    getSentenceScoreFromSentenceTokensWordFreq(sentence_scores,sentence_tokens,word_frequencies)
                    
    mySummary = processSummary(sentence_tokens,sentence_scores,0.3)
    
    return mySummary


#------------------exe func


def mySummary(bigText):
   
    pro_sum = getSummary(bigText)


    return pro_sum