function solve() {
  let rawTextInput = document.getElementById("input")
  let separatedTextInput = rawTextInput.value.split(".")
  let formattedOutput = document.getElementById("output")
  separatedTextInput.pop()
  
  while (separatedTextInput.length > 0){
    let paragraph = document.createElement("p")
    let paragraphContent = separatedTextInput.splice(0, 3)
    paragraph.textContent = paragraphContent.join(".") + "."
    formattedOutput.appendChild(paragraph)
  }
}