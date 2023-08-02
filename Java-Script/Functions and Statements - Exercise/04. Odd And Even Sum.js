function oddAndEvenSum(number){
    numberArray = String(number).split("")
    let oddSum = 0
    let evenSum = 0

    for (const number in numberArray){
        if (Number(numberArray[number]) % 2 == 0){
            evenSum += Number(numberArray[number])
        }else {
            oddSum += Number(numberArray[number])
        }
    }

    let result = `Odd sum = ${oddSum}, Even sum = ${evenSum}`
    return result
}