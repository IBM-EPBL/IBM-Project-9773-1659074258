function hoverylogin(){
    const usernameInp=document.getElementById("username");
    const emailInp=document.getElementById("email");
    const passwordInp=document.getElementById("password");
    const Submit=document.getElementById("button");
    Submit.addEventListener("mouseover",(button)=>{
        let name=usernameInp.value;
        let pass=passwordInp.value;
        let email=emailInp.value;
        if((name== null || name== '') && (pass== null || pass=='') && (email== null || email =='')) {
            button.target.classList.toggle("move");
        }
        else{
            button.target.classList.toggle("stop");
        }
    })
}
hoverylogin()