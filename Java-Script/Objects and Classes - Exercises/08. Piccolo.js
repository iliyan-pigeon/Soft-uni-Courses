function carNumbersCollector(data){
    carsInParking = []
    
    for (const car of data){
        let [direction, carNumber] = car.split(", ")
        if (direction === "IN" && !carsInParking.includes(carNumber)){
            carsInParking.push(carNumber)
        }else if (direction === "OUT" && carsInParking.includes(carNumber)){
            let index = carsInParking.indexOf(carNumber)
            carsInParking.splice(index, 1)
        }
    }

    if (carsInParking){
        carsInParking = carsInParking.sort((carNumOne, carNumTwo) => carNumOne.localeCompare(carNumTwo))
        carsInParking.forEach(carNum => {
            console.log(carNum);
        });
    }else{
        console.log("Parking Lot is Empty");
    }
}