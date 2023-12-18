import pickle
import streamlit as st

model = pickle.load(open('estimasi_wine.sav', 'rb'))

st.title('Estimasi kualitas anggur merah dan putih di portugal')

fixed_acidity = st.number_input('Input kadar asam yang tetap pada wine')
residual_sugar = st.number_input('input km sisa gula setelah fermentasi')
chlorides = st.number_input('input pajak banyaknya garam')
density = st.number_input('input kepadataan air terhadap anggurnya')
pH = st.number_input('input pH')
alcohol = st.number_input('input persenan alkohol')

predict = ''

if st.button('hitung'):
    predict = model.predict(
        [[fixed_acidity,residual_sugar,chlorides,density,pH,alcohol]]
    )
    st.write('kualitasnya dari (skala 0-10) : ', predict)
