import streamlit as st
st.set_page_config(
    page_title="Home",
    page_icon="🏠",      
)
st.title("🏠Home")

st.sidebar.title("What to do")

app_mode = st.sidebar.selectbox("Choose the app_mode",["Insert the image/s", "View Output"])
if app_mode == "Insert the image/s":    
    st.write("""### Insert the image/s""")
    st.file_uploader("Submit you file")
elif app_mode == "View Output":
    st.write("""### Output View""")    

