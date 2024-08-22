import streamlit as st

st.header('Calculator App')
st.write('this is a calculator application developed using streamlit')
button=st.button('welcome')
if button:
    st.balloons()

num1=st.number_input('enter the first number',value=0)
option=st.selectbox('select the operation',("+","-","*","/"))
num2=st.number_input('enter the second number',value=0)
button1=st.button('calculate')
if button1:
    if option=="+":
        st.subheader(f"added result is  {round(num1+num2)}")
    elif option=="-":
        st.subheader(f"substracted result is  {num1-num2}")
    elif option=="*":
        st.subheader(f"multiplied result is  {num1*num2}")
    elif option=="/":
        st.subheader(f"divided result is  {num1/num2}")
        