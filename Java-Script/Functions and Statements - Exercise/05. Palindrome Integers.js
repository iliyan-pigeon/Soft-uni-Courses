function palindromeVerifier(numbers){
    let answers = []

    for (const number in numbers){
        let reversedNumber = String(numbers[number]).split("").reverse().join("")
        if (numbers[number] == reversedNumber){
            answers.push(true)
        }else {
            answers.push(false)
        }
    }

    return answers.join("\n")
}