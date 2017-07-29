import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize, wordpunct_tokenize


nltk.download('wordnet')
nltk.download('punkt') #for tokenizer

print('wordnet')
for syns in wn.synsets('school'):
    for i in syns.lemmas():
        print i.name()

print('tokenizer')
sentence = """Hello all.
I am a student of UMKC.
Studying masters in CS."""
s=word_tokenize(sentence)
print(s)


print('Stemming')
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()
example_words = ["python","pythoner","pythoning","pythoned","pythonly"]
for w in example_words:
    print(ps.stem(w))


print('parts of speech')
pos=nltk.pos_tag(s)
print(pos)

print('lemmatization')
lemmatize = nltk.WordNetLemmatizer()
print lemmatize.lemmatize('schooling', pos='v')

from nltk.util import ngrams
from collections import Counter
print('trigrams')
trigrams=ngrams(s,3)
print Counter(trigrams)


from nltk import pos_tag, ne_chunk
import numpy
print ne_chunk(pos_tag(wordpunct_tokenize(sentence)))