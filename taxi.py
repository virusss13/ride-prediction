import streamlit as st
import pickle

st.title("taxi rider prediction")
pp=st.number_input("enter the price per weak")
pop=st.number_input("enter population")
mon=st.number_input("Enter monthly income")
avg=st.number_input("average parking per month")
button=st.button("submit")
if button:
    lr=pickle.load(open("taxi.pkl","rb"))
    res = round(lr.predict([[pp, pop, mon, avg]])[0], 2)
    st.markdown(f"Number of weekly riders:{res}")