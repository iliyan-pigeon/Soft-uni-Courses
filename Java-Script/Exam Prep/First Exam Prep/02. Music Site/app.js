window.addEventListener('load', solve)

function solve() {
    let genreInput = document.getElementById("genre")
    let nameInput = document.getElementById("name")
    let authorInput = document.getElementById("author")
    let dateInput = document.getElementById("date")
    let addBtn = document.getElementById("add-btn")

    let allHitsDiv = document.getElementsByClassName("all-hits-container")[0]
    let savedDiv = document.getElementsByClassName("saved-container")[0]

    let totalLikes = 0
    let totalLikesParagraph = document.getElementsByClassName("likes")[0].children[0]


    addBtn.addEventListener("click", addHitsHandler)

    function addHitsHandler(event){
        event.preventDefault()
        if (genreInput.value !== "" && nameInput.value !== "" && authorInput.value !== "" &&
        dateInput.value !== ""){
          let hitsInfoDiv = elementCreator("div", null, allHitsDiv, null, ["hits-info"])
          let img = elementCreator("img", null, hitsInfoDiv, null, null, {src:"./static/img/img.png"})
          let genreH2 = elementCreator("h2", `Genre: ${genreInput.value}`, hitsInfoDiv)
          let nameH2 = elementCreator("h2", `Name: ${nameInput.value}`, hitsInfoDiv)
          let authorH2 = elementCreator("h2", `Author: ${authorInput.value}`, hitsInfoDiv)
          let dateH3 = elementCreator("h3", `Date: ${dateInput.value}`, hitsInfoDiv)
          let saveSongBtn = elementCreator("button", "Save song", hitsInfoDiv, null, ["save-btn"])
          let likeSongBtn = elementCreator("button", "Like song", hitsInfoDiv, null, ["like-btn"])
          let deleteBtn = elementCreator("button", "Delete", hitsInfoDiv, null, ["delete-btn"])
  
          genreInput.value = ""
          nameInput.value = ""
          authorInput.value = ""
          dateInput.value = ""
  
          likeSongBtn.addEventListener("click", addLikesHandler)
          saveSongBtn.addEventListener("click", saveSongHandler)
          deleteBtn.addEventListener("click", deleteHandler)
  
          function addLikesHandler(){
              totalLikes += 1
              totalLikesParagraph.textContent = `Total Likes: ${totalLikes}`
              likeSongBtn.setAttribute("disabled", true)
            }
  
          function saveSongHandler(){
              document.querySelector(".save-btn").remove()
              document.querySelector(".like-btn").remove()
              savedDiv.appendChild(hitsInfoDiv)

              
          }  

          function deleteHandler(){
            this.parentElement.remove()
          }
        }
    }


    function elementCreator(type, content, parentElement, id, classes, attributes){
      let element = document.createElement(type)
      
      if (content && type === "input" || content && type === "textarea"){
        element.value = content
      }
    
      if (content && type != "input" && type != "textarea"){
        element.textContent = content
      }
    
      if (id){
        element.id = id
      }
    
      if (classes){
        element.classList.add(...classes)
      }
    
      if (attributes){
        for (let attribute in attributes){
          element.setAttribute(attribute, attributes[attribute])
        }
      }
    
      if (parentElement){
        parentElement.appendChild(element)
      }
    
      return element
    }

}



  