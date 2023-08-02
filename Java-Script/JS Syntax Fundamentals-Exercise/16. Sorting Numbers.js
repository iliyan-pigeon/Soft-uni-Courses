function sortingNumbers(someArray){
    let arrayCopy = [...someArray]
    arryCopy = arrayCopy.sort((a, b)=>a-b)
    result = []
    counter = 1

    for (i=counter; i<=someArray.length; i++){
        if (i % 2 != 0){
            result.push(arrayCopy.shift())
        }else{
            result.push(arrayCopy.pop())    
        }
    }

    return result
}

