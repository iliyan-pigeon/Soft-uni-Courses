function solve(sentence, searchedWord){
    let words = sentence.split(" ")
    let occurances = 0

    for (let word of words){
        if (word == searchedWord){
            occurances += 1
        }
    }

    console.log(occurances);
}