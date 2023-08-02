function attachEvents() {
  let baseURL = "http://localhost:3030/jsonstore/collections/books"
  let allButtons = Array.from(document.getElementsByTagName("button"))
  let loadBooksBtn = allButtons[0]
  let submitBth = allButtons[5]
  let h3Form = document.getElementsByTagName("h3")[0]

  let tbody = document.querySelector("table tbody")
  let bookIds = {}
  let id = null

  let [inputTitle, inputAuthor] = Array.from(document.getElementsByTagName("input"))
  
  loadBooksBtn.addEventListener("click", booksLoader)
  submitBth.addEventListener("click", addBook)

  function booksLoader(){
    tbody.innerHTML = ""
    bookIds = {}
    fetch(baseURL)
      .then((response) => response.json())
      .then((data) => {
        for (let book in data){
          let {author, title} = data[book]
          bookIds[title] = book
          let tr = elementCreator("tr", null, tbody)
          let tdTitle = elementCreator("td", `${title}`, tr)
          let tdAuthor = elementCreator("td", `${author}`, tr)
          let tdButtons = elementCreator("td", null, tr)
          let editBtn = elementCreator("button", "Edit", tdButtons)
          let deleteBtn = elementCreator("button", "Delete", tdButtons)
          editBtn.addEventListener("click", editHandler)
          deleteBtn.addEventListener("click", deleteHandler)
        }
      })
  }

  function editHandler(){
    h3Form.textContent = "Edit FORM"
    submitBth.textContent = "Save"
    id = bookIds[this.parentElement.parentElement.children[0].textContent]
    inputTitle.value = this.parentElement.parentElement.children[0].textContent
    inputAuthor.value = this.parentElement.parentElement.children[1].textContent
  }

  function deleteHandler(){
    id = bookIds[this.parentElement.parentElement.children[0].textContent]

    fetch(`${baseURL}/${id}`, {
      method: "DELETE"
    })
      .then(booksLoader)
      .catch(() =>{
        console.log(Error);
      })
  }

  function addBook(){
    if (inputTitle.value.length !== 0 && inputAuthor.value.length !== 0){
      if(submitBth.textContent === "Save"){
        h3Form.textContent = "FORM"
        submitBth.textContent = "Submit"

        let authorToAdd = inputAuthor.value
        let titleToAdd = inputTitle.value
        
        let data = {
          "author": authorToAdd,
          "title": titleToAdd
        }
        console.log(titleToAdd);

        fetch(`${baseURL}/${id}`, {
          method: "PUT",
          body: JSON.stringify(data)
        })
          .then(booksLoader)
          .catch(() => {
            console.log(Error);
          })

        inputTitle.value = ""
        inputAuthor.value = ""
      }else{
        let authorToAdd = inputAuthor.value
        let titleToAdd = inputTitle.value
        let data = {
          "author": authorToAdd,
          "title": titleToAdd
        }
  
        fetch(baseURL, {
          method: "POST",
          body: JSON.stringify(data)
        })
          .then(booksLoader)
          .catch(() => {
            console.log(Error);
          })
        }
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

attachEvents(); 