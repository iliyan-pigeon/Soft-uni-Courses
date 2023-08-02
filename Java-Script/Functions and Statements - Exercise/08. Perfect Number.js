function isPerfectNumber(number){
    let divisorsSum = 0

    for (i=1; i<number; i++){
        if(number % i === 0){
            divisorsSum += i  
        }
    }

    if (divisorsSum === number){
        return "We have a perfect number!"
    }else {
        return "It's not so perfect."
    }
}