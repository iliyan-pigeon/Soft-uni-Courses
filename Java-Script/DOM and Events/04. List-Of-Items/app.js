function addItem() {
    let unorderedList = document.getElementById("items")
    let liElement = document.createElement("li")
    let input = document.getElementById("newItemText")
    liElement.textContent = input.value
    unorderedList.appendChild(liElement)
}