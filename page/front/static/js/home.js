// 기구 별 element 만들기
class MakeGymMachine extends HTMLElement {
    connectedCallback() {
        let machineBox = document.createElement('div');
        machineBox.classList.add("machine-box")
        this.appendChild(machineBox);
        
        let machineName = document.createElement('span')
        machineName.innerText = this.getAttribute('name');
        machineName.style.fontSize="23px"
        machineBox.appendChild(machineName)

        let minusButton = document.createElement('button');
        minusButton.innerText = '-';
        minusButton.classList.add("control-button")
        machineBox.appendChild(minusButton);

        let cnt = document.createElement('span');
        cnt.innerText = 0;
        cnt.classList.add("user-count")
        machineBox.appendChild(cnt);

        let plusButton = document.createElement('button');
        plusButton.innerText = '+';
        plusButton.classList.add("control-button")
        machineBox.appendChild(plusButton);

        function plusClick() {
            cnt.innerText = parseInt(cnt.innerText) + 1;
        }
        function minusClick() {
            cnt.innerText = parseInt(cnt.innerText) - 1;
            if (cnt.innerText < 0) {
                cnt.innerText = 0;
            }
        }
        plusButton.addEventListener("click", plusClick);
        minusButton.addEventListener("click", minusClick);
    }
}
customElements.define('make-machine', MakeGymMachine)



// 날씨 데이터 가져오기
function getWeather() {
    const weather = document.querySelector('input[name="weather"]:checked').value;
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
