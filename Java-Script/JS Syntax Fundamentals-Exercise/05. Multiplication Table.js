function tenTimesTable(number){
    for (i=1; i<= 10; i++){
        calculationResult = number * i
        result = `${number} X ${i} = ${calculationResult}`
        console.log(result);
    }
}