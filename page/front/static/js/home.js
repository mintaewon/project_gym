// 기구 별 element 만들기
class MakeGymMachine extends HTMLElement {
    connectedCallback() {
        let MachineName = document.createElement('div');
        MachineName.innerText = this.getAttribute('name');
        MachineName.id = "kindOfMachine"
        this.appendChild(MachineName);

        let MinusButton = document.createElement('button');
        MinusButton.innerText = '-';
        MinusButton.classList.add("controlbutton")
        this.appendChild(MinusButton);
        let Cnt = document.createElement('span');
        Cnt.innerText = 0;
        Cnt.classList.add("userCount")
        this.appendChild(Cnt);
        let PlusButton = document.createElement('button');
        PlusButton.innerText = '+';
        PlusButton.classList.add("controlbutton")
        this.appendChild(PlusButton);


        function plusClick() {
            Cnt.innerText = parseInt(Cnt.innerText) + 1;
        }
        function minusClick() {
            Cnt.innerText = parseInt(Cnt.innerText) - 1;
            if (Cnt.innerText < 0) {
                Cnt.innerText = 0;
            }
        }


        PlusButton.addEventListener("click", plusClick);
        MinusButton.addEventListener("click", minusClick);
    }
}
customElements.define('make-machine', MakeGymMachine)



// 날씨 데이터 가져오기
function getWeather() {
    const weather = document.querySelector('input[name="Weather"]:checked').value;
    return weather;
}

// 사용인원 데이터 가져오기
function getUseMachines() {
    let usingList = [];
    findCnt = document.querySelectorAll("make-machine .userCount");
    findCnt.forEach(element => { usingList.push(Number(element.innerText)) });
    return usingList;
}
// DB에서 데이터 다운로드
function dataDownEvent() {
    axios({
        url: "/down",
        method: "get",
        responseType: "blob" // 응답 데이터 타입 정의
    })
        .then(function (response) {
            console.log("다운로드 성공");
            const blob = new Blob([response.data]);

            const fileObjectUrl = window.URL.createObjectURL(blob);

            const link = document.createElement("a");
            link.href = fileObjectUrl;
            link.style.display = "none";

            link.download = "gymdata.csv";

            document.body.appendChild(link);
            link.click();
            link.remove();

            window.URL.revokeObjectURL(fileObjectUrl);
        })
        .catch(function (error) {
            console.log("다운 실패");
        })
}

// 백엔드로 데이터 전송
function postClickEvent(getUseMachines, getWeather) {
    const data_ls = {
        weather: getWeather(),
        use: getUseMachines()
    };

    axios.post("/info", data_ls)
        .then(function (response) {
            console.log("성공");
            const date = response.data.date;
            alert(date + " 수집 완료");
        })
        .catch(function (error) {
            console.log("실패");
            console.log(error);
        });
}
