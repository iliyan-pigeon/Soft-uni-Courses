function sumTable() {
    let result = document.getElementById("sum")
    let prices = document.getElementsByTagName("td")
    let sum = 0

    for (let i=0; i<prices.length-1; i++){
        if (i % 2 != 0){
            sum += Number(prices[i].textContent)
        }
    }

    result.textContent = sum
}