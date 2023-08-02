function takeCharsInRange(firstChar, secondChar){
    let firstAscii = firstChar.charCodeAt(0)
    let secondAscii = secondChar.charCodeAt(0)
    let result = ''
    let start = 0
    let end = 0

    if (firstAscii > secondAscii){
        start = secondAscii
        end = firstAscii
    }else {
        start = firstAscii
        end = secondAscii
    }

    for (i=start+1; i<end; i++){
        result += " "
        result += String.fromCharCode(i)
    }

    return result
}

takeCharsInRange('a', 'd')