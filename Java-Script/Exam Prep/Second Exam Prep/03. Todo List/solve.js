function attachEvents() {
    let baseURL = "http://localhost:3030/jsonstore/tasks"
    let titleInput = document.getElementById("title")

    let addBtn = document.getElementById("add-button")
    let loadBtn = document.getElementById("load-button")

    let todoList = document.getElementById("todo-list")
    let taskIds = {}
    let fromBtn = false

    loadBtn.addEventListener("click", loadHandler)
    addBtn.addEventListener("click", addHandler)

    function loadHandler(event) {
        if (fromBtn){
            fromBtn = false
        }else {
            event.preventDefault()
        }
        todoList.textContent = ""

        fetch(baseURL)
          .then((response) => response.json())
          .then((data) => {
            for (let task in data){
                let {name, _id} = data[task]
                taskIds[name] = _id

                let li = elementCreator("li", null, todoList)
                let span = elementCreator("span", name, li)
                let removeBtn = elementCreator("button", "Remove", li)
                let editBtn = elementCreator("button", "Edit", li)

                removeBtn.addEventListener("click", () => {
                    fromBtn = true
                    let id = taskIds[removeBtn.parentElement.children[0].textContent]

                    fetch(`${baseURL}/${id}`, {
                        method: "DELETE"
                    })
                      .then(loadHandler)
                      .catch(() => {
                        console.log("error");
                      })
                })

                editBtn.addEventListener("click", () => {
                    fromBtn = true
                    let name = editBtn.parentElement.children[0].textContent
                    let id = taskIds[name]
                    let li = editBtn.parentElement
                    li.innerHTML = ""
          
                    let nameInput = elementCreator("input", name, li)
                    let removeBtn = elementCreator("button", "Remove", li)
                    let submitBtn = elementCreator("button", "Submit", li)

                    removeBtn.addEventListener("click", () => {
                        fetch(`${baseURL}/${id}`, {
                            method: "DELETE"
                        })
                          .then(loadHandler)
                          .catch(() => {
                            console.log("error");
                          })
                    })

                    submitBtn.addEventListener("click", () => {
                        let body = {"name": nameInput.value}

                        fetch(`${baseURL}/${id}`, {
                            method: "PATCH",
                            body: JSON.stringify(body)
                        })
                          .then(loadHandler)
                          .catch(() => {
                            console.log("error");
                          })
                    })
                })
            }
          })
    }

    function addHandler(event) {
        fromBtn = true
        event.preventDefault()

        let task = titleInput.value
        let data = {"name": task}

        fetch(baseURL, {
            method: "POST",
            body: JSON.stringify(data)
        })
          .then(loadHandler)
          .catch(() => {
            console.log("error");
          })
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

attachEvents();
