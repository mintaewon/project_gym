const instance = axios.create();
const id = document.querySelector("#user-id");
const passwd = document.querySelector("#password");

const signInBtn = document.querySelector("#sign-in");
const signUpBtn = document.querySelector("#sign-up");

function onSignInBtnClick(){
    // event.preventDefault();
    console.log(id.value);
    console.log(passwd.value);
    localStorage.setItem(id.value, passwd.value);
    axios.get("/");
}

// signInBtn.addEventListener("click", onSignInBtnClick)