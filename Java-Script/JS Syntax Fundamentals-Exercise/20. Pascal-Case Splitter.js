function wordsDelimiter(sentence){
    let separatedWords = []
    let currentWord = ''
    sentence += "A"

    for (const ch in sentence){
        if (sentence[ch].toUpperCase() === sentence[ch]){
            if (currentWord.length != 0){
                separatedWords.push(currentWord)
                currentWord = ''   
            }
        }
        currentWord += sentence[ch]
    }

    console.log(separatedWords.join(", "));
}
