function addressStorage(data){
    let storedAddresses = {}

    for (const address of data){
        let info = address.split(":")
        let personName = info[0]
        let theAddress = info[1]

        storedAddresses[personName] = theAddress
    }

    let entries = Object.entries(storedAddresses)
    let sortedByName = entries.sort((firstPerson, secondPerson) =>{
        let firstName = firstPerson[0]
        let secondName = secondPerson[0]
        return firstName.localeCompare(secondName)
    })

    for (const [name, info] of sortedByName){
        console.log(`${name} -> ${info}`);
    }
}

addressStorage(['Tim:Doe Crossing','Bill:Nelson Place','Peter:Carlyle Ave','Bill:Ornery Rd'])