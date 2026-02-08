import streamlit as st
from urllib.parse import quote_plus

st.set_page_config(page_title="OSC Auto", page_icon="🔧", layout="wide")
st.title("🔧 OSC Auto - Wyszukiwarka części OEM")

with st.form("szukaj"):
    fraza = st.text_input("🔍 Podaj kod OEM lub nazwę części:", placeholder="np. 1K0615301M")
    szukaj = st.form_submit_button("Szukaj", use_container_width=True)

if szukaj and fraza:
    st.success(f"Szukam: **{fraza}**")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🛍️ Allegro")
        link = f"https://allegro.pl/listing?string={quote_plus(fraza)}&order=p"
        st.link_button("Otwórz Allegro", link, use_container_width=True)
    
    with col2:
        st.markdown("### 🔷 Ovoko")
        link = f"https://ovoko.pl/szukaj?q={quote_plus(fraza)}"
        st.link_button("Otwórz Ovoko", link, use_container_width=True)
    
    with col3:
        st.markdown("### 🟢 OLX")
        link = f"https://www.olx.pl/oferty/q-{quote_plus(fraza)}/?search%5Border%5D=filter_float_price%3Aasc"
        st.link_button("Otwórz OLX", link, use_container_width=True)

st.markdown("---")
st.caption("OSC Auto © 2024")
