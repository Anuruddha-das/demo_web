import streamlit as st

name = st.text_input("Enter your name :")
text = st.text_area("Enter your text :")
passion = st.selectbox("enter your passion",("developing","programming","engineering","doctor","others"))
button = st.button("submit")
if button==True:
    st.markdown(f'''{name}
, {text}, {passion}''')
    st.code("""import streamlit as st

name = st.text_input("Enter your name :")
text = st.text_area("Enter your text :")
passion = st.selectbox("enter your passion",("developing","programming","engineering","doctor","others"))
button = st.button("submit")
if button==True:
    st.markdown(f'''{name}
, {text}, {passion}''')
    st.code(#paste your entire code here)""")