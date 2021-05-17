# from gensim.utils import tokenize
from gensim.corpora import dictionary
import streamlit as st
st.title('LDA Results')

import pandas as pd
from nltk.corpus import stopwords
import gensim
from gensim import corpora

df = pd.read_csv('Speeches_with_topics.csv', converters={'Tokens': eval})
result = df['Tokens'][0]

new_dictionary = corpora.Dictionary(result)
doc_term_matrix = [new_dictionary.doc2bow(rev) for rev in result]


LDA = gensim.models.ldamodel.LdaModel
model =  LDA.load('model/lda.model')
model.print_topics()

import pyLDAvis
import pyLDAvis.gensim_models as gensimvis


vis = gensimvis.prepare(model, doc_term_matrix, new_dictionary)
pyLDAvis.display(vis)

html_string = pyLDAvis.prepared_data_to_html(vis)
from streamlit import components
components.v1.html(html_string, width=1000, height=800, scrolling=True)