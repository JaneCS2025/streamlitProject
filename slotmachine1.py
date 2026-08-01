import streamlit as st
from streamlit_extras.let_it_rain import rain
import random
import time

##https://janeslotmachine.streamlit.app/

symbols = ['🍒', '🍿', '🎁', '🐸', '⭐️']

st.markdown("""
 <style>
   .stApp{
     background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGfQ9yM3Fo_vDyLe5J_0KT1RaAI-zNJci-PWICeIFyzA&s=10");
     background-size:cover;
     background-repeat:no-repeat;
   }
   [data-testid='stAudio']{
      display: none;
   }
 </style>

"""
,
unsafe_allow_html=True
)

# st.title("🎰 WIN BIG SLOT MACHINE 🥳🥳🥳")
st.markdown("""
<h1 style="color: #f7f5e6; font-size: 48px">🎰 WIN BIG SLOT MACHINE 🥳🥳🥳</h1>
""", unsafe_allow_html=True)
# st.write("Press the button to spin")

st.markdown("""
<p style="color: #f7f5e6; font-size: 16px">Press the button to spin</p>
""", unsafe_allow_html=True)

#session state - python object store value in memory
# st.write('st.session_state', st.session_state)

if "score" not in st.session_state:
    st.session_state['score'] = 0

if "coin" not in st.session_state:
    st.session_state['coin'] = 0


def showSymbol(box, symbol):
    box.markdown(
        f'<p style="font-size: 100px; text-align: center; margin: 0;">{symbol}</p>', unsafe_allow_html=True
    )

def showCornerGif(url, duration=5):
    placeholder = st.empty()
    placeholder.markdown(
        f'<p style="position: fixed; bottom:0; left:0;"><img src={url} width=300></img></p>', unsafe_allow_html=True
    )
    time.sleep(duration)
    placeholder.empty()

if st.button('🎲 SPIN Match 2 for some coins, match 3 for the jackpot!'):
    #start sound effects
    spin_sound = st.empty()
    spin_sound.audio('audio/spin.wav', autoplay=True)

    col1, col2, col3 = st.columns(3)
    box1 = col1.empty()
    box2 = col2.empty()
    box3 = col3.empty()

    for i in range(15):
        showSymbol(box1, random.choice(symbols))
        showSymbol(box2, random.choice(symbols))
        showSymbol(box3, random.choice(symbols))
        time.sleep(0.2)

    #stop the spin sound effect
    spin_sound.empty()

    s1 = random.choice(symbols)
    s2 = random.choice(symbols)
    s3 = random.choice(symbols)

    showSymbol(box1, s1)
    showSymbol(box2, s2)
    showSymbol(box3, s3)

    clapping_sound = st.empty()
###### Write the condition logic here #####
    if s1 == s2 == s3:
        clapping_sound.audio('audio/clapping.wav', autoplay=True)
        st.success("🎉🎉🎉 Jackpot! 3 match!! You won 100 points and 50 coins!!")
        st.audio("audio/coin.wav", autoplay=True)
        st.session_state.score +=100
        st.session_state.coin +=50
        showCornerGif('https://i.pinimg.com/originals/78/78/a2/7878a20aaed4de2b44a8b61fc38e9a36.gif')
        rain(
            emoji=s1,
            font_size=100,
            falling_speed=5,
            animation_length=1
        )
        clapping_sound.empty()
    elif s1 == s2 or s1 == s3 or s2 == s3:
        if s1==s2 or s1 == s3:
            em = s1
        elif s2 == s3:
            em = s2
        st.audio("audio/coin.wav", autoplay=True)
        clapping_sound.audio('audio/clapping.wav', autoplay=True)
        st.success("✨ Nice! 2 match! You won 10 coins!")
        st.session_state.score +=10
        st.session_state.coin +=10
        rain(
              emoji= em,
              font_size=100,
              falling_speed=5,
              animation_length=1
             )
        showCornerGif('https://i.pinimg.com/originals/86/96/59/869659344a7740d7692b439c01120c80.gif')
        clapping_sound.empty()
    else:
        st.info("So close! Try again 😝")

st.markdown(f'<p style="color: white; font-size: 35px">⭐️ Your score: {st.session_state.score}</p>', unsafe_allow_html=True)
st.markdown(f'<p style="color: #ffe8cc; font-size: 35px">💰 Your coin: {st.session_state.coin}</p>', unsafe_allow_html=True)

        


