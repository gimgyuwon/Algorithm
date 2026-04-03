function solution(prices) {
    let time = 0
    const ans = []
    
    for (let i = 0; i < prices.length; i++){
        let time = 0
        for (let j = i+1; j< prices.length; j++){
            time++
            if (prices[i] > prices[j]){
                break
            }
        }
        ans.push(time)
    }
    return ans
}