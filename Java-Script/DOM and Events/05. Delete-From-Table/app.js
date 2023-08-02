function deleteByEmail() {
    let result = document.getElementById("result")
    let email = document.querySelector('input[type="text"]')
    let allEmails = Array.from(document.querySelectorAll("td:nth-child(even)"))
    let foundElement = allEmails.find((a) => a.textContent === email.value)
    if (foundElement){
        foundElement.parentElement.remove()
        result.textContent = "Deleted."
    }else{
        result.textContent = "Not found."
    }
}