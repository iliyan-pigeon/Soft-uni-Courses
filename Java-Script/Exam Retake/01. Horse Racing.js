function horseRace(data){
    let positions = data.shift().split("|")
    
    for (let command of data){
        command = command.split(" ")
        let theCommand = command[0]
        
        if (theCommand === "Retake"){
            let overtaking = command[1]
            let overtaken = command[2]

            let overtakingIndex = positions.indexOf(overtaking)
            let overtakenIndex = positions.indexOf(overtaken)

            if (overtakingIndex < overtakenIndex) {
                positions.splice(overtakingIndex, 1);
                positions.splice(overtakenIndex, 0, overtaking);
                console.log(`${overtaking} retakes ${overtaken}.`);
              }
        }else if (theCommand === "Trouble"){
            let horseName = command[1];
            let horseIndex = positions.indexOf(horseName);
            if (horseIndex !== 0) {
                positions.splice(horseIndex, 1);
                positions.splice(horseIndex - 1, 0, horseName);
                console.log(`Trouble for ${horseName} - drops one position.`);
            }
        }else if (theCommand === "Rage"){
            let horseName = command[1];
            let horseIndex = positions.indexOf(horseName);
            if (horseIndex !== positions.length - 1) {
                if (horseIndex === positions.length - 2){
                    positions.splice(horseIndex, 1);
                    positions.splice(horseIndex + 1, 0, horseName);
                }else{
                    positions.splice(horseIndex, 1);
                    positions.splice(horseIndex + 2, 0, horseName);
                }
                console.log(`${horseName} rages 2 positions ahead.`);
            }
        }else if (theCommand === "Miracle"){
            let horseName = positions[0];
            positions.splice(0, 1);
            positions.splice(positions.length, 0, horseName);
            console.log(`What a miracle - ${horseName} becomes first.`);
        }else if (theCommand === "Finish"){
            let winner = positions[positions.length - 1]
            console.log(positions.join("->"));
            console.log(`The winner is: ${winner}`);
        }
    }
}


horseRace((['Bella|Alexia|Sugar',
'Retake Alexia Sugar',
'Rage Bella',
'Trouble Bella',
'Miracle',
'Finish']))