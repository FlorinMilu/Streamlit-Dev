#Modules
import streamlit as st
import pyrebase as pb
from streamlit_option_menu import option_menu 
st.set_page_config(
    page_title="Welcome",
    page_icon="👋",      
)


#Configuration Key for the Firebase Authentication method
firebaseConfig = {
    'apiKey': "AIzaSyCXfldMfi_W_rgJFXmy5-SpWevmNvBNnew",
    'authDomain': "streamlitapp-300b6.firebaseapp.com",
    'databaseURL': "https://streamlitapp-300b6-default-rtdb.europe-west1.firebasedatabase.app/",
    'projectId': "streamlitapp-300b6",
    'storageBucket': "streamlitapp-300b6.appspot.com",
    'messagingSenderId': "959468841208",
    'appId': "1:959468841208:web:b6df8801456c24ff12f30d",
    'measurementId': "G-18W3Q8JWXH"
  };
#Firebase Authentication
firebase = pb.initialize_app(firebaseConfig)
auth = firebase.auth()

#Database
db = firebase.database()
storage = firebase.storage()




st.title("Hello!👋 This is my license paper page!")
st.subheader("Student: Milu Mihai-Florin")
st.text(
    """
        This is a web application for my licence paper which is about
        helping pathologists to predict diseases from MRI scans.        
        The focus of the app is to allow users to upload medical images
        from which the model segments and estimates volume of tumors.
    """
    )
st.markdown("---")

#Authentication
with st.sidebar:
    selected =  option_menu(
        menu_title=None,
        options=["Log In", "Sign Up"],
        icons=["", ""],
        menu_icon=None,
        default_index=0,
        orientation="horizontal",    
    )    
    email = st.text_input('Please enter your email address')
    password = st.text_input('Please enter you password', type = 'password')        

    if selected == "Log In":
        login = st.button('Log In')
        if login:
            user = auth.sign_in_with_email_and_password(email, password)                
            db.child(user['localId']).child("ID").set(user['localId'])        
            if user:
                st.switch_page("pages/Home.py")
    elif selected == "Sign Up":
        submit = st.button('Create my account')
        if submit:
            user = auth.create_user_with_email_and_password(email,password)        
            st.balloons()
            #Sign in
            user = auth.sign_in_with_email_and_password(email,password)
            if user:                
                db.child(user['localId']).child("ID").set(user['localId'])        
                st.sidebar.success('Your account is created successfully!')  
                st.sidebar.info("Now you can Log In!")                
