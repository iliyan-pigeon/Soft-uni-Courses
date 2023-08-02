function attachEvents() {
  let baseURL = "http://localhost:3030/jsonstore/collections/students"
  let tbody = document.querySelector("#results > tbody")
  let inputs = document.getElementsByClassName("inputs")[0].children
  let [first, last, facN, grd] = inputs
  let submitBtn = document.getElementById("submit")

  window.addEventListener("load", loadGrades)
  submitBtn.addEventListener("click", studentCreator)

  function loadGrades(){
    tbody.textContent = ""
    fetch(baseURL)
      .then((response) => response.json())
      .then((data) => {
        for (let student in data){
          let {firstName, lastName, facultyNumber, grade, _id} = data[student]
          let tr = document.createElement("tr")
          let tdFirstName = document.createElement("td")
          tdFirstName.textContent = firstName
          let tdLastName = document.createElement("td")
          tdLastName.textContent = lastName
          let tdFacNumber = document.createElement("td")
          tdFacNumber.textContent = facultyNumber
          let tdGrade = document.createElement("td")
          tdGrade.textContent = grade
          tr.appendChild(tdFirstName)
          tr.appendChild(tdLastName)
          tr.appendChild(tdFacNumber)
          tr.appendChild(tdGrade)
          tbody.appendChild(tr)
        }
      })
  }

  function studentCreator(){
    let data = {
      "firstName": first.value,
      "lastName": last.value,
      "facultyNumber": facN.value,
      "grade": grd.value
    }

    fetch(baseURL, {
      method: "POST",
      body: JSON.stringify(data)
    })
      .then(loadGrades)
      .catch(() => {
        console.log(Error);
      })
  }
}

attachEvents();