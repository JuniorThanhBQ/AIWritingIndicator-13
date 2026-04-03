import streamlit as st

pg = st.navigation([
    st.Page("pages/Home.py", title="Trang chủ"),
    st.Page("pages/FAQ.py", title="Hướng dẫn sử dụng"),
    st.Page("pages/Check.py", title="Check AI"),
])
pg.run()
