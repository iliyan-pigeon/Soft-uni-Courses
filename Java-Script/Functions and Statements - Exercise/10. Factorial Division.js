function factorialDivision(firstNumber, secondNumber){
    function factorial(number){
        if (number < 0){
            return "Error!"
        }else if (number === 0 || number === 1){
            return 1
        }else{
            return number * factorial(number-1)
        }
        }

    let firstNumberFactorial = factorial(firstNumber)
    let secondNumberFactorial = factorial(secondNumber)
    let result = (firstNumberFactorial / secondNumberFactorial).toFixed(2)

    return result
}

