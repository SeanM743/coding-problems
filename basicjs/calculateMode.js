const calculate_mode = (array) => {
    const occurrences = {}
    const answer = []
    let maxVal = 0


    for(let i = 0; i < array.length; i++){
        let arrayElement = array[i]
        if(occurrences[arrayElement]){
            occurrences[arrayElement] +=1
            if(occurrences[arrayElement] > maxVal) {
                maxVal = occurrences[arrayElement]
            }
        }
        else{
            occurrences[arrayElement] =1
        }

        for (key in occurrences){
            if(occurrences[key] == maxVal){
                answer.push(key)
            }
        }
    }

    
    return answer
}
console.log(calculate_mode([1,2,3,3]))