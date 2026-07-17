import streamlit as st

st.logo("https://i.pinimg.com/736x/8c/6d/db/8c6ddb5fe6600fcc4b183cb2ee228eb7.jpg", size="large", link="https://www.apple.com/ca/")

# Icon can go to Google fonts Icons to get Icon name
# https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded&selected=Material+Symbols+Rounded:pageview:FILL@0;wght@400;GRAD@0;opsz@24&icon.query=page&icon.size=24&icon.color=%231f1f1f

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.title("Log in")
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Log in")

    if submitted:
        if username == "admin" and password == "1234":
            st.session_state.logged_in = True
            st.session_state.username = username
            st.rerun()
        else:
            st.error("Incorrect username or password")
            

def logout():
    st.session_state.logged_in = False
    st.rerun()

login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

pages = {
  "Daily life": [
    st.Page("page1.py", title = "Page 1", icon=":material/contact_page:", default=True),
    st.Page("page2.py", title = "Page 2", icon=":material/contact_page:")
  ],

  "Favorite food": [
     st.Page("food.py", title = "Food")
  ],
  "Data Analytics": [
    st.Page("dataframe.py", title = "Table")
  ],
  "Game": [
    st.Page("game.py", title="Slot Machine")
  ],
  "Account": [logout_page],
}


if st.session_state.logged_in:
    pg = st.navigation(pages)
else:
    pg = st.navigation([login_page])


pg.run()