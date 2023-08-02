function getInfo() {
    let inputStopId = document.getElementById("stopId").value
    let stopName = document.getElementById("stopName")
    let allBuses = document.getElementById("buses")
    let baseURL = "http://localhost:3030/jsonstore/bus/businfo"

    fetch(`${baseURL}/${inputStopId}`)
      .then((response) => response.json())
      .then((currentStop) => {
        let {name, buses} = currentStop
        stopName.textContent = name
        for (let busNumber in buses){
            let busLi = document.createElement("li")
            busLi.textContent = `Bus ${busNumber} arrives in ${buses[busNumber]} minutes`
            allBuses.appendChild(busLi)
        }
      })
      .catch(() => {
        stopName.textContent = "Error"
      })
}