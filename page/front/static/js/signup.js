const instance = axios.create();
let idCheck = false

// 아이디 중복확인
function idDuplicationCheck(){
    const id = document.querySelector('#id').value
    const data = {
        id:id
    }
    axios.post("/idcheck", data)
    .then(function (response){
        console.log(response)
        if (response.data == true){
            idCheck = true
            alert("사용할 수 있는 아이디입니다.")
        }else{
            alert("이미 존재하는 아이디입니다.")
            idCheck = false
        }
    })
    .catch(function(error){
        console.log(error)
    })
    
}

// 가입하기 버튼 처리
function signUpBtn(){
    // 회원가입 실패처리 코드 넣어야됨
    const psw = document.querySelector('#password').value
    const pswchk = document.querySelector('#passwordcheck').value
    const pswerr = document.querySelector('.password-error')
    let check = false

    // 아이디 중복 확인


    // 비밀번호 확인
    if (psw==pswchk){
        check = true
        pswerr.classList.add('hidden')

    }else{
        pswerr.classList.remove('hidden')
    }


    if (check && idCheck){
        alert("회원가입 완료!")
    }else{
        alert("아이디 중복 확인을 해주세요")
        return false
    }

}

const idChkBtn = document.querySelector('.id-check')
idChkBtn.addEventListener('click', idDuplicationCheck)