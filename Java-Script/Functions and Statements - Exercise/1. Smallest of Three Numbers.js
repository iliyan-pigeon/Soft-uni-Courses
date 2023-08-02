function pickSmallestNumber(...numbers){
    let smallestNumber = Number.MAX_VALUE

    for (const number in numbers){
        if (numbers[number] < smallestNumber){
            smallestNumber = numbers[number]
        }
    }

    return smallestNumber
}