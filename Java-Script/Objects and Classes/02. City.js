function objectDistructor(someObject){
    let tuples = Object.entries(someObject)

    for (const [key, value] of tuples){
        console.log(`${key} -> ${value}`)
    }
}