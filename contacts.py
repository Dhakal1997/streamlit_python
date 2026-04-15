import streamlit as st

st.write("# My first app")
st.write("* app is going on")
st.info("Click Me do nth")
st.title("Rainy Day")
if st.button("Click Me"):
    st.write("Button clicked")
st.link_button("go to google", "https://www.google.com") 
name = st.text_input("Whats your name?", placeholder="Type here")
gender = st.selectbox("Gender", options=["male","female","dont wanna say"])
method = st.radio("Prefered contact method",options=["phone","email"])

if st.button("Submit"):
    st.write(f"Hello {name} ")
    st.write(f"Your gender is {gender} and prefer way of contact is {method}:  ")
    