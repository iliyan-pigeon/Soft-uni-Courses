function wordsAccomodation(words, sentence){
    let wordsArray = words.split(", ")
    let arraySentence = sentence.split(" ")

    for (let word in wordsArray){
        for (let sWord in arraySentence){
            if (wordsArray[word].length == arraySentence[sWord].length
                && arraySentence[sWord].includes("*") == true){
                arraySentence[sWord] = wordsArray[word]
            }
        }
    }

    return arraySentence.join(" ")
}