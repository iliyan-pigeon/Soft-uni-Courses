function selectWords(sentence){
    let sentenceArray = sentence.split(" ")
    let selectedWords = []
    
    for (const word in sentenceArray){
        if (sentenceArray[word].startsWith("#") && /^[a-zA-Z]+$/.test(sentenceArray[word].slice(1))){
            selectedWords.push(sentenceArray[word].slice(1))
        }
    }

    console.log(selectedWords.join("\n"));
}
