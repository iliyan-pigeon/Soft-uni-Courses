function solve(sentence, searchedWord){
    while (sentence.includes(searchedWord)){
        sentence = sentence.replace(searchedWord, "*".repeat(searchedWord.length))
    }

    console.log(sentence);
}