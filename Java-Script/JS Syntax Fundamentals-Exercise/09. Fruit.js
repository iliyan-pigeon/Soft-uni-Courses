function priceCalculator(fruitType, weightGrams, pricePerKilo){
    let weightKilo = weightGrams / 1000
    let totalPrice = weightKilo * pricePerKilo
    let result = `I need $${totalPrice.toFixed(2)} to buy ${weightKilo.toFixed(2)} kilograms ${fruitType}.`

    console.log(result);     

}