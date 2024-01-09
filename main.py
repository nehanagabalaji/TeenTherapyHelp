import streamlit as st
import lc_helper as lch

st.title("Teen Therapy Assistant")

question = st.sidebar.text_area("What's your question?",height = 200)

if question:
    response = lch.generate_therapy_response(question)
    st.text_area(response['text'], height=300)