function hoverylogin(){
    const usernameInp=document.getElementById("username");
    const passwordInp=document.getElementById("password");
    const Submit=document.getElementById("button");
    Submit.addEventListener("mouseover",(button)=>{
        let email=usernameInp.value;
        let pass=passwordInp.value;
        if((email== null || email== '') && (pass== null || pass=='')){
            button.target.classList.toggle("move");
        }
        else{
            button.target.classList.toggle("stop");
        }
    })
}
hoverylogin()