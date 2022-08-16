import streamlit as st
import requests

st.title('gym')

st.markdown('---------')

date = st.date_input('오늘 날짜')
select_weather = st.radio("오늘 날씨", ("맑음","비","눈"))

def req(use:list, weather:str=select_weather):
    data = {
        'use':use,
        'weather':weather
    }
    res = requests.post("http://34.64.172.90:8000/info/", json=data)
    # res = requests.post("http://host.docker.internal:8000/info/", json=data)
    # res = requests.post("http://localhost:8000/info/", json=data)
    st.write('Success')
    st.write(res.json()['date'])

equipments = [
    "프리웨이트",
    "프리웨이트(PTzone)",
    "런닝 머신",
    "싸이클",
    "파워랙",
    "파워랙(PTzone)",
    "스미스 머신",
    "파워 레그프레스",
    "플랫 벤치",
    "인클라인 벤치",
    "케이블",
    "케이블(PTzone)",
    "힙 익스텐션 머신",
    "레그프레스 머신",
    "이너싸이",
    "레그 익스텐션",
    "레그 컬",
    "숄더프레스 머신",
    "체스트 플라이 머신",
    "체스트 프레스 머신",
    "시티드 로우 머신",
    "랫풀다운",
    "랫풀다운(PTzone)",
    "싯업 벤치",
    "싯업 벤치(PTzone)",
    "백 익스텐션 머신",
    "어시스트 풀업 머신",
]

user_num_ls = []

for eq in equipments:
    user_num_ls.append(st.number_input(eq, step=1, min_value=0))

if st.button("수집"):
    req(user_num_ls)

# st.write('버튼 만들 예정')
# st.button("db다운로드")