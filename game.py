import streamlit as st
from streamlit_extras.let_it_rain import rain
import random
import time

symbols = ['🍀', '🍒', '🍿', '🎁', '🐸']


st.image("https://prodimages.everythingneon.com/giant/l100-7798-casino-animated-led-sign.gif")
# st.write("Press the button to spin")
st.markdown("""
  <p style="color: white; font-size: 16px">Press the button to spin</p>
""",
 unsafe_allow_html=True
)

st.divider()


## Initialize the session_state
if "coin" not in st.session_state:
   st.session_state['coin'] = 0

if 'score' not in st.session_state:
   st.session_state['score'] = 0

if st.button("Press to spin 🎲"):
   col1, col2, col3 = st.columns(3)
   box1 = col1.empty()
   box2 = col2.empty()
   box3 = col3.empty()

   # This is the spinning process
   for i in range(15):
      box1.header(random.choice(symbols))
      box2.header(random.choice(symbols))
      box3.header(random.choice(symbols))
      time.sleep(0.2)

   s1 = random.choice(symbols) 
   s2 = random.choice(symbols) 
   s3 = random.choice(symbols) 

   box1.header(s1)
   box2.header(s2)
   box3.header(s3)

   if s1 == s2 == s3:
      st.session_state.score +=10
      st.session_state.coin +=10
      rain(
         emoji=s1,
         font_size=100,
         falling_speed=5,
         animation_length='10'
      )
      st.success("🎉🎉🎉 Wow, you win, 3 match! Jackpot!")
   elif s1 == s2 or s1 == s3 or s2 == s3:
      if s1 == s2 or s1==s3:
         em = s1
      elif s2==s3:
         em = s2
      st.success(" 2 match! Awesome!")
      st.session_state.score +=5
      st.session_state.coin +=5
      # st.balloons()
      rain(
         emoji=em,
         font_size=100,
         falling_speed=5,
         animation_length='10'
      )
   else:
      st.info("So close! Try again 😀")


st.write(f'⭐️ Your score: {st.session_state.score}')
st.write(f'💰 Your coin: {st.session_state.coin}')

st.markdown(
   """
    <style>
       .stApp {
         background-image: url("https://static.vecteezy.com/system/resources/thumbnails/003/810/467/small/casino-advertising-neon-banner-design-with-playing-cards-and-casino-chips-on-purple-background-vector.jpg");
         background-size: cover;
         background-repeat: no-repeat;
       }  
       .block-container{
        background: transparent !important;
       }

       section .main > div {
        background: transparent !important;
       }

    </style>     

   """,
   unsafe_allow_html=True
)