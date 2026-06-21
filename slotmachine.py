import streamlit as st
import random
import time
from streamlit_extras.let_it_rain import rain

##https://janeslotmachine.streamlit.app/

symbols = ['🍒', '🍿', '🎁', '🐸', '⭐️']

st.image('https://prodimages.everythingneon.com/giant/l100-7798-casino-animated-led-sign.gif')

#session state - python object store value in memory
# st.write('st.session_state', st.session_state)

if "score" not in st.session_state:
    st.session_state['score'] = 0

if "coin" not in st.session_state:
    st.session_state['coin'] = 0


if st.button('🎲 SPIN Match 2 for some coins, match 3 for the jackpot!'):
    col1, col2, col3 = st.columns(3)
    box1 = col1.empty()
    box2 = col2.empty()
    box3 = col3.empty()

    for i in range(15):
        box1.markdown(
            f"<div style='font-size:120px;text-align:center'>{random.choice(symbols)}</div>",
            unsafe_allow_html=True
        )

        box2.markdown(
            f"<div style='font-size:120px;text-align:center'>{random.choice(symbols)}</div>",
            unsafe_allow_html=True
        )
        box3.markdown(
            f"<div style='font-size:120px;text-align:center'>{random.choice(symbols)}</div>",
            unsafe_allow_html=True
        )
        time.sleep(0.2)

    s1 = random.choice(symbols)
    s2 = random.choice(symbols)
    s3 = random.choice(symbols)

    box1.markdown(
            f"<div style='font-size:120px;text-align:center'>{s1}</div>",
            unsafe_allow_html=True
        )
    box2.markdown(
            f"<div style='font-size:120px;text-align:center'>{s2}</div>",
            unsafe_allow_html=True
        )
    box3.markdown(
            f"<div style='font-size:120px;text-align:center'>{s3}</div>",
            unsafe_allow_html=True
        )

###### Write the condition logic here #####
    if s1 == s2 == s3:
        
        st.session_state.score +=100
        st.session_state.coin +=50
        text = '🎉🍿⭐️Jackpot! 3 match!! You won 100 points and 50 coins!!'
        st.markdown(
            f"<div style='font-size:20px; color: white'>{text}</div>",
            unsafe_allow_html=True
        )
        st.image('https://condaluna.com/assets/stickers/congrats.gif')
       
        
        
    elif s1 == s2 or s1 == s3 or s2 == s3:
        if s1 == s2:
            matched_symbol = s1
        elif s1 == s3:
            matched_symbol = s1
        else:  # s2 == s3
            matched_symbol = s2
        
        st.session_state.score +=10
        st.session_state.coin +=10
        rain(
                emoji= matched_symbol,
                font_size=100,
                falling_speed=5,
                animation_length=1

            )
       
    else:
        rain(
            emoji='💩',
            font_size=100,
            falling_speed=5,
            animation_length=0.5
        )
       

# st.write(f'### ⭐️ Your score: {st.session_state.score}')
# st.write(f'### 🪙 Your coin: {st.session_state.coin}')

st.markdown(
  f"### ⭐️ <span style='color: white'>  Your score:  {st.session_state.score}</span>", unsafe_allow_html=True)
st.markdown(
  f"### 💰 <span style='color: white'>  Your coin:  {st.session_state.coin}</span>", unsafe_allow_html=True)
        

##Add background image
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://static.vecteezy.com/system/resources/thumbnails/003/810/467/small/casino-advertising-neon-banner-design-with-playing-cards-and-casino-chips-on-purple-background-vector.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<style>
div.stButton > button {
    background-color: purple;
    color: white;
    font-size: 50px;
    font-weight: bold;
    border-radius: 12px;
    border: none;
    width: 500px
}

/* Disable hover effect */
div.stButton > button:hover {
    background-color: purple !important;
    color: white !important;
    border: none !important;
    transform: none !important;
    box-shadow: none !important;
}
</style>
""", unsafe_allow_html=True)