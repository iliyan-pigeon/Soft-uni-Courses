function filterElements(someArray, step){
    let filteredElements = []

    for (i=0; i<someArray.length; i += step){
        filteredElements.push(someArray[i])
    }

    return filteredElements
}