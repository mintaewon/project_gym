// 아이디 중복확인
function idDuplicationCheck(){

    alert("확인")
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