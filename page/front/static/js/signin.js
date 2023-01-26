const instance = axios.create();
const id = document.querySelector("#user-id");
const passwd = document.querySelector("#password");

const signInBtn = document.querySelector("#sign-in");
const signUpBtn = document.querySelector("#sign-up");

function onSignInBtnClick(event){
    // event.preventDefault();
    console.log(id.value);
    console.log(passwd.value);
    localStorage.setItem(id.value, passwd.value);
    // axios.post("/home", "min")
    // .then(function (response){
    //     console.log(response);
    // })
}



function testClick(){
    const ls = "abc";
    axios.post("/test", ls)
    .then(function (response){
        console.log(response);
        console.log('성공');
    })
    .catch(function (error){
        console.log(error);
        console.log('실패');
    })
}