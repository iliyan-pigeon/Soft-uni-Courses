function numberRangeManipulator(firstNumber, secondNumber){
    let numbers = []
    let combinedAmount = 0
    let result = ""

    for (i=firstNumber; i<=secondNumber; i++){
        numbers.push(i)
        combinedAmount += i
    }
    
    result += numbers.join(" ") + "\n" + `Sum: ${combinedAmount}`

    console.log(result);
}

