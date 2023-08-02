function extractText() {
    let liElements = document.getElementsByTagName("li")
    let textArea = document.getElementsByTagName("textarea")[0]
    
    for (const li of liElements){
        textArea.textContent += li.textContent + "\n"
    }
}