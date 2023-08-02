function groceriesListOrderer(data){
    let orderedList = data.shift().split("!")
    
    for (let item of data){
        let command = item.split(" ")[0]

        if (command === "Urgent"){
            let product = item.split(" ")[1]
            if (!orderedList.includes(product)){
                orderedList.push(product)
            }
        }else if (command === "Unnecessary"){
            let product = item.split(" ")[1]
            if (orderedList.includes(product)){
                orderedList.splice(orderedList.indexOf(product), 1)
            }
        }else if (command === "Correct"){
            item = item.split(" ")
            let oldItem = item[1]
            let newItem = item[2]
            if (orderedList.includes(oldItem)){
                orderedList.splice(orderedList.indexOf(oldItem), 1, newItem)
            }
        }else if (command === "Rearrange"){
            let product = item.split(" ")[1]
            if (orderedList.includes(product)){
                orderedList.splice(product)
                orderedList.push(product)
            }
        }
    }

    console.log(orderedList.join(", "));
}

groceriesListOrderer((["Milk!Pepper!Salt!Water!Banana",
"Urgent Salt",
"Unnecessary Grapes",
"Correct Pepper Onion",
"Rearrange Grapes",
"Correct Tomatoes Potatoes",
"Go Shopping!"]));