const id = document.querySelector("#userId");
const passwd = document.querySelector("#password");

const signInBtn = document.querySelector("#signIn");
const signUpBtn = document.querySelector("#signUp");

function onSignInBtnClick(event){
    event.preventDefault()
    console.log(id.value);
    console.log(passwd.value);
}

signInBtn.addEventListener("click", onSignInBtnClick)