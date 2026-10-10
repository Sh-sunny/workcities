import streamlit as st

st.set_page_config(page_title="Work Cities", page_icon="🏙️")

st.title("Work Cities")
st.write(
    """
    Welcome to Work Cities — your gateway to exploring city-based work data in an interactive app.
    Click the button below to open the main application.
    """
)

if st.button("Go to App"):
    st.switch_page("pages/app.py")
