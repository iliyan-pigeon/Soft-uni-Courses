function oddAppearances(data){
    let wordsCount = {}
    let wordsArray = data.split(" ")

    for (const word of wordsArray){
        wordsCount[word.toLowerCase()] = 0

        for (const searchedWord of wordsArray){
            if (word.toLowerCase() === searchedWord.toLowerCase()){
                wordsCount[word.toLowerCase()] += 1
            }
        }
    }

    let oddWordsCount = Object.entries(wordsCount).filter(([,a]) => a % 2 != 0)
    let result = []

    for (const array of oddWordsCount){
        result.push(array[0])
    }

    console.log(result.join(" "));
}
