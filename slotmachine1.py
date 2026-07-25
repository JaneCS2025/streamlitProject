import streamlit as st
import random
import time

##https://janeslotmachine.streamlit.app/

symbols = ['🍒', '🍿', '🎁', '🐸', '⭐️']

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


if st.button('🎲 SPIN Match 2 for some coins, match 3 for the jackpot!'):
    col1, col2, col3 = st.columns(3)
    box1 = col1.empty()
    box2 = col2.empty()
    box3 = col3.empty()

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

###### Write the condition logic here #####
    if s1 == s2 == s3:
        st.success("🎉🎉🎉 Jackpot! 3 match!! You won 100 points and 50 coins!!")
        st.session_state.score +=100
        st.session_state.coin +=50
        st.snow()
    elif s1 == s2 or s1 == s3 or s2 == s3:
        st.success("✨ Nice! 2 match! You won 10 coins!")
        st.session_state.score +=10
        st.session_state.coin +=10
        st.balloons()
    else:
        st.info("So close! Try again 😝")

st.markdown(f'<p style="color: white; font-size: 35px">⭐️ Your score: {st.session_state.score}</p>', unsafe_allow_html=True)

# st.write(f'### 🪙 Your coin: {st.session_state.coin}')
        

st.markdown("""
 <style>
   .stApp{
     background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGfQ9yM3Fo_vDyLe5J_0KT1RaAI-zNJci-PWICeIFyzA&s=10");
     background-size:cover;
     background-repeat:no-repeat;
   }
 </style>


"""
,
unsafe_allow_html=True
)
