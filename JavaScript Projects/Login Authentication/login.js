const username = document.getElementById("username");
const password = document.getElementById("password");
const output = document.getElementById("output");

const Details = {
    username: "jayman1144",
    password: "General Kenobi"
}

function output_display(result){
    if(result){
        username.style.display = "none";
        password.style.display = "none";
        output.textContent = "You successfully logged in";
        output.style.display = "flex";
    }
    else{
        username.style.display = "none";
        password.style.display = "none";
        output.textContent = "Incorrect details, try again";
        output.style.display = "flex";
    }
}

function reset_display(){
    setTimeout(() =>
        {username.style.display = "flex";
            password.style.display = "flex";
            username.value = "";
            password.value = "";
            output.style.display = "none"
            output.textContent = "";},5000)
}

document.addEventListener("submit",  async event =>
    {if(username.value === Details.username && password.value === Details.password){
        event.preventDefault();
        output_display(true)
    }
    else{
        event.preventDefault();
        output_display();
        reset_display();

    }}
)