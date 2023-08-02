function difference(someArray){
    let evenSum = 0
    let oddSum = 0

    for (i=0; i<=someArray.length-1; i++)
    if (someArray[i] % 2 != 0){
        oddSum += someArray[i]
    }else {
        evenSum += someArray[i]
    }

    let difference_between = evenSum - oddSum

    console.log(difference_between)
}

