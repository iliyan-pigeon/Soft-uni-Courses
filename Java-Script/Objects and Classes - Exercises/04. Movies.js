function moviesColector(data){
    let movies = []

    for (let command of data){
        command = command.split(" ")
        if (command.includes("addMovie")){
            command.shift()
            let movie = {"name": command.join(" ")}
            movies.push(movie)
        }else if (command.includes("directedBy")){
            let movieName = []

            for (const  word of command){
                if (word === "directedBy"){
                    for (i=0; i<=movieName.length; i++){
                        command.shift()
                    }
                    break
                }else{
                    movieName.push(word)
                }
            }
            let movie = movies.find((m) => m.name === movieName.join(" "))    
            if (movie){
                movie["director"] = command.join(" ")
            }   
        }else{
            let movieName = []

            for (const word of command){
                if (word === "onDate"){
                    for (i=0; i<=movieName.length; i++){
                        command.shift()
                    }
                    break
                }else{
                    movieName.push(word)
                }
            }    
            let movie = movies.find((m) => m.name === movieName.join(" "))    
            if (movie){
                movie["date"] = command.join(" ")
            }
        }
    }
    for (let movie of movies){
        let movieKeys = Object.keys(movie)
        if (movieKeys.includes("director") && movieKeys.includes("date")){
            console.log(JSON.stringify(movie));
        }
    }
}

moviesColector(['addMovie Fast and Furious','addMovie Godfather','Inception directedBy Christopher Nolan','Godfather directedBy Francis Ford Coppola','Godfather onDate 29.07.2018','Fast and Furious onDate 30.07.2018','Batman onDate 01.08.2018','Fast and Furious directedBy Rob Cohen'])