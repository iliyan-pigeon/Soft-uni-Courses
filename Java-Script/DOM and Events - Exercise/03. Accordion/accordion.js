function toggle() {
    let extraParagraph = document.getElementById("extra")
    let button = document.getElementsByClassName("button")[0]

    if (extraParagraph.style.display === "none"){
        extraParagraph.style.display = "block"
        button.textContent = "Less"
    }else{
        extraParagraph.style.display = "none"
        button.textContent = "More"
    }
}