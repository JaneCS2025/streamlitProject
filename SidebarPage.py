import streamlit as st

st.logo("https://i.pinimg.com/736x/8c/6d/db/8c6ddb5fe6600fcc4b183cb2ee228eb7.jpg", size='large', link="https://www.youtube.com/watch?v=dQw4w9WgXcQ" )

pages = {
 "Daily Life": [
   st.Page("page1.py", title="Self Introduction"),
   st.Page("page2.py", title="Page 2")
 ],
 "Food": [
   st.Page("food.py", title="Self Introduction"),
 ]

}

pg = st.navigation(pages)
pg.run()

