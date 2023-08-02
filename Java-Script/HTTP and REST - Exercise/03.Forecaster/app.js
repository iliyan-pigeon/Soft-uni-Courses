function attachEvents() {
  let locationInput = document.getElementById("location")
  let locationInputButton = document.getElementById("submit")
  let forecast = document.getElementById("forecast")
  let currentForecast = document.getElementById("current")
  let upcomingForecast = document.getElementById("upcoming")
  let locationsURL = "http://localhost:3030/jsonstore/forecaster/locations"
  let todayURL = "http://localhost:3030/jsonstore/forecaster/today"
  let upcomingURL = "http://localhost:3030/jsonstore/forecaster/upcoming"
  locationInputButton.addEventListener("click",  locationsHandler)

  function locationsHandler(){
    fetch(`${locationsURL}`)
      .then((response) => response.json())
      .then((locations) => {
        let searchedLocationName = locationInput.value
        let searchedLocationCode = null
        for (let l of locations){
            let {code, name} = l
            if (searchedLocationName === name){
                searchedLocationCode = code
            }
        }
        fetch(`${todayURL}/${searchedLocationCode}`)
          .then((response) => response.json())
          .then((info) => {
            let name = info["name"]
            let condition = info["forecast"]["condition"]
            let highDegree = info["forecast"]["high"]
            let lowDegree = info["forecast"]["low"]
            let divForecasts = document.createElement("div")
            divForecasts.className = "forecasts"
            let spanConditionSymbol = document.createElement("span")
            spanConditionSymbol.className = "condition symbol"
            if (condition === "Sunny"){
                spanConditionSymbol.textContent = "☀"
            }else if ( condition === "Partly sunny"){
                spanConditionSymbol.textContent = "⛅"
            }else if (condition === "Overcast"){
                spanConditionSymbol.textContent = "☁"
            }else if (condition === "Rain"){
                spanConditionSymbol.textContent = "☂"
            }
            divForecasts.appendChild(spanConditionSymbol)
            let spanCondition = document.createElement("span")
            spanCondition.className = "condition"
            divForecasts.appendChild(spanCondition)
            let spanName = document.createElement("span")
            spanName.className = "forecast-data"
            spanName.textContent = name
            spanCondition.appendChild(spanName)
            let spanTemperature = document.createElement("span")
            spanTemperature.className = "forecast-data"
            spanTemperature.textContent = `${lowDegree}°/${highDegree}°`
            spanCondition.appendChild(spanTemperature)
            let theCondition = document.createElement("span")
            theCondition.className = "forecast-data"
            theCondition.textContent = condition
            spanCondition.appendChild(theCondition)
            currentForecast.appendChild(divForecasts)
            forecast.style.display = "block"
          })
          .catch(() =>{
            forecast.style.display = "block"
            forecast.textContent = "Error"
          })

        fetch(`${upcomingURL}/${searchedLocationCode}`)
          .then((response) => response.json())
          .then((upcomingDays) => {
            let forecastInfo = document.createElement("div")
            forecastInfo.className = "forecast-info"
            upcomingForecast.appendChild(forecastInfo)
            upcomingDays = upcomingDays["forecast"]
            for (let day of upcomingDays){
              let condition = day["condition"]
              let highDegree = day["high"]
              let lowDegree = day["low"]
              let spanUpcoming = document.createElement("span")
              spanUpcoming.className = "upcoming"
              let spanSymbol = document.createElement("span")
              spanSymbol.className = "symbol" 
              if (condition === "Sunny"){
                spanSymbol.textContent = "☀"
              }else if ( condition === "Partly sunny"){
                  spanSymbol.textContent = "⛅"
              }else if (condition === "Overcast"){
                  spanSymbol.textContent = "☁"
              }else if (condition === "Rain"){
                  spanSymbol.textContent = "☂"
              }
              spanUpcoming.appendChild(spanSymbol)
              let spanDegreesRange = document.createElement("span")
              spanDegreesRange.className = "forecast-data"
              spanDegreesRange.textContent = `${lowDegree}°/${highDegree}°`
              spanUpcoming.appendChild(spanDegreesRange)
              let spanForecastCondition = document.createElement("span")
              spanForecastCondition.className = "forecast-data"
              spanForecastCondition.textContent = condition
              spanUpcoming.appendChild(spanForecastCondition)
              forecastInfo.appendChild(spanUpcoming)
              forecast.style.display = "block"            
              }
          })
          .catch(() =>{
            forecast.style.display = "block"
            forecast.textContent = "Error"
          })
      })
      .catch(() =>{
        forecast.style.display = "block"
        forecast.textContent = "Error"
      })
  }
}


attachEvents();