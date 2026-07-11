import streamlit as st

st.logo("https://play-lh.googleusercontent.com/2SL3gubcMu57VsxUCBQX5unIzAkm2kdTB8aZwPoxu39u02dxIwxlYGwlfu8gimNWrE3HzzavYcggk89rwYZp0bg", size="large")

pages = {
  "Daily Life":[
    st.Page("page1.py", title="Page 1"),
    st.Page("page2.py", title="Page 2")
  ],
  "Food": [
    st.Page("food.py", title="Chicken Salad"),
  ],
  "Game": [
    st.Page("game.py", title="Slot Machine")
  ]
}


pg = st.navigation(pages)
pg.run()