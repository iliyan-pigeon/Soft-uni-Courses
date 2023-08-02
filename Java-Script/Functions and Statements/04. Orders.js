function totalPrice(product, amount){
    let singleProductPrice = 0

    switch (product){
        case "coffee":
            singleProductPrice = 1.50
            break
        case "water":
            singleProductPrice = 1.00
            break
        case "coke":
            singleProductPrice = 1.40
            break
        case "snacks":
            singleProductPrice = 2.00
            break            
    }
    let result = (singleProductPrice * amount).toFixed(2)
    
    console.log(result);
}