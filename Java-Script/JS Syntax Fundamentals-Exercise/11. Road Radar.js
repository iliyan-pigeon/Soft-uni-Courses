function radar(speed, area){
    let speedLimit = 0
    let result = ""

    if (area == "motorway"){
        speedLimit = 130
    }else if (area == "interstate"){
        speedLimit = 90
    }else if (area == "city"){
        speedLimit = 50
    }else if (area == "residential"){
        speedLimit = 20
    }

    if (speedLimit >= speed){
        result = `Driving ${speed} km/h in a ${speedLimit} zone`
        console.log(result);
    }else{
        let difference = Math.abs(speed - speedLimit)
        let status = ""

        if (difference <= 20){
            status = "speeding"
        }else if (difference <= 40){
            status = "excessive speeding"
        }else{
            status = "reckless driving"
        }

        result = `The speed is ${difference} km/h faster than the allowed speed of ${speedLimit} - ${status}`
        console.log(result);
    }
}