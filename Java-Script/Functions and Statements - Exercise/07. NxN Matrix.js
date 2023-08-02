function matrixCreator(number){
    let matrix = []
    let row = []

    for (i=0; i<Number(number); i++){
        row.push(number)
    }

    row = row.join(" ")
    for (i=0; i<Number(number); i++){
        matrix.push(row)
    }

    return matrix.join("\n")
}

matrixCreator(3)