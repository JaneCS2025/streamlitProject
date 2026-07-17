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

       [data-testid="stAudio"] {
        display: none;
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

def showCornerImage(url, duration=5):
   placeholder = st.empty()
   placeholder.markdown(
      f'<div style="position: fixed; bottom: 0; left: 0;"><img src={url} width=300></img></div>',
       unsafe_allow_html=True
   )
   time.sleep(duration)
   placeholder.empty()

showUI('⭐️', ' Your score : ', st.session_state.score)
showUI('💰', ' Your coin : ', st.session_state.coin)

if st.button("Press to spin 🎲"):
   spin_sound = st.empty()
   spin_sound.audio("audio/spin.wav", autoplay=True)
   col1, col2, col3 = st.columns(3)
   box1 = col1.empty()
   box2 = col2.empty()
   box3 = col3.empty()

  
   # This is the spinning process
   for i in range(15):
      show_symbol(box1, random.choice(symbols))
      show_symbol(box2, random.choice(symbols))
      show_symbol(box3, random.choice(symbols))
      time.sleep(0.1)
   spin_sound.empty()   # stops the spin sound when spinning ends

   s1 = random.choice(symbols)
   s2 = random.choice(symbols)
   s3 = random.choice(symbols)

   show_symbol(box1, s1)
   show_symbol(box2, s2)
   show_symbol(box3, s3)
 

   clapping_sound = st.empty()
   if s1 == s2 == s3:  
      st.audio("audio/coin.wav", autoplay=True)
      clapping_sound.audio("audio/clapping.wav", autoplay=True)
      st.session_state.score +=10
      st.session_state.coin +=10
      rain(
         emoji=s1,
         font_size=100,
         falling_speed=5,
         animation_length=1
      )
      showBanner("🎉🎉🎉 Wow, you win, 3 match! Jackpot!")
      showCornerImage('https://i.pinimg.com/originals/86/96/59/869659344a7740d7692b439c01120c80.gif')
      clapping_sound.empty()
   elif s1 == s2 or s1 == s3 or s2 == s3:
      if s1 == s2 or s1==s3:
         em = s1
      elif s2==s3:
         em = s2
      st.audio("audio/coin.wav", autoplay=True)
      showBanner(" 2 match! Awesome 🤩!")
      clapping_sound.audio("audio/clapping.wav", autoplay=True)
      rain(
         emoji=em,
         font_size=100,
         falling_speed=5,
         animation_length=1
      )
      st.session_state.score +=5
      st.session_state.coin +=5
      showCornerImage('https://i.pinimg.com/originals/78/78/a2/7878a20aaed4de2b44a8b61fc38e9a36.gif')
      clapping_sound.empty()
   else:
      showBanner("So close! Try again 😀")




