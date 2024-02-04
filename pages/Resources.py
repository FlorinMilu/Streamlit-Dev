import streamlit as st
st.set_page_config(
    page_title="Resources",
    page_icon="📑",      
)

st.title("📑Resources")
 
#Sidebar 
with st.sidebar:    
    if st.button("Log Out"):
        st.switch_page("main.py")    
    st.title("What to do:")    
    st.page_link("pages/Home.py", label = "Home", icon = "🏠")
    st.page_link("pages/Resources.py", label = "Resources", icon = "📑")
    st.page_link("pages/RoadMap.py", label = "RoadMap", icon = "🎯",)
    st.markdown("---")
    st.link_button("📌Visit my GitHub to view the source code!👈","https://github.com/FlorinMilu/Streamlit-Dev")
