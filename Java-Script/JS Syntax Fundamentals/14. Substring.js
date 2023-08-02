function solve(someString, startIndex, length){
    let result = ''
    for (i=startIndex; i<length+startIndex; i++){
        result += someString[i]
    }

    console.log(result);
}

