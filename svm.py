
import streamlit as st
import pickle
 
st.title("SVM Implementation")
age=st.number_input("Enter age")
es=st.number_input("Enter estimated salary")

button=st.button("Purchased")
if button:
    model=pickle.load(open("svc.pkl","rb"))
    res=model.predict([[age,es]])[0]
    if res == 0:
        st.markdown("No")
    elif res == 1:
        st.markdown("No") 
    