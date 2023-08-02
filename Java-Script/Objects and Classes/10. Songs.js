function songs(data){
    class Song{
        constructor(type, name, time){
            this.type = type
            this.name = name
            this.time = time
        }
    }

    let songs = []
    let numberOfSongs = data.shift()
    let songType = data.pop()

    for (const info of data){
        let [songType, songName, songTime] = info.split("_")
        songs.push(new Song(songType, songName, songTime))
    }

    if (songType === "all"){
        songs.forEach((i) => console.log(i.name))
    }else{
        let filtered = songs.filter((i) => i.type === songType)
        filtered.forEach((i) => console.log(i.name))
    }
}