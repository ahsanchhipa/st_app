import streamlit as st
import pandas as pd

name = st.text_input("Enter Your Name: ")
Fname=  st.text_input("Enter Your Father Name: ")
adr= st.text_area("Enter Your Text: ")
classdata = st.selectbox("Enter your Designation: ",(" ","SRAaaaaaaaa","RA", "PA", "RS" ) )
