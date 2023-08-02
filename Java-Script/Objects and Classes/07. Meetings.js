function meetingManager(meetingRequests){
    let meetings = {}
    
    for (const request of meetingRequests){
        let requestInfo = request.split(" ")
        let weekDay = requestInfo[0]
        let personName = requestInfo[1]

        if (weekDay in meetings){
            console.log(`Conflict on ${weekDay}!`)
        }else{
            meetings[weekDay] = personName
            console.log(`Scheduled for ${weekDay}`)
        }
    }

    for (const key of Object.keys(meetings)){
        console.log(`${key} -> ${meetings[key]}`)
    }
}