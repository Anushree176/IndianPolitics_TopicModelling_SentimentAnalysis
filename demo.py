from gensim.utils import tokenize
import streamlit as st

import pandas as pd
# import numpy
# import re
# import string
import spacy
# import nltk
# from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
# from nltk.stem import WordNetLemmatizer
# from nltk.tokenize import word_tokenize
import gensim
from gensim import corpora

st.set_page_config(layout="wide")
st.title('INDIAN POLITICS : Topic Modelling and Sentiment Analysis')

df = pd.read_csv('Speeches_with_topics.csv', converters={'Tokens': eval})
tokenized = df['Tokens'][0]

dictionary = corpora.Dictionary(tokenized)
doc_term_matrix = [dictionary.doc2bow(rev) for rev in tokenized]

LDA = gensim.models.ldamodel.LdaModel

lda_model = LDA(corpus=doc_term_matrix, id2word=dictionary, num_topics=5, 
                random_state=100, chunksize=1, passes=50, iterations=10)

lda_model.print_topics()

import pyLDAvis
import pyLDAvis.gensim_models as gensimvis
import matplotlib.pyplot as plt
import seaborn as sns

# pyLDAvis.enable_notebook()
vis = gensimvis.prepare(lda_model, doc_term_matrix, dictionary)
# vis
pyLDAvis.display(vis)
'''
## LDA Results for a single speech
'''
html_string = pyLDAvis.prepared_data_to_html(vis)
from streamlit import components
components.v1.html(html_string, width=1250, height=900, scrolling=True)

'''
## Most commonly used words in the tweets
'''
st.image('cleaned.png',use_column_width=True)