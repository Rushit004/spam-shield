# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import streamlit as st
import string
import nltk
import pickle
import sklearn as sk

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

import nltk

nltk.download('punkt')
nltk.download('punkt_tab')

ps = PorterStemmer()

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("Emial/SMS Spam Classifier")

input_text = st.text_area("Enter the message")



def transform_txt(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


if st.button("Predict"):
    # 1.preprocess
    transformed_sms = transform_txt(input_text)
    # 2.vectorization
    vector_input = tfidf.transform([transformed_sms])
    # 3.predict
    result = model.predict(vector_input)[0]
    # 4.Display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
