function reversedArray(n, someArray){
    let reversedArray = []

    for (i=0; i<n; i++){
        reversedArray.push(someArray[i])
    }

    reversedArray = reversedArray.reverse()

    console.log(reversedArray.join(" "))
}

