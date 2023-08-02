function circleArea(input){
    let type = typeof(input)
    let result = ""

    if (type == "number"){
        result = (input * input * Math.PI).toFixed(2)
    }else{
        result = `We can not calculate the circle area, because we receive a ${type}.`
    }

    console.log(result)
}