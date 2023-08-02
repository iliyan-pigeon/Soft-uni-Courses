function wordFinder(searchedWord, sentence){
    let sentenceArray = sentence.split(" ")
    let wordFound = false
  
    for (const word in sentenceArray){
        if (sentenceArray[word].toLowerCase() === searchedWord){
            wordFound = true
            console.log(searchedWord);
        }
    }
    if (wordFound === false){
        console.log(`${searchedWord} not found!`);
    }
}