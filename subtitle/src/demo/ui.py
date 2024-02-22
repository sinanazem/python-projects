import streamlit as st
from src.parse_subtitle import Subtitle
from src.data import DATA_DIR

st.header(":clapper:English with Movies")
uploaded_file = st.file_uploader("upload a subtitle(srt format)",type=[".srt"])

st.write(uploaded_file)

sub_file_path = DATA_DIR / "Subtitle" / 'Game of Thrones - 1x01 - Winter is Coming.720p HDTV.en.srt'
s = Subtitle(sub_file_path)

for sub in s.subs:
    st.write(sub.text)
# cols = st.columns(2)