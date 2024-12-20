import streamlit as st
from src.currency_converter import CurrencyConverter
from src.utils import read_json


col_header, col_image = st.columns(2)
with col_header:
    
    st.markdown("### :currency_exchange: Currency Converter")
    st.markdown(
    """The Currency Converter App, built with Streamlit and a Python API,
    offers a user-friendly interface for real-time currency conversion.""")
    st.markdown(
    """Users input the amount and select source/target currencies,
    and the app dynamically calculates conversions based on up-to-date exchange rates.
    """
    )
with col_image:
    st.image("https://currencylab.io/wp-content/uploads/2020/11/Artboard-27-copy-2.png")

st.markdown("<hr>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

all_curency = read_json("src/constants/currency_tickers.json")

with col1:
    selected_currency = st.selectbox("From currency (Base): ", all_curency, index=0, key="c1")

with col2:
    target_currency = st.selectbox("To currency: (Target)", all_curency, index=0, key="c2")

with col3:
    amount = st.number_input('Enter amount: ', value=0.0, key="a")

obj = CurrencyConverter(selected_currency, target_currency)
exchange_rate = obj.get_exchange_rate()
result_amount = obj.calculate_amount(amount)




st.markdown("<hr>", unsafe_allow_html=True)
st.success(f"Exchange Rate: {exchange_rate}")
col_metric1, col_shape, col_metric2 = st.columns(3)

with col_metric1:
    st.metric("Base Currency", amount)
with col_shape:
    st.image('https://robnei.blog/wp-content/uploads/2020/08/flecha-37.png', width=130)
with col_metric2:
    st.metric("Converted Currency", result_amount)


st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("#### :information_desk_person: About this tool: ")
st.markdown("This Currency Converter App is a powerful tool designed for seamless currency conversion.")

st.markdown(
    """
    Leveraging the ExchangeRate API, the app provides real-time exchange rates to ensure accurate
    and up-to-date currency conversions.
    """
)

st.markdown(
    """
With a clean Streamlit interface,
    users can effortlessly input amounts, select source and target currencies,
    and receive instant and reliable conversion results.
""")
st.markdown("Simplify your currency exchange needs with this efficient and user-friendly tool.")