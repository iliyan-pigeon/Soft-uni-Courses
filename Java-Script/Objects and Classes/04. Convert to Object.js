function jsonToObject(jsonString){
    let info = JSON.parse(jsonString)
    
    for (const [key, value] of Object.entries(info)){
        console.log(`${key}: ${value}`)
    }
}

jsonToObject('{"name": "George", "age": 40, "town": "Sofia"}')