function formatGrade(grade){
    let finalGrade = ''

    if (grade < 3.00){
        finalGrade = `Fail (2)`
    }else if (grade >= 3.00 && grade < 3.50){
        finalGrade = `Poor (${grade.toFixed(2)})`
    }else if (grade >= 3.50 && grade < 4.50){
        finalGrade = `Good (${grade.toFixed(2)})`
    }else if (grade >= 4.50 && grade < 5.50){
        finalGrade = `Very good (${grade.toFixed(2)})`
    }else if (grade >= 5.50){
        finalGrade = `Excellent (${grade.toFixed(2)})`
    }

    console.log(finalGrade);
}