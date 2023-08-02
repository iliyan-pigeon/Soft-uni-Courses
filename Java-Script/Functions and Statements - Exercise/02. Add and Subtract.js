function sumAndSubtract(firstNumber, secondNumber, thirdNumber){
    function sum(numberOne, numberTwo){
        let result = numberOne + numberTwo
        return result
    }

    function subtract(firstNum, secondNum){
        let result = firstNum - secondNum
        return result
    }

    let sumResult = sum(firstNumber, secondNumber)
    let result = subtract(sumResult, thirdNumber)
    console.log(result);
}

sumAndSubtract(23, 6, 10)
