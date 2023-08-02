window.addEventListener("load", solve);

function solve() {
  let titleInput = document.getElementById("task-title")
  let categoryInput = document.getElementById("task-category")
  let contentTextarea = document.getElementById("task-content")

  let publishBtn = document.getElementById("publish-btn")

  let reviewList = document.getElementById("review-list")
  let publishedList = document.getElementById("published-list")

  publishBtn.addEventListener("click", publishHandler)

  function publishHandler(){
    let title = titleInput.value
    let category = categoryInput.value
    let content = contentTextarea.value

    let li = elementCreator("li", null, reviewList, null, ["rpost"])
    let article = elementCreator("article", null, li)
    let h4 = elementCreator("h4", title, article)
    let categoryP = elementCreator("p", `Category: ${category}`, article)
    let contentP = elementCreator("p", `Content: ${content}`, article)
    let editBtn = elementCreator("button", "Edit", li, null, ["action-btn", "edit"])
    let postBtn = elementCreator("button", "Post", li, null, ["action-btn", "post"])

    editBtn.addEventListener("click", () => {
        titleInput.value = title
        categoryInput.value = category
        contentTextarea.value = content

        reviewList.innerHTML = ""
    })

    postBtn.addEventListener("click", () => {
       let parent = postBtn.parentElement
       reviewList.removeChild(parent)

       let li = elementCreator("li", null, publishedList, null, ["rpost"])
       let article = elementCreator("article", null, li)
       let h4 = elementCreator("h4", title, article)
       let categoryP = elementCreator("p", `Category: ${category}`, article)
       let contentP = elementCreator("p", `Content: ${content}`, article)
       
    })

    titleInput.value = ""
    categoryInput.value = ""
    contentTextarea.value = ""
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