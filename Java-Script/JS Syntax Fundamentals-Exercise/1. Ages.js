function ageCategory(age){
    let category

    if (age >= 0 && age <= 2){
        category = "baby"
    }else if (age >= 3 && age <= 13){
        category = "child"
    }else if (age >= 14 && age <= 19){
        category = "teenager"
    }else if (age >= 20 && age <= 65){
        category = "adult"
    }else if (age >= 66){
        category = "elder"
    }else {
        category = "out of bounds"
    }

    console.log(category);
}