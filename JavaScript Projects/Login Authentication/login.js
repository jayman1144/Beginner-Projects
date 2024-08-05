const username = document.getElementById("username");
const password = document.getElementById("password");
const output = document.getElementById("output");
const intro_buttons = document.getElementById("decision")

function log_in(){
    reset_display(0);    

    const Details = {
        username: "jayman1144",
        password: "General Kenobi"
    }

    document.addEventListener("submit",  event =>
        {if(username.value === Details.username && password.value === Details.password){
            event.preventDefault();
            output_display(true,"Error")
        }
        else{
            event.preventDefault();
            output_display(false,"Incorrect details, try again");
            reset_display(5000);

        }}
    )
}

function output_display(result,error){
    if(result){
        username.style.display = "none";
        password.style.display = "none";
        output.textContent = "You successfully logged in";
        output.style.display = "flex";
    }
    else{
        username.style.display = "none";
        password.style.display = "none";
        output.textContent = `${error}`;
        output.style.display = "flex";
    }
}

function reset_display(duration){
    setTimeout(() =>
        {intro_buttons.style.display = "none";
            username.parentElement.style.display = "flex";
            username.style.display = "flex";
            password.style.display = "flex";
            username.value = "";
            password.value = "";
            output.style.display = "none"
            output.textContent = "";},duration)
}

function sign_up(){
    reset_display(0);

    const New_User = {
        username: username.value,
        password: password.value,
        creation_time: new Date(),
    }
    document.addEventListener("submit", event => {
        event.preventDefault();
        output_display(false,"Account successfully created")
    })
    reset_display(5000);

}