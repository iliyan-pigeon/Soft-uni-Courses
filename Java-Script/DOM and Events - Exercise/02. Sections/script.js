function create(words) {
   let container = document.getElementById("content")
   for (let word of words){
      let divContainer = document.createElement("div")
      let paragraph = document.createElement("p")
      paragraph.textContent = word
      paragraph.style.display = "none"
      divContainer.appendChild(paragraph)
      divContainer.addEventListener("click", () => {
         paragraph.style.display = "block"
      })
      container.appendChild(divContainer)
   }
}