function priceCalculator(peopleNumber, groupType, day){
    let totalPrice
    let singlePersonPrice

    if (groupType == "Students"){

       if (day == "Friday"){
            singlePersonPrice = 8.45
       }else if (day == "Saturday"){
            singlePersonPrice = 9.80
       }else if (day == "Sunday"){
            singlePersonPrice = 10.46
       }

        totalPrice = singlePersonPrice * peopleNumber
        
        if (peopleNumber >= 30){
            totalPrice -= (totalPrice * 0.15) 
        }

    }else if (groupType == "Business"){

        if (day == "Friday"){
            singlePersonPrice = 10.90    
        }else if (day == "Saturday"){
            singlePersonPrice = 15.60
        }else if (day == "Sunday"){
            singlePersonPrice = 16
        }
        
        totalPrice = singlePersonPrice * peopleNumber

        if (peopleNumber >= 100){
            totalPrice -= (singlePersonPrice * 10)
        }
        
     }else if (groupType == "Regular"){

        if (day == "Friday"){
            singlePersonPrice = 15            
        }else if (day == "Saturday"){
            singlePersonPrice = 20
        }else if (day == "Sunday"){
            singlePersonPrice = 22.50 
        } 

        totalPrice = singlePersonPrice * peopleNumber

        if (peopleNumber >= 10 && peopleNumber <= 20){
            totalPrice -= (totalPrice * 0.05)
        }

     }

     console.log(`Total price: ${totalPrice.toFixed(2)}`);

}