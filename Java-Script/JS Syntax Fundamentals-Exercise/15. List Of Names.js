function fruitSorter(someArray){
    let orderedFruits = someArray.sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()))
    let counter = 1

    for (let fruit in orderedFruits){
        result = `${counter}.${orderedFruits[fruit]}`;
        counter += 1
        console.log(result);
    }
}