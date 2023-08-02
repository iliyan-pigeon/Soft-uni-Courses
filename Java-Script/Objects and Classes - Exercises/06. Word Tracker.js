function wordsTracker(data){
    let searchedWords = data.shift().split(" ")
    let collectedWords = {}

    for (const searched of searchedWords){
        collectedWords[searched] = 0
    }

    for (const word of data){
        if (searchedWords.includes(word)){
            collectedWords[word] += 1
        }
    }

    collectedWords = Object.entries(collectedWords)
        .sort((firstWord, secondWord) => {
        let [_firstName, firstCount] = firstWord;
        let [_secondName, secondCount] = secondWord
        return secondCount - firstCount   
    })

    for (const word of collectedWords){
        let name = word[0]
        let count = word[1]

        console.log(`${name} - ${count}`);
    }
}

wordsTracker([
    'this sentence',
    'In', 'this', 'sentence', 'you', 'have',
    'to', 'count', 'the', 'occurrences', 'of',
    'the', 'words', 'this', 'and', 'sentence',
    'because', 'this', 'is', 'your', 'task'
    ])