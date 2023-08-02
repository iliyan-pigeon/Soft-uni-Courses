function piecesHandler(data){
    let piecesNumber = data.shift()
    let pieces = {}

    for (let i=0; i<piecesNumber; i++){
        let piece = data[i].split("|")
        pieces[piece[0]] = piece
    }

    data.splice(0, piecesNumber)

    for (let command of data){
        command = command.split("|")
        let theCommand = command[0]
        
        if (theCommand === "Add"){
            let name = command[1]
            let composer = command[2]
            let key = command[3]

            if (Object.keys(pieces).includes(name)){
                console.log(`${name} is already in the collection!`);
            }else{
                pieces[name] = [name, composer, key]
                console.log(`${name} by ${composer} in ${key} added to the collection!`);
            }
        }else if (theCommand === "Remove"){
            let name = command[1]

            if (Object.keys(pieces).includes(name)){
                Reflect.deleteProperty(pieces, name);
                console.log(`Successfully removed ${name}!`);
            }else{
                console.log(`Invalid operation! ${name} does not exist in the collection.`);
            }
        }else if (theCommand === "ChangeKey"){
            let name = command[1]
            let key = command[2]

            if (Object.keys(pieces).includes(name)){
                pieces[name][pieces[name].length -1] = key
                console.log(`Changed the key of ${name} to ${key}!`);
            }else{
                console.log(`Invalid operation! ${name} does not exist in the collection.`);
            }
        }else{
            for (let piece in pieces){
                let [name, composer, key] = pieces[piece]
                console.log(`${name} -> Composer: ${composer}, Key: ${key}`);
            }
        }
    }
}


piecesHandler(["4",
"Eine kleine Nachtmusik|Mozart|G Major",
"La Campanella|Liszt|G# Minor",
"The Marriage of Figaro|Mozart|G Major",
"Hungarian Dance No.5|Brahms|G Minor",
"Add|Spring|Vivaldi|E Major",
"Remove|The Marriage of Figaro",
"Remove|Turkish March",
"ChangeKey|Spring|C Major",
"Add|Nocturne|Chopin|C# Minor",
"Stop"  
])