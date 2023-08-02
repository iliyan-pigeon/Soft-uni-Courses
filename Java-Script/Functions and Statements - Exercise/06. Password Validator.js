function passwordValidator(password){
    let validPassword = true

    if (password.length < 6 || password.length > 10){
        console.log("Password must be between 6 and 10 characters");
        validPassword = false;
    }
    if (/^[A-Za-z0-9]*$/.test(password) == false){
        console.log("Password must consist only of letters and digits")
        validPassword = false
    }

    let digitsAmount = 0
    for (const ch in password){
        if (/^[0-9]*$/.test(password[ch]) == true){
            digitsAmount += 1
        }
    }
    if (digitsAmount < 2){
        console.log("Password must have at least 2 digits")
        validPassword = false
    }

    if (validPassword){
        console.log("Password is valid")
    }
}