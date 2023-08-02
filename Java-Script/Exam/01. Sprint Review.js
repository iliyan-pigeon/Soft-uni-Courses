function solve(data){
    let number = data.shift()
    let elements = []

    for (let i=0; i<number; i++){
        let current = data[i].split(":")
        let assignee = current.shift()
        current.join(", ")
        if (elements.hasOwnProperty(assignee)){
            elements[assignee].push(current)
        }else{
            elements[assignee] = [current]
        }
        
    }

    data.splice(0, number)
    
    for (let e of data){
        e = e.split(":")
        let command = e.shift()
        
        if (command === "Add New"){
            let [assignee, taskId, title, theStatus, points] = e
            if (elements.hasOwnProperty(assignee)){
                elements[assignee].push([taskId, title, theStatus, points])
            }else{
                console.log(`Assignee ${assignee} does not exist on the board!`);
            }
        }else if(command === "Change Status"){
            let addedStat = false
            let [assignee, taskId, newStatus] = e
            if (!elements.hasOwnProperty(assignee)){
                console.log(`Assignee ${assignee} does not exist on the board!`);
            }else{
                for (let task of elements[assignee]){
                    if (taskId === task[0]){
                        task[2] = newStatus
                        addedStat = true
                        break
                    }
                }
                if (!addedStat){
                    console.log(`Task with ID ${taskId} does not exist for ${assignee}!`);
            }
            }
        }else if (command === "Remove Task"){
            let [assignee, index] = e
            if (!elements.hasOwnProperty(assignee)){
                console.log(`Assignee ${assignee} does not exist on the board!`);
            }else if (elements[assignee].length <= index){
                console.log(`Index is out of range!`);
            }else if (elements[assignee].length > index){
                elements[assignee].splice(index, 1)
            }
        }
    }

    let todoPoints = 0
    let inProgress = 0
    let codeReview = 0
    let donePoints = 0

    for (let ass in elements){
        for (let i of elements[ass]){
            if (i[2] === "ToDo"){
                todoPoints += Number(i[3])
            }else if (i[2] === "In Progress"){
                inProgress += Number(i[3])
            }else if (i[2] === "Code Review"){
                codeReview += Number(i[3])
            }else if (i[2] === "Done"){
                donePoints += Number(i[3])
            }
        }
    }

    console.log(`ToDo: ${todoPoints}pts`);
    console.log(`In Progress: ${inProgress}pts`); 
    console.log(`Code Review: ${codeReview}pts`); 
    console.log(`Done Points: ${donePoints}pts`); 
    
    let othersSum = todoPoints + inProgress + codeReview

    if (othersSum <= donePoints){
        console.log('Sprint was successful!');
    }else{
        console.log("Sprint was unsuccessful...");
    }
}




solve([
    "4",
    "Kiril:BOP-1213:Fix Typo:Done:1",
    "Peter:BOP-1214:New Products Page:In Progress:2",
    "Mariya:BOP-1215:Setup Routing:ToDo:8",
    "Georgi:BOP-1216:Add Business Card:Code Review:3",
    "Add New:Sam:BOP-1237:Testing Home Page:Done:3",
    "Change Status:Georgi:BOP-1216:Done",
    "Change Status:Will:BOP-1212:In Progress",
    "Remove Task:Georgi:3",
    "Change Status:Mariya:BOP-1215:Done",
    ])