function attachEvents() {
    let baseURL = "http://localhost:3030/jsonstore/phonebook"
    let loadBtn = document.getElementById("btnLoad")
    let createBtn = document.getElementById("btnCreate")
    let phonebook = document.getElementById("phonebook")
    let personInput = document.getElementById("person")
    let phoneInput = document.getElementById("phone")

    let dataStorage = {}

    loadBtn.addEventListener("click", phonebookLoader)
    createBtn.addEventListener("click", creator)

    function phonebookLoader(){
        fetch(baseURL)
          .then((response) => response.json())
          .then((data) => {
            for (let user in data){
                let {person, phone} = data[user]
                dataStorage[`${person}: ${phone}`] = data[user]
                let li = elementCreator("li", `${person}: ${phone}`, phonebook)
                let liButton = elementCreator("button", "Delete", li)
                liButton.addEventListener("click", deleteHandler)

                function deleteHandler(){
                  let parentLi = this.parentElement
                  let key = parentLi.textContent.slice(0, -6)
                  let id = dataStorage[key]["_id"]
                  fetch(`${baseURL}/${id}`, {
                    method: "DELETE"
                  })
                    .then((response) => response.json())
                    .then((data) =>{
                        console.log(data);
                    })
                    .catch(() => {
                        console.log(error);
                    })
                  parentLi.remove()  
                }
            }
          })
    }

   function creator(){
       let deletePerson = personInput.value
       let deletePhone = phoneInput.value
       let deleteData = {
        "person": deletePerson,
        "phone": deletePhone
       }

       fetch(`${baseURL}`, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(deleteData)
       })
         .then(() => {
            phonebook.innerHTML = ""
            personInput.value = ""
            phoneInput.value = ""
            phonebookLoader()
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

attachEvents();