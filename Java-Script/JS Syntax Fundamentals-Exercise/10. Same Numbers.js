function sumAndScan(digits){
    digits = String(digits).split("")
    let firstDigit = digits[0]
    let areSame = true
    let combinedAmount = 0

    for (let digit in digits){
        if (digits[digit] != firstDigit){
            areSame = false
        }
        combinedAmount += Number(digits[digit])
    }

    console.log(areSame);
    console.log(combinedAmount);
}