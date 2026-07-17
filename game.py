import streamlit as st
from streamlit_extras.let_it_rain import rain
import random
import time

symbols = ['🍀', '🍒', '🍿', '🎁', '🐸','🐶', '🐙']

st.image("https://prodimages.everythingneon.com/giant/l100-7798-casino-animated-led-sign.gif")

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
## Initialize the session_state
if "coin" not in st.session_state:
   st.session_state['coin'] = 0

if 'score' not in st.session_state:
   st.session_state['score'] = 0


##Make function to render the text to white color:
def show_symbol(box, symbol):
      box.markdown(
         f"<p style='font-size: 100px; text-align: center; margin: 0'>{symbol}</p>",
         unsafe_allow_html=True
      )

def showUI(icon, text, state):
   st.markdown(
   f'<p style="font-size: 25px; color: white">{icon} {text} {state}</p>',  unsafe_allow_html=True
   )

def showBanner(text):
   st.markdown(
      f'<p style="font-size: 25px; color: yellow">{text}</p>'
   ,  unsafe_allow_html=True)

showUI('⭐️', ' Your score : ', st.session_state.score)
showUI('💰', ' Your coin : ', st.session_state.coin)

if st.button("Press to spin 🎲"):
   col1, col2, col3 = st.columns(3)
   box1 = col1.empty()
   box2 = col2.empty()
   box3 = col3.empty()

  
   # This is the spinning process
   for i in range(15):
      show_symbol(box1, random.choice(symbols))
      show_symbol(box2, random.choice(symbols))
      show_symbol(box3, random.choice(symbols))
      time.sleep(0.2)

   s1 = random.choice(symbols)
   s2 = random.choice(symbols)
   s3 = random.choice(symbols)

   show_symbol(box1, s1)
   show_symbol(box2, s2)
   show_symbol(box3, s3)

   if s1 == s2 == s3:
      st.session_state.score +=10
      st.session_state.coin +=10
      rain(
         emoji=s1,
         font_size=100,
         falling_speed=5,
         animation_length='10'
      )
      showBanner("🎉🎉🎉 Wow, you win, 3 match! Jackpot!")
   elif s1 == s2 or s1 == s3 or s2 == s3:
      if s1 == s2 or s1==s3:
         em = s1
      elif s2==s3:
         em = s2

      showBanner(" 2 match! Awesome 🤩!")
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
      showBanner("So close! Try again 😀")




