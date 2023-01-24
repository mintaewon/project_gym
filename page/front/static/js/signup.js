const instance = axios.create();
let emailCheck = false
let userEmail = ""

// 아이디 중복확인
function idDuplicationCheck(){
    const email = document.querySelector('#email').value
    const data = {
        email:email
    }
    axios.post("/emailcheck", data)
    .then(function (response){
        console.log(response)
        if (response.data == true){
            emailCheck = true
            userEmail = email
            alert("사용할 수 있는 아이디입니다.")
        }else{
            alert("이미 존재하는 아이디입니다.")
            emailCheck = false
            userEmail = ""
        }
    })
    .catch(function(error){
        console.log(error)
    })
    
}

// 가입하기 버튼
function signUpBtn(){
    const psw = document.querySelector('#password').value
    const pswchk = document.querySelector('#passwordcheck').value
    const pswerr = document.querySelector('.password-error')
    let check = false
    const idValue = document.querySelector('#email').value
    // 아이디 중복 확인
    if (userEmail!=idValue){
        emailCheck=false
    }

    // 비밀번호 확인
    if (psw==pswchk){
        check = true
        pswerr.classList.add('hidden')

    }else{
        pswerr.classList.remove('hidden')
    }


    if (check && emailCheck){
        alert("회원가입 완료!")
    }else if(!emailCheck){
        alert("아이디 중복 확인을 해주세요")
        return false
    }else{
        alert("비밀번호를 확인해주세요")
        return false
    }

}

const idChkBtn = document.querySelector('.email-check')
idChkBtn.addEventListener('click', idDuplicationCheck)