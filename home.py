import streamlit as st
from model_lib import premium_predict

st.title("⛨ Know your Healthcare Premium", text_alignment = 'center')
st.write("<h5 style='text-align: center;'>by 🛡️S.H.I.E.L.D insurance</h5>",unsafe_allow_html = True)
st.divider()

st.space("small")

st.set_page_config(layout="wide")

col_left, col1, col2, col3, col_right = st.columns([1, 1, 1, 1, 1])

with col_left:
    st.image("images/medit.png", width = 200)

with col_right:
    st.image("images/health.png", width = 200)

with col1:
    age = st.number_input("Age", min_value=18, max_value=100)
    st.space("xsmall")
    st.write("Diseases (select all that apply)")
    diab,hd,bp,th = 0,0,0,0
    pred = None

    if st.checkbox("Diabetes"):
        diab = 1
    if st.checkbox("Heart Disease"):
        hd = 1
    if st.checkbox("High Blood Pressure"):
        bp = 1
    if st.checkbox("Thyroid"):
        th = 1


with col2:
    bmi = st.selectbox("BMI",  ['Underweight', 'Normal', 'Overweight', 'Obesity'])
    st.space("xsmall")
    in_plan = st.selectbox("Insurance Plan",  ['Bronze', 'Silver', 'Gold'] )
with col3:
    smoke = st.selectbox("Smoking Status", ['No Smoking', 'Occasional', 'Regular'])
    st.space("xsmall")
    grisk = st.number_input("Genetical Risk", min_value=0, max_value=5)

data = {}
data['age'] = age; data['bmi_category'] = bmi; data['smoking_status'] = smoke
data['insurance_plan'] = in_plan; data['genetical_risk'] = grisk; data['diabetes'] = diab
data['heart_disease'] = hd; data['high_blood_pressure'] = bp; data['thyroid'] = th

# Create 3 columns
col1, col2, col3 = st.columns([2, 1, 2])

with col2:
    st.space("small")
    submit = st.button("submit", type="primary", use_container_width=True)

if submit:

    with col2:
        with st.spinner("Processing..."):
    
            #fetch the prediction
            pred = premium_predict(data)

# now print the result
if pred:
    st.space("small")
    st.write("<h5 style='text-align: center;'>Annual Premium Amount</h5>",unsafe_allow_html = True)
    st.write(f"<h5 style='text-align: center; color: yellow;'>₹ {pred[0]:,.2f}</h5>",unsafe_allow_html = True)