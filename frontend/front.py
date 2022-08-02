import streamlit as st
from datetime import datetime
import requests

st.title('gym')

st.markdown('---------')

date = st.date_input('오늘 날짜')

if st.button("프리웨이트존"):
    data = {
        'name':'FreeWeight',
        'num':0
    }
    requests.post("http://localhost:8000/info/", json=data)
    st.write('Success')
    st.write(datetime.now())

if st.button("스미스머신"):
    data = {
        'name':'SmithMachine',
        'num':1
    }
    requests.post("http://localhost:8000/info/", json=data)
    st.write(datetime.now())

if st.button("파워레그프레스"):
    data = {
        'name':'PowerLegPress',
        'num':2
    }
    requests.post("http://localhost:8000/info/", json=data)
    st.write(datetime.now())

if st.button("파워랙"):
    data = {
        'name':'PowerRack',
        'num':3
    }
    requests.post("http://localhost:8000/info/", json=data)
    st.write(datetime.now())

if st.button("인클라인벤치"):
    data = {
        'name':'InclineBench',
        'num':4
    }
    requests.post("http://localhost:8000/info/", json=data)
    st.write(datetime.now())

if st.button("플랫벤치"):
    data = {
        'name':'FlatBench',
        'num':5
    }
    requests.post("http://localhost:8000/info/", json=data)
    st.write(datetime.now())

if st.button("숄더프레스머신"):
    data = {
        'name':'ShoulderPressMachine',
        'num':6
    }
    requests.post("http://localhost:8000/info/", json=data)
    st.write(datetime.now())

if st.button("케이블"):
    data = {
        'name':'Cable',
        'num':7
    }
    requests.post("http://localhost:8000/info/", json=data)
    st.write(datetime.now())

if st.button("랫풀다운"):
    data = {
        'name':'LatPulldown',
        'num':8
    }
    requests.post("http://localhost:8000/info/", json=data)
    st.write(datetime.now())

if st.button("체스트플라이 머신"):
    data = {
        'name':'ChestFlyMachine',
        'num':9
    }
    requests.post("http://localhost:8000/info/", json=data)
    st.write(datetime.now())

if st.button("체스트프레스 머신"):
    data = {
        'name':'ChestPressMachine',
        'num':10
    }
    requests.post("http://localhost:8000/info/", json=data)
    st.write(datetime.now())

if st.button("시티드로우머신"):
    data = {
        'name':'SeatedRowMachine',
        'num':11
    }
    requests.post("http://localhost:8000/info/", json=data)
    st.write(datetime.now())

if st.button("레그프레스머신"):
    data = {
        'name':'LegPressMachine',
        'num':12
    }
    requests.post("http://localhost:8000/info/", json=data)
    st.write(datetime.now())

if st.button("이너타이머신"):
    data = {
        'name':'InnerThighMachine',
        'num':13
    }
    requests.post("http://localhost:8000/info/", json=data)
    st.write(datetime.now())

if st.button("레그 익스텐션"):
    data = {
        'name':'LegExtension',
        'num':14
    }
    requests.post("http://localhost:8000/info/", json=data)
    st.write(datetime.now())

if st.button("레그컬"):
    data = {
        'name':'LegCurl',
        'num':15
    }
    requests.post("http://localhost:8000/info/", json=data)
    st.write(datetime.now())