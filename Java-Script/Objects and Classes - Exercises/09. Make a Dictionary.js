function jsonDictionaryParser(data){
    let terms = {}

    for (const line of data){
        let [term, explanation] = line.split('":"')
        terms[term] = explanation
    }

    terms = Object.entries(terms).sort(([a,],[b,]) => a.localeCompare(b))
    
    for(const line of terms){
        console.log(`Term: ${line[0].substring(2)} => Definition: ${line[1].slice(0, line[1].length-2)}`);
    }
}
