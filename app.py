import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
# Load tokenizer and model
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
model = load_model('model.keras')

input_max_len= len(tokenizer.word_index) + 1
# Streamlit UI
st.title("Next Word Prediction")
input_text = st.text_area("Enter text:", "")

def predict_next_word(text):
    token=tokenizer.texts_to_sequences([text])[0]
    if(len(token)>input_max_len):
        token=token[-(input_max_len),:]
    token=np.array(pad_sequences([token],maxlen=input_max_len-1,padding='pre'))
    prediction=model.predict(token)
    predicted_index=np.argmax(prediction,axis=1)
    for word,index in tokenizer.word_index.items():
        if index==predicted_index:
            return word
    return None

if st.button("Predict Next Word") and input_text:
    next_word = predict_next_word(input_text)
    st.write(f"Predicted next word: **{next_word}**")
