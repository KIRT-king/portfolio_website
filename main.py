import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.subheader("Hi :wave:")
    st.title("My name is KIRT")
with col2:
    st.image("images/avatarka.jpg")

st.title("KIRT's AI Bot")
st.subheader("Ask anything about me")
st.text_input("")
st.button("ASK", use_container_width=True)

st.title("")
st.title("")
st.title("")

col1, col2 = st.columns(2)

with col1:
    st.subheader("My Telegram")
with col2:
    st.image("images/kirt_04.png")