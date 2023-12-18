import pickle
import streamlit as st

model = pickle.load(open('estimasi_wine.sav', 'rb'))

st.title('Estimasi kualitas anggur merah dan putih di portugal')

fixed_acidity = st.number_input('Input kadar asam yang tetap pada wine', step=0.000001)
residual_sugar = st.number_input('input km sisa gula setelah fermentasi', step=0.000001)
chlorides = st.number_input('input pajak banyaknya garam', step=0.000001)
density = st.number_input('input kepadataan air terhadap anggurnya', step=0.000001)
pH = st.number_input('input pH', step=0.000001)
alcohol = st.number_input('input persenan alkohol', step=0.000001)

predict = ''

if st.button('hitung'):
    predict = model.predict(
        [[fixed_acidity,residual_sugar,chlorides,density,pH,alcohol]]
    )
    st.write('kualitasnya dari (skala 0-10) : ', predict)
