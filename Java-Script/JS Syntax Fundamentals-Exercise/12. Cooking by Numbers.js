function mathOperations(number, opFirst, opSecond, opThird, opFourth, opFifth){
    let theNumber = Number(number)
    let operators = [opFirst, opSecond, opThird, opFourth, opFifth]
    
    for (let operator in operators){
        if (operators[operator] == "chop"){
            theNumber /= 2
        }else if (operators[operator] == "dice"){
            theNumber = Math.sqrt(theNumber)
        }else if (operators[operator] == "spice"){
            theNumber += 1
        }else if (operators[operator] == "bake"){
            theNumber *= 3
        }else if (operators[operator] == "fillet"){
            theNumber -= (theNumber * 0.2)
        }

        console.log(theNumber);
    }
}
