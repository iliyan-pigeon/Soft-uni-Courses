function arrayRotator(someArray, rotationsNumber){
    for (i=0; i<rotationsNumber; i++){
        element = someArray.shift()
        someArray.push(element)
    }

    result = someArray.join(" ")
    console.log(result);
}