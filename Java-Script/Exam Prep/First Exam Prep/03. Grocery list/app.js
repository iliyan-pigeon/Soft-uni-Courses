let productInput = document.getElementById("product")
let countInput = document.getElementById("count")
let priceInput = document.getElementById("price")

let addProductBtn = document.getElementById("add-product")
let updateProductBtn = document.getElementById("update-product")
let loadProductBtn = document.getElementById("load-product")

let tbody = document.getElementById("tbody")
let baseURL = "http://localhost:3030/jsonstore/grocery"
let productIds = {}
let id = null
let secondary = false

loadProductBtn.addEventListener("click", loadProductsHandler)
addProductBtn.addEventListener("click", addProductHandler)
updateProductBtn.addEventListener("click", updateProductHandler)

function loadProductsHandler(event){
    productIds = {}
    tbody.innerHTML = ""
    if (!secondary){
        event.preventDefault()
    }
    secondary = false
    fetch(baseURL)
      .then((response) => response.json()) 
      .then((data) => {
        for (let info in data){
            let {count, price, product, _id} = data[info]
            productIds[product] = _id
            let tr = elementCreator("tr", null, tbody)
            let tdProcudtName = elementCreator("td", product, tr, null, ["name"])
            let tdCount = elementCreator("td", count, tr, null, ["count-product"])
            let tdPrice = elementCreator("td", price, tr, null, ["product-price"])
            let tdAction = elementCreator("td", null, tr, null, ["btn"])
            let updateBtn = elementCreator("button", "Update", tdAction, null, ["update"])
            let deleteBtn = elementCreator("button", "Delete", tdAction, null, ["delete"])

            deleteBtn.addEventListener("click", () => {
                secondary = true
                let id = productIds[deleteBtn.parentElement.parentElement.children[0].textContent]
                
                fetch(`${baseURL}/${id}`, {
                    method: "DELETE"
                })
                  .then(loadProductsHandler)
                  .catch(() => {
                    console.log("error");
                  })
            })

            updateBtn.addEventListener("click", () => {
                secondary = true
                let name = deleteBtn.parentElement.parentElement.children[0].textContent
                let count = deleteBtn.parentElement.parentElement.children[1].textContent
                let price = deleteBtn.parentElement.parentElement.children[2].textContent
                id = productIds[name]

                productInput.value = name
                countInput.value = count
                priceInput.value = price

                addProductBtn.setAttribute('disabled', true)
                updateProductBtn.disabled = false
            })
        }
  })
}

function addProductHandler(event){
    secondary = true
    event.preventDefault()
    let data = {
        product: productInput.value,
        count: countInput.value,
        price: priceInput.value
    }

    productInput.value = ""
    countInput.value = ""
    priceInput.value = ""

    fetch(baseURL, {
        method: "POST",
        body: JSON.stringify(data)
    })
      .then(loadProductsHandler)
      .catch(() =>{
        console.log("error");
      })
}

function updateProductHandler(event){
    secondary = true
    event.preventDefault()

  updateProductBtn.setAttribute("disabled", true)
  addProductBtn.disabled = false
  
  let data = {
    product: productInput.value,
    count: countInput.value,
    price: priceInput.value
  }

  productInput.value = ""
  countInput.value = ""
  priceInput.value = ""

  fetch(`${baseURL}/${id}`, {
    method: "PATCH",
    body: JSON.stringify(data)
  })
    .then(id = null)
    .then(loadProductsHandler)
    .then(() => {
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