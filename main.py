import streamlit as st

st.title("Welcome to me web page! 🥳🥳🥳")
st.header("This is my blog")
st.subheader("This is the first post")

st.divider()

st.markdown(
  '''
     This is the playground for you to try streamlit and have fun.
     **There's :rainbow[so much] you can build!**
    
      We prepared a few examples for you to get started. Just 
      click on the buttons above and discover what you can do   
      with Streamlit. 

  '''
)

if st.button("Send balloons!"):
  st.balloons()

st.button("click me")