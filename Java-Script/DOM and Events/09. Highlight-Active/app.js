function focused() {
    let allInputs = Array.from(document.querySelectorAll('[type=text]'))
    
    for(let line of allInputs){
        line.addEventListener("focus", handleFocus)
        line.addEventListener("blur", handleBlur)
    }

    function handleFocus(event){
        let currentInput = event.target
        let parentElement = currentInput.parentElement
        parentElement.classList.add("focused")
    }

    function handleBlur(event){
        let currentInput = event.target
        let parentElement = currentInput.parentElement
        parentElement.classList.remove("focused")
    }

}