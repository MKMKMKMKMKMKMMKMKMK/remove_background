import streamlit as st

st.page_link("app.py", label = "Home")
st.title('アプリケーション一覧')
st.page_link('pages/dotpicture.py', label='ドット絵変換アプリ')
st.page_link('pages/main.py',label='画像背景除去ツール')
st.page_link('pages/transparent.py',label='背景透明化ツール')
st.page_link('pages/screen-size.py',label='スクラッチの背景サイズにするツール')
