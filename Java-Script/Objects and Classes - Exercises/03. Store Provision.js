function storeProvision(stoke, ordered){
    let storage = {}

    for (i=0; i<stoke.length; i+=2){
        storage[stoke[i]] = Number(stoke[i+1])
    }

    for (i=0; i<ordered.length; i+=2){
        if (ordered[i] in storage){
            storage[ordered[i]] += Number(ordered[i+1])
        }else{
            storage[ordered[i]] = Number(ordered[i+1])
        } 
    }

    for (const [product, amount] of Object.entries(storage)){
        console.log(`${product} -> ${amount}`);
    }
}