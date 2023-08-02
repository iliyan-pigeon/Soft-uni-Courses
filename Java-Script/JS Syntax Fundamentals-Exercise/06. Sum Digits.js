function digitsSum(digits){
    let result = 0
    digits = String(digits).split('')

    for (i=0; i<digits.length; i++){
        result += Number(digits[i])
    }

    console.log(result);
}
