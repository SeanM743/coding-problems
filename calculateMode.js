const calculate_mode = (array) => {
    const occurrences = {}
    const answer = []


    for(let i = 0; i < array.length; i++){
        let arrayElement = array[i]
        if(occurrences[arrayElement]){
            occurrences[arrayElement] +=1

        }
        else{
            occurrences[arrayElement] =1
        }
    }

    
    return occurrences
}
console.log(calculate_mode([1,2,3,3]))