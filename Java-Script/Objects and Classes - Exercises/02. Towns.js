function citiesCoordinates(data){
    for (const city of data){
        let info = city.split(" | ")
        let town = info[0]
        let latitude = Number(info[1]).toFixed(2)
        let longitude = Number(info[2]).toFixed(2)
        
        townObject = {town, latitude, longitude}
        console.log(townObject);
    }
} 