import streamlit as st
from streamlit_option_menu import option_menu


options_log_in = option_menu('Welcome to the Acadmy', ['Login', 'Register'], icons = ['box-arrow-in-left', 'brightness-high'], orientation =  'horizontal')

if options_log_in == 'Login': 
    username = st.text_input('Username')
    password = st.text_input('Password')


    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col3:
        button_log_in = st.button ('Log in')


if options_log_in == 'Register': 
    username = st.text_input('Username')
    password = st.text_input('Password')
    password_repeat = st.text_input('reeinter Password')
    phone_num = st.text_input('phone')

    terms  = st.checkbox ('terms')
    if terms:
        st.write ('Terms')
        col1, col2, col3, col4, col5 = st.columns(5)
        with col3:
            button_log_in = st.button ('Register')


