function loadingProgress(percent){
    let loadingBar = []
    
    if (percent === 100){
        return "100% Complete!\n[%%%%%%%%%%]"
    }else {
        for (i=1; i<=percent/10; i++){
            loadingBar.push("%")
        }

        for (i=percent/10; i<10; i++){
            loadingBar.push(".")
        }

        let result = `${percent}% [${loadingBar.join("")}]\nStill loading...`
        return result
    }
}