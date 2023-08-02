function employeesPersonalNumbers(employeesData){
    Object.entries(
        employeesData.reduce((employeesData, employee) =>{
            employeesData[employee] = employee.length
            return employeesData
        }, {})
    ).forEach(([employee, length]) =>{
        console.log(`Name: ${employee} -- Personal Number: ${length}`);
    })
}