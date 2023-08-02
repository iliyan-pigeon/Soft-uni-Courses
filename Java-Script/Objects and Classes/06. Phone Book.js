function phoneNumberStorage(data){
    dataObject = {}

    for (const person of data){
        let personInfo = person.split(" ")
        dataObject[personInfo[0]] = personInfo[1]
    }

    for (const [key, value] of Object.entries(dataObject)){
        console.log(`${key} -> ${value}`);
    }
}