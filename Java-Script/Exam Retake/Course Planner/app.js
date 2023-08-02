let baseURL = "http://localhost:3030/jsonstore/tasks"

let nameInput = document.getElementById("course-name")
let typeInput = document.getElementById("course-type")
let descriptionTextarea = document.getElementById("description")
let teacherNameInput = document.getElementById("teacher-name")


let addBtn = document.getElementById("add-course")
let editBtn = document.getElementById("edit-course")

let loadCourseBtn = document.getElementById("load-course")
let listDiv = document.getElementById("list")
let ids = {}
let id = null

loadCourseBtn.addEventListener("click", loadHandler)

function loadHandler(){
    ids = {}
    listDiv.innerHTML = ""

    fetch(baseURL)
      .then((response) => response.json())
      .then((data) => {
        for (let i in data){
            let {title, type, description, teacher, _id} = data[i]
            ids[title] = _id
            let containerDiv = elementCreator("div", null, listDiv, null, ["container"])
            let titleH2 = elementCreator("h2", title, containerDiv)
            let teacherH3 = elementCreator("h3", teacher, containerDiv)
            let typeH3 = elementCreator("h3", type, containerDiv)
            let descriptionH4 = elementCreator("h4", description, containerDiv)
            let editBtn2 = elementCreator("button", "Edit Course", containerDiv, null, ["edit-btn"])
            let finishBtn = elementCreator("button", "Finish Course", containerDiv, null, ["finish-btn"])

            editBtn2.addEventListener("click", () => {
                let parent = editBtn2.parentElement
                let children = parent.children
                id = children[0].textContent

                nameInput.value = children[0].textContent
                typeInput.value = children[2].textContent
                descriptionTextarea.value = children[3].textContent
                teacherNameInput.value = children[1].textContent

                listDiv.removeChild(parent)

                editBtn.disabled = false
                addBtn.disabled = true
            })

            finishBtn.addEventListener("click", () => {
                let parent = finishBtn.parentElement
                let children = parent.children
                id = children[0].textContent

                fetch(`${baseURL}/${ids[id]}`, {
                    method: "DELETE"
                })
                  .then(loadHandler)
                  .catch(() =>{
                    console.log("error");
                  })
            })
        }
      })
}

addBtn.addEventListener("click", addHandler)
editBtn.addEventListener("click", editHandler)

function addHandler(event){
    event.preventDefault()

    let title = nameInput.value
    let type = typeInput.value
    let description = descriptionTextarea.value
    let teacherName = teacherNameInput.value

        let data = {
            title: title,
            type: type,
            description: description,
            teacher: teacherName
        }
    
        fetch(baseURL, {
            method: "POST",
            body: JSON.stringify(data)
        })
          .then(loadHandler)
          .catch(() =>{
            console.log("error");
          })

        nameInput.value = ""
        typeInput.value = ""
        descriptionTextarea.value = ""  
        teacherNameInput.value = ""
    }


function editHandler(event){
    event.preventDefault()

    let title = nameInput.value
    let type = typeInput.value
    let description = descriptionTextarea.value
    let teacherName = teacherNameInput.value

    let data = {
        title: title,
        type: type,
        description: description,
        teacher: teacherName
    }

    fetch(`${baseURL}/${ids[id]}`, {
        method: "PUT",
        body: JSON.stringify(data)
    })
      .then(loadHandler)
      .catch(() =>{
        console.log("error");
      })
    
    nameInput.value = ""
    typeInput.value = ""
    descriptionTextarea.value = ""
    teacherNameInput.value = ""

    editBtn.disabled = true
    addBtn.disabled = false
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