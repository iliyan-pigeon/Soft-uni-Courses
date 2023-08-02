function solve(firstNumber, secondNumber, thirdNumber){
    let largestNumber = -Number.MAX_VALUE
    if (firstNumber > largestNumber){
        largestNumber = firstNumber
    }if (secondNumber > largestNumber){
        largestNumber = secondNumber
    }if (thirdNumber > largestNumber){
        largestNumber = thirdNumber
    }
    result = `The largest number is ${largestNumber}.`
    console.log(result)
}