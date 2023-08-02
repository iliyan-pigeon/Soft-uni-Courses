function solve() {
    let infoSpan = document.querySelector("#info > span")
    let departButton = document.getElementById("depart")
    let arriveButton = document.getElementById("arrive")
    let baseURL = "http://localhost:3030/jsonstore/bus/schedule"
    let currentStationId = "depot"
    let currentStationName = null
    function depart() {
      arriveButton.disabled = false
      departButton.disabled = true
      fetch(`${baseURL}/${currentStationId}`)
        .then((response) => response.json())
        .then((currentStation) =>{
            let {name, next} = currentStation
            currentStationId = next
            currentStationName = name
            infoSpan.textContent = `Next stop ${name}`
        })
        .catch(() =>{
            infoSpan.textContent = "Error"
            arriveButton.disabled = false
            departButton.disabled = true
        })
    } 

    async function arrive() {
      arriveButton.disabled = true
      departButton.disabled = false
      infoSpan.textContent = `Arriving at ${currentStationName}`
    }

    return {
        depart,
        arrive
    };
}

let result = solve();