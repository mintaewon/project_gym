import streamlit as st
from datetime import datetime

st.title('gym')

st.markdown('---------')

date = st.date_input('오늘 날짜')


if st.button("프리웨이트존"):
    st.write(datetime.now())

if st.button("스미스머신"):
    st.write(datetime.now())

if st.button("파워레그프레스"):
    st.write(datetime.now())

if st.button("파워랙"):
    st.write(datetime.now())

if st.button("인클라인벤치"):
    st.write(datetime.now())

if st.button("플랫벤치"):
    st.write(datetime.now())

if st.button("숄더프레스머신"):
    st.write(datetime.now())

if st.button("케이블"):
    st.write(datetime.now())

if st.button("랫풀다운"):
    st.write(datetime.now())

if st.button("체스트플라이 머신"):
    st.write(datetime.now())

if st.button("체스트프레스 머신"):
    st.write(datetime.now())

if st.button("시티드로우머신"):
    st.write(datetime.now())

if st.button("레그프레스머신"):
    st.write(datetime.now())

if st.button("이너싸이머신"):
    st.write(datetime.now())

if st.button("레그 익스텐션"):
    st.write(datetime.now())

if st.button("레그컬"):
    st.write(datetime.now())
