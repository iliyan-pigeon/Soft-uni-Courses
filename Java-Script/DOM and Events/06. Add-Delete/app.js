function addItem() {
    let unorderedList = document.getElementById("items")
    let liElement = document.createElement("li")
    let input = document.getElementById("newItemText")
    let anchorElement = document.createElement("a")
    anchorElement.textContent = "[Delete]"
    anchorElement.href = "#"
    anchorElement.addEventListener("click", deleteHandler)
    liElement.textContent = input.value
    liElement.appendChild(anchorElement)
    unorderedList.appendChild(liElement)

    function deleteHandler(e){
        let anchor = e.currentTarget
        anchor.parentElement.remove()
    }
}