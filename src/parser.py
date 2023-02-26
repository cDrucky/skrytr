import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter
from heapq import nlargest
from scraper import cleaned_structure


# Load Spacy's English language model
nlp = spacy.load('en_core_web_sm')



class Summarizer:
    def __init__(self, corpus) -> None:
        self.corpus = corpus
        self.doc = nlp(corpus)

    @property
    def keywords(self):
        keyword = []
        stopwords = list(STOP_WORDS)
        pos_tag = ['PROPN', 'ADJ', 'NOUN', 'VERB']
        for token in self.doc:
            if(token.text in stopwords or token.text in punctuation):
                continue
            if(token.pos_ in pos_tag):
                keyword.append(token.text) 
        return keyword

    @property
    def common_words(self):
        freq_word = Counter(self.keywords)
        return freq_word.most_common(5)

    @property
    def freq_word(self):
        return Counter(self.keywords)

    def sentence_strength(self):
        sent_strength={}
        for sent in self.doc.sents:
            for word in sent:
                if word.text in self.freq_word.keys():
                    if sent in sent_strength.keys():
                        sent_strength[sent]+=self.freq_word[word.text]
                    else:
                        sent_strength[sent]=self.freq_word[word.text]
        return sent_strength


    def summarize(self):
        summarized_sentences = nlargest(3, self.sentence_strength(), key=self.sentence_strength().get)
        return [ w.text for w in summarized_sentences ]

    def __str__(self):
        return ' '.join(self.summarize())


test = Summarizer(cleaned_structure)

print("Summary: ", test)
print("Full: ", cleaned_structure)