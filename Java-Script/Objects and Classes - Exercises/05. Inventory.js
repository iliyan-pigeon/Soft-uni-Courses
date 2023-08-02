function heroesInvertory(data){
    let heroeObjects = []
    
    for (let line of data){
        line = line.split(" / ")
        let Hero = line.shift()
        let level = Number(line.shift())
        let items = []
        if (line){
            items = line
        }

        let heroInfo = {Hero, level, items}
        heroeObjects.push(heroInfo)
    }

    heroeObjects = heroeObjects.sort((a, b) => a.level - b.level)

    for (const {Hero, level, items} of heroeObjects){
        console.log(`Hero: ${Hero}`);
        console.log(`level => ${level}`);
        console.log(`items => ${items.join(", ")}`);
    }
}

heroesInvertory([
    'Isacc / 25 / Apple, GravityGun',
    'Derek / 12 / BarrelVest, DestructionSword',
    'Hes / 1 / Desolator, Sentinel, Antara'
    ])