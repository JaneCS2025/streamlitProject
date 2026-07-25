
import streamlit as st

st.logo("https://i.pinimg.com/736x/8c/6d/db/8c6ddb5fe6600fcc4b183cb2ee228eb7.jpg", size="large", link="https://www.apple.com/ca/")

#st.write(st.session_state)

if "logged_in" not in st.session_state:
  st.session_state.logged_in = False


def login():
  st.title("Log In")
  with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    submitted = st.form_submit_button("Log In")

  if submitted:
    if username == 'admin' and password == '1234':
       st.session_state.logged_in = True
       st.session_state.username = username
       st.rerun()
    else:
      st.error("username and password incorrect")


def logout():
  st.session_state.logged_in = False
  st.rerun()


login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

pages = {
  "Daily life": [
    st.Page("page1.py", title = "Page 1", icon=":material/home:", default=True),
    st.Page("page2.py", title = "Page 2", icon=":material/contact_page:")
  ],

  "Favorite food": [
     st.Page("food.py", title = "Food", icon=":material/icecream:")
  ],
  "Data Analytics": [
    st.Page("dataframe.py", title = "Table", icon=":material/data_thresholding:")
  ],
  "Game": [
    st.Page("game.py", title="Slot Machine", icon=":material/sports_esports:")
  ],
  "Settings": [
    logout_page
  ]
}

if st.session_state.logged_in:
  pg = st.navigation(pages)
else:
  pg = st.navigation([login_page])


pg.run()