window.addEventListener('load', solve);

function solve() {
    let hiddenInput = document.getElementById("task-id")
    let titleInput = document.getElementById("title")
    let descriptionTextarea = document.getElementById("description")
    let labelSelect = document.getElementById("label")
    let pointsInput = document.getElementById("points")
    let assigneeInput = document.getElementById("assignee")

    let createTaskBtn = document.getElementById("create-task-btn")
    let deleteTaskBtn = document.getElementById("delete-task-btn")

    let tasksSection = document.getElementById("tasks-section")
    let totalSprintPointsP = document.getElementById("total-sprint-points")
    let totalPoints = 0
    let taskNumber = 1

    createTaskBtn.addEventListener("click", createHandler)

    function createHandler(){
        if (titleInput.value !== "" && descriptionTextarea.value !== "" && 
        labelSelect.value !== "" && pointsInput.value !== "" &&
         assigneeInput.value !== ""){
            let title = titleInput.value
            let description = descriptionTextarea.value
            let label = labelSelect.value
            let points = Number(pointsInput.value)
            let assignee = assigneeInput.value

            totalPoints += points

            let article = elementCreator("article", null, tasksSection, `task-${taskNumber}`, ["task-card"])
            taskNumber += 1
            if (labelSelect.value === "Feature"){
                let divLabel = elementCreator("div", `${label} ⊡`, article, null, ["task-card-label", "feature"])
            }else if (labelSelect.value === "Low Priority Bug"){
                let divLabel = elementCreator("div", `${label} ☉`, article, null, ["task-card-label", "low-priority"])
            }else if (labelSelect.value === "High Priority Bug"){
                let divLabel = elementCreator("div", `${label} ⚠`, article, null, ["task-card-label", "high-priority"])
            }
            let titleH3 = elementCreator("h3", title, article, null, ["task-card-title"])
            let descriptionP = elementCreator("p", description, article, null, ["task-card-description"])
            let pointsDiv = elementCreator("div", `Estimated at ${points} pts`, article, null, ["task-card-points"])
            let assigneeDiv = elementCreator("div", `Assigned to: ${assignee}`, article, null, ["task-card-assignee"])
            let actionsDiv = elementCreator("div", null, article, null, ["task-card-actions"])
            let deleteBtn = elementCreator("button", "Delete", actionsDiv)

            titleInput.value = ""
            descriptionTextarea.value = ""
            labelSelect.value = ""
            pointsInput.value = ""
            assigneeInput.value = ""

            deleteBtn.addEventListener("click", () => {
                titleInput.value = titleH3.textContent
                descriptionTextarea.value = descriptionP.textContent
                labelSelect.value = label
                pointsInput.value = points
                assigneeInput.value = assigneeDiv.textContent

                createTaskBtn.setAttribute("disabled", true)
                deleteTaskBtn.disabled = false
                deleteBtn.setAttribute("disabled", true)

                titleInput.setAttribute("disabled", true)
                descriptionTextarea.setAttribute("disabled", true)
                labelSelect.setAttribute("disabled", true)
                pointsInput.setAttribute("disabled", true)
                assigneeInput.setAttribute("disabled", true)
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
}