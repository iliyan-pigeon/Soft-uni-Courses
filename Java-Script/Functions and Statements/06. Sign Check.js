function positiveOrNegative(...numbers){
    let amountPositive = 0
    let amountNegative = 0
    let result = ''

    for (const number in numbers){
        if (numbers[number] > 0){
            amountPositive += 1
        }else if (numbers[number] < 0){
            amountNegative += 1
        }
    }

    if (amountPositive === 0){
        result = "Negative"
    }else if (amountNegative === 0){
        result = "Positive"
    }else if (amountNegative === 2){
        result = "Positive"
    }else if (amountNegative === 1){
        result = "Negative"
    }

    console.log(result);
}