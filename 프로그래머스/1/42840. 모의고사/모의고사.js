function solution(answers) {
    let first = [1, 2, 3, 4, 5]
    let second = [2, 1, 2, 3, 2, 4, 2, 5]
    let third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    let fScore = 0
    let sScore = 0
    let tScore = 0
    
    for (let i = 0; i < answers.length; i++){
        if (first[i%5] === answers[i]) fScore++
        if (second[i%8] === answers[i]) sScore++
        if (third[i%10] === answers[i]) tScore++
    }
    
    let winnerScore = Math.max(fScore, sScore, tScore)
    let ans = []
    
    if (winnerScore === fScore){
        ans.push(1)
    }
    if (winnerScore === sScore){
        ans.push(2)
    }
    if (winnerScore === tScore){
        ans.push(3)
    }
    
    return ans
}