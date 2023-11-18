import streamlit as st
user_input = st.text_input('Enter flat type:')

predicted_price = model.predict([[user_input]])
st.write(f'Predicted Resale Price: {predicted_price[0]}')
