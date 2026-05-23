import streamlit as     
st.set_page_config(
    page_title="Kuliah Praktisi",
    pagee_icon="tada",
    layout="wide"
)


#Hirarki teks
st_tittle("Dashboard")
st.header("Laporan Bulanan")
st.subheader("Monthly Expenses")
st.caption ("Made with love")

import streamlit as st

st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("See explanation"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')
    st.image("https://static.streamlit.io/examples/dice.jpg")
