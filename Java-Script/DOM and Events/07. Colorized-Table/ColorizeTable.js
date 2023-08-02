function colorize() {
    let evenElements = Array.from(document.querySelectorAll("tr:nth-child(even)"))
    for (let element of evenElements){
        element.style.backgroundColor = "Teal"
    }
}