import streamlit as st

tab1, tab2, tab3 = st.tabs(['Home', 'About', 'Contact'])

with tab1:
  st.title("Welcome to Home page 📃")
  st.header("This is the first post")
  st.subheader('This is the subheader')

  st.divider()

  st.markdown("""
    This is Jane. I am a student. I am currently in Canada. ....
  """)

 #making some badge
  st.badge("New")
  st.badge("Success", icon=":material/check:", color='green')
  st.markdown(":yellow-badge[:material/star: Favorite] :orange-badge[‼️ Needs review] :grey-badge[:material/check: Deprecated]")

  #Display text in small font
  st.caption("This is written small caption text 🍀")

  #Display code block

  code = '''
     def Hello():
       print("Hello Streamlit!")    
  ''' 

  st.code(code, language='python')

  st.text("This is a line1\n Add more text in line 2")

  st.html("<p style='color:red; font-size: 40px; font-weight: 900'>😀 This is html paragraph element</p>")

  
with tab2:
  #embedded a video
  # st.title("Chicken Salad Lesson")
  st.html("<p style='color: #915000; font-size: 30px'>Chicken Salad Lesson 1</p>")
  st.caption("This a introduction for creating chicken salad")
  st.iframe("https://www.youtube.com/embed/ShUh33xMGVY?si=OssEZJAiXxkMqc7K", width=560, height=315)
  

