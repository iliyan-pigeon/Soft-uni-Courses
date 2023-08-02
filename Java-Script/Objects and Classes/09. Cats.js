function catsClass(data){
    class Cat{
        constructor(name, age){
            this.name = name
            this.age = age
        }

        meow(){
            console.log(`${this.name}, age ${this.age} says Meow`);
        }
    }

    let cats = []
    for (const info of data){
        let theInfo = info.split(" ")
        let catName = theInfo[0]
        let catAge = theInfo[1]
        cats.push(new Cat(catName, catAge))
    }

    for (const cat of cats){
        cat.meow()
    }
}