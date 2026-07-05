import streamlit as st

## Adding tab:

st.title("This is my blogpost")
st.markdown("""
 
 My name is cody. I live in NJ, USA. I am a student in Grade 6. ...

""")




tab1, tab2, tab3 = st.tabs(['Home','About', 'Contact'])


with tab1:
  st.title("Welcome to me web page! 🥳🥳🥳")
  st.header("This is my blog")
  st.subheader("This is the first post")

  st.divider()
  st.markdown(
    '''
      This is the playground for you to try streamlit and have fun.
      **There's :rainbow[so much] you can build!**
      
        We prepared a few examples for you to get started. Just 
        click on the buttons above and discover what you can do   
        with Streamlit. 

    '''
  )

  st.markdown(
    '''
      My name is Jane. I am student. Currently I am living in Canada. My hobbit is python coding, playing computer games.....
    '''
  )


  if st.button("Send balloons!"):
    st.balloons()

  if st.button("Send snowflake"):
    st.snow()


  st.header("This is my photo gallery")
  col1, col2, col3, col4 = st.columns(4)

  with col1:
      # st.image("https://static.streamlit.io/examples/cat.jpg")
      st.image('https://cdn.kingcounty.gov/-/media/king-county/depts/dph/images/health-safety/disease-illness/diseases-from-animals-zoonotic/gray-tabby-cat.jpg?rev=cf0242c3fa1e4e8d97e07bdb5c1c3c5d&hash=E87E00AB1127D469E0A2B839A1D68488')
      st.markdown("this is a cat named xxx")
      st.image("https://www.catit.com/wp-content/uploads/2023/08/breeds-43672-barney-bear-british-shorthair-854x854.jpg.webp")
      st.markdown("this is another cat named xxx")

  with col2:
      st.image("https://static.streamlit.io/examples/dog.jpg")
      st.markdown("this is a dog named xxx")
      st.image("https://hips.hearstapps.com/hmg-prod/images/shibainu-dog-royalty-free-image-1752089989.pjpeg?crop=1xw:1xh;center,top")
      st.markdown("this is another dog named xxx")

  with col3:
      st.image("https://static.streamlit.io/examples/owl.jpg")
      st.markdown("this is owl named xxx")

  with col4:
      st.image("https://cdn.britannica.com/10/250610-050-BC5CCDAF/Zebra-finch-Taeniopygia-guttata-bird.jpg")
      st.markdown("this is bird named xxx")

with tab2:
   st.markdown("About me")

with tab3:
   st.markdown("My contact information")



            