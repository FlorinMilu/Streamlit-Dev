import streamlit as st
st.set_page_config(
    page_title="Welcome!",
    page_icon="👋",      
)

st.sidebar.link_button("📌Visit my GitHub to view the source code!👈","https://github.com/FlorinMilu/Disease-Prediction")
st.title("Hello!👋 This is my license paper page!")
st.subheader("Student: Milu Mihai-Florin")
st.text("This is a web application for my licence paper which is about\nPredicting diseases from MRI scans")
st.markdown("---")
st.markdown(
    """
    This app is aiming to make possible the uploading of images from
    MRI scans and helping pathologists in identifying and predicting the 
    state of breast carcinoma in women.    
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)
