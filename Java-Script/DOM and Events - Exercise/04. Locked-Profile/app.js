function lockedProfile() {
    let allButtons = document.getElementsByTagName("button")

    for (let button of allButtons){
        button.addEventListener("click", clickHandler)
    }

    function clickHandler(event){
        let currentButton = this
        let currentProfile = currentButton.parentElement
        let hiddenInformation = currentProfile.children[9]
        let unlockElement = currentProfile.children[4]

        if (unlockElement.checked){
            if (currentButton.textContent === "Show more"){
                currentButton.textContent = "Hide it"
                hiddenInformation.style.display = "block"
            }else{
                currentButton.textContent = "Show more"
                hiddenInformation.style.display = "none"
            }
        }
    }
}