window.addEventListener("load", solve);

function solve() {
  let firstNameInput = document.getElementById("first-name")
  let lastNameInput = document.getElementById("last-name")
  let ageInput = document.getElementById("age")
  let storyTitleInput = document.getElementById("story-title")
  let genreInput = document.getElementById("genre")
  let storyTextarea = document.getElementById("story")

  let publishInputBtn = document.getElementById("form-btn")
  publishInputBtn.addEventListener("click", publishHandler)

  let previewList = document.getElementById("preview-list")
  let mainDiv = document.getElementById("main")

  function publishHandler(){
    if (firstNameInput.value !== "" && lastNameInput.value !== "" &&
    ageInput.value !== "" && storyTitleInput.value !== "" && genreInput.value !== "" &&
    storyTextarea.value !== ""){
      let firstName = firstNameInput.value
      let lastName = lastNameInput.value
      let age = ageInput.value
      let title = storyTitleInput.value
      let genre = genreInput.value
      let content = storyTextarea.value

      let li = elementCreator("li", null, previewList, null, ["story-info"])
      let article = elementCreator("article", null, li)
      let h4 = elementCreator("h4", `Name: ${firstName} ${lastName}`, article)
      let ageParagraph = elementCreator("p", `Age: ${age}`, article)
      let titleParagraph = elementCreator("p", `Title: ${title}`, article)
      let genreParagraph = elementCreator("p", `Genre: ${genre}`, article)
      let contentParagraph = elementCreator("p", content, article)

      let saveStoryBtn = elementCreator("button", "Save Story", li, null, ["save-btn"])
      let EditStoryBtn = elementCreator("button", "Edit Story", li, null, ["edit-btn"])
      let deleteStoryBtn = elementCreator("button", "Delete Story", li, null, ["delete-btn"])
      
      publishInputBtn.setAttribute("disabled", true)
      firstNameInput.value = ""
      lastNameInput.value = ""
      ageInput.value = ""
      storyTitleInput.value = ""
      genreInput.value = ""
      storyTextarea.value = ""

      EditStoryBtn.addEventListener("click", () => {
        firstNameInput.value = firstName
        lastNameInput.value = lastName
        ageInput.value = age
        storyTitleInput.value = title
        genreInput.value = genre
        storyTextarea.value = content

        publishInputBtn.disabled = false

        previewList.innerHTML = "<h3>Preview</h3>"
      })

      saveStoryBtn.addEventListener("click", () => {
        mainDiv.innerHTML = "<h1>Your scary story is saved!</h1>"
      })

      deleteStoryBtn.addEventListener("click", () => {
        publishInputBtn.disabled = false
        previewList.innerHTML = "<h3>Preview</h3>"
      })
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
