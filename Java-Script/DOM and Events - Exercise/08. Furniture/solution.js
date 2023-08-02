function solve() {
  let textAraeas = document.getElementsByTagName("textarea")
  let generateTextArea = textAraeas[0]
  let buyTextArea = textAraeas[1]
  let buttons = document.getElementsByTagName("button")
  let generateButton = buttons[0]
  let buyButton = buttons[1]
  let tbody = document.querySelector("table > tbody")
  generateButton.addEventListener("click", generate)
  buyButton.addEventListener("click", calculate)

  function calculate() {
    let checkedInputs = Array.from(document.querySelectorAll("input:checked"))
    let boughtFurniture = []
    let totalPrice = 0
    let totalDecorationFactor = 0

    for (let input of checkedInputs){
      let tableRow = Array.from(input.parentElement.parentElement.children)
      counter = 0
      for (let child of tableRow){
        if (counter === 0){
          counter += 1
        }else if (counter === 1){
          boughtFurniture.push(child.children[0].textContent)
          counter += 1
        }else if (counter === 2){
          totalPrice += Number(child.children[0].textContent)
          counter += 1
        }else if (counter === 3){
          totalDecorationFactor += Number(child.children[0].textContent)
        }
      }
    }
    
    let averageDecorationFactor = totalDecorationFactor / boughtFurniture.length
    buyTextArea.value += `Bought furniture: ${boughtFurniture.join(", ")}\n`
    buyTextArea.value += `Total price: ${totalPrice.toFixed(2)}\n`
    buyTextArea.value += `Average decoration factor: ${averageDecorationFactor}`
  }

  function generate() {
    let data = JSON.parse(generateTextArea.value)
    for (let {img, name, price, decFactor} of data){
      let tr = elementCreator("tr", "", tbody)
      let tbFirst = elementCreator("td", "", tr)
      elementCreator("img", "", tbFirst, "", "", {src: img})
      let tbSecond = elementCreator("td", "", tr)
      elementCreator("p", name, tbSecond)
      let tbThird = elementCreator("td", "", tr)
      elementCreator("p", price, tbThird)
      let tbFourth = elementCreator("td", "", tr)
      elementCreator("p", decFactor, tbFourth)
      let tbFifth = elementCreator("td", "", tr)
      elementCreator("input", "", tbFifth, "", "", {type: "checkbox"})
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
