
#%% [markdown]
# #  Natural Language Processing
# ## Concepts

# A text collection is known as __corpus__ (plural is __corpora__)

# ## TextBlob

# ### Installation

# `conda install -c conda-forge textblob`

# `ipython -m textblob.download_corpora`

# ### References

# [List of Tags](https://www.clips.uantwerpen.be/pages/MBSP-tags)

# ## Project Gutenberg
# A great source for text analysis is the free ebooks at 
# Project [Gutenberg](https://www.gutenberg.org/)
#%% Imports
from pathlib import Path
from textblob import TextBlob

#%% 
text = "Today is a beautiful day. Tomorrow looks like bad weather."

blob = TextBlob(text)

print(f'Blob\n\n {blob}\n')
print(f'Sentences\n\n{blob.sentences}\n')
print(f'Words \n\n {blob.words}\n')
print(f'Tags \n\n {blob.tags}\n')
print(f'Noun Phrases \n\n {blob.noun_phrases}\n')

#%% [markdown] 
# ## Sentiment Analysis
#
# polarity: -1 to 1 negative to positive 
#
# subjectivity: 0 to 1 objective to subjective

print(f'Sentiment \n\n {blob.sentiment}\n')
for sentence in blob.sentences:
    print(sentence.sentiment)


#%% [markdown]
# ### Naive Bayes Analyser
# The Naive Bayes [Classifier](https://en.wikipedia.org/wiki/Naive_Bayes_classifier)
# is another option
from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())
print(f'The sentiment for the blob is {blob.sentiment}')



#%% [markdown]
# ## Language Detection and Translation
# TextBlob uses Google Translate.  

print(f'The language of the blob: {blob.detect_language()}')
spanish = blob.translate(to='es')
print(f'Translation to spanish:\n{spanish}')

#%% [markdown]
# ## Inflection
# Inflections are different forms of the same words, such as singular
#
# and plural, or tense.
from textblob import Word

index = Word('index')
cacti = Word('cacti')
print(f'plural {index} is {index.pluralize()}')
print(f'singular of {cacti} is {cacti.singularize()}')

#%% [markdown]
# Spell Checking

word = Word('theyr')
print(f'Options for {word}: {word.spellcheck()}')
print(f'Choosing the highest confidence value we get: {word.correct()}')

sentence = TextBlob('Ths sentense has missplled wrds.')
print(f'before:\n{sentence}\nafter:\n{sentence.correct()}')

#%% [markdown]
# ## Normalization
# Stemming and lemmatization are two approaches to handle inflections
# 
# In general, __stemming__ algorithms err on the side of being too 
# 
# aggressive, sacrificing precision in order to increase recall.
#
# __Lemmatization__ does not simply chop off inflections, but instead 
# 
# relies on a lexical knowledge base like WordNet to obtain the correct base forms of words.
#
# offers better precision than stemming, but at the expense of recall.

word = Word('varieties')
print(f'The word {word} has stem {word.stem()} and lematization of',
      f'{word.lemmatize()}')



#%% [markdown]
# ## Word Frequencies

from pathlib import Path

blob = TextBlob(Path('romeo_and_juliet.txt').read_text())

print(f'Occurences of word "juliet": {blob.word_counts["juliet"]}')
print(f'Occurences of word "joy": {blob.words.count("joy")}')

#%% [markdown]
# ## Definitions, Synomyms and Antonyms from WordNet

happy = Word('happy')
print(f'Definitions for {happy}:\n {happy.definitions}')
print(f'Synoyms for {happy}:\n {happy.synsets}')

synonyms = set()
for synset in happy.synsets:
    for lemma in synset.lemmas():
        synonyms.add(lemma.name())

print(f'Friendlier Synoyms for {happy}:\n {synonyms}')

lemmas = happy.synsets[0].lemmas()
print(f'Antonym for {happy}: {lemmas[0].antonyms()}')
#%% [markdown]
# ## Stop Words
# Stop words are common words in text that are often removed from text
# 
# before analyzing it because they typically dont provide useful info
import nltk

nltk.download('stopwords')  

#%%
from nltk.corpus import stopwords

stops = stopwords.words('english')

blob = TextBlob('Today is a beautiful day.')

filtered_words = [word for word in blob.words if word not in stops]
print(f'Original:\n {blob}\nfiltered words: {filtered_words}')


#%% [markdown]
# ## n-grams
# A sequence of n text items, such as letters in words or words in 
#
# sentences.  Used to identify words that appear together.

text = 'Today is a beatiful day.  Tomorrow looks like bad weather.'

blob = TextBlob(text)
print(f'3-grams in text: {blob.ngrams(n=3)}')


#%% [markdown]
# ## Visualizinga Word Frequencies

blob = TextBlob(Path('romeo_and_juliet.txt').read_text())
stop_words = stopwords.words('english')

items = blob.word_counts.items()
items = [item for item in items if item[0] not in stop_words]

from operator import itemgetter

sorted_items = sorted(items, key=itemgetter(1), reverse=True)

import pandas as pd
import matplotlib.pyplot as plt



#%% [markdown]
# ### Bar Chart

top_20 = sorted_items[:20]
df = pd.DataFrame(top_20, columns=['word','count'])
axes = df.plot.bar(x='word',y='count',legend=False)


#%%  [markdown]
# ### Word Cloud
# ` conda install -c conda-forge wordcloud `
import imageio

mask_image = imageio.imread('mask_heart.png')

from wordcloud import WordCloud

word_cloud = WordCloud(colormap='prism', mask=mask_image,
                        background_color='white')

text = Path('romeo_and_juliet.txt').read_text()

word_cloud = word_cloud.generate(text)
word_cloud = word_cloud.to_file('RomeoAndJulietHeart.png')


#%% [markdown]
# ## Readability with Textatistic
# Usually affected by words used, sentence structure, length, topic
#
# ` pip install textatistic `
#
# Ouput:  notdalechall_coun: words not understood by 5th graders
#
# polysyblword_count: words with > 3 syllables, flesch_score: >90 5th graders
#
# < 30 need college degree, flesch..: grade level, gunn..: grade level
#
# smog..: years of education to understand, dale..: grade levels >16 college
# 
# More details in [Readability](https://en.wikipedia.org/wiki/Readability)


text = Path('romeo_and_juliet.txt').read_text()

from textatistic import Textatistic

readability = Textatistic(text) 

print(f'Readability of Romeo and Juliet:\n{readability.dict()}')


#%% [markdown]
# <h1> Test </h1>
# This is a test of a long paraghaph. dkljfldk 
# dlkfjdl fkdfldkjfd lkkldjf ldkfj dlfkj dlkj <br>
# Another paragraph.

#%% [markdown]
# ## Named Entitiy Recognition with spaCy
# Attempts to locate and categorize items like dates, times, quantities, places
# people, things, organizations and more.  
#
# Using [spaCy](https://spacy.io/) <br>
#
# `conda install -c conda-forger spacy`
#
# `python -m spacy download en`
import spacy
#%% 
nlp = spacy.load('en')  # spaCy recommends the name nlp

document = nlp('In 1994, Tim Berners-Lee founded the World Wide Web'+
               'Consortium (W3C), devoted to developing web technologies')

for entity in document.ents:
    print(f'{entity.text}: {entity.label_}')

#%% [markdown]
# ## Similarity Detection
document1 = nlp(Path('romeo_and_juliet.txt').read_text())
document2 = nlp(Path('EdwardTheSecond.txt').read_text())

print(f'Similarity between Docs {document1.similarity(document2)}')

#%% [markdown]
# ## Other tools
# ![Tools 1](nlptools1.png)
# ![Tools 1](nlptools2.png)

#%%
