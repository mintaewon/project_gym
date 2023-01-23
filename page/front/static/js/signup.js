const instance = axios.create();

// 아이디 중복확인
function idDuplicationCheck(){
    const id = document.querySelector('#id').value
    const data = {
        id:id
    }
    axios.post("/idcheck", data)
    .then(function (response){
        console.log(response)
        alert("성공")
    })
    .catch(function(error){
        console.log(error)
        alert("실패")
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


    if (check){
        alert("회원가입 완료!")
    }else{
        return false
    }

}

const idChkBtn = document.querySelector('.id-check')
idChkBtn.addEventListener('click', idDuplicationCheck)