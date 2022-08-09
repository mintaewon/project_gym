import streamlit as st
from datetime import datetime
import requests

st.title('gym')

st.markdown('---------')

date = st.date_input('오늘 날짜')
select_weather = st.radio("오늘 날씨", ("맑음","비","눈"))

def req(name, num, weather=select_weather):
    data = {
        'name':name,
        'num':num,
        'weather':weather
    }
    requests.post("http://host.docker.internal:8000/info/", json=data)
    st.write('Success')
    st.write(datetime.now())

if st.button("프리웨이트존"):
    req('Freeweight',0)

if st.button("스미스머신"):
    req('SmithMachine',1)

if st.button("파워레그프레스"):
    req('PowerLegPress',2)

if st.button("파워랙"):
    req('PowerRack',3)

if st.button("인클라인벤치"):
    req('InclineBench',4)

if st.button("플랫벤치"):
    req('FlatBench',5)

if st.button("숄더프레스머신"):
    req('ShoulderPressMachine',6)

if st.button("케이블"):
    req('Cable',7)

if st.button("랫풀다운"):
    req('LatPulldown',8)

if st.button("체스트플라이 머신"):
    req('ChestFlyMachine',9)

if st.button("체스트프레스 머신"):
    req('ChestPressMachine',10)

if st.button("시티드로우머신"):
    req('SeatedRowMachine',11)

if st.button("레그프레스머신"):
    req('LegPressMachine',12)

if st.button("이너타이머신"):
    req('InnerThighMachine',13)

if st.button("레그 익스텐션"):
    req('LegExtension',14)

if st.button("레그컬"):
    req('LegCurl',15)