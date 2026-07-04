import streamlit as st

st.logo("https://i.pinimg.com/736x/8c/6d/db/8c6ddb5fe6600fcc4b183cb2ee228eb7.jpg", size="large", link="https://www.apple.com/ca/")

pages = {
  "Daily life": [
    st.Page("page1.py", title = "Page 1"),
    st.Page("page2.py", title = "Page 2")
  ],

  "Favorite food": [
     st.Page("food.py", title = "Food")
  ],
  "Data Analytics": [
    st.Page("dataframe.py", title = "Table")
  ]
}

pg = st.navigation(pages)
pg.run()