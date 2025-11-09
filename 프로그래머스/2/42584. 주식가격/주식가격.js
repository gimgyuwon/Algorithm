function solution(prices) {
    const len = prices.length
    const ans_lst = []
    
    for (let i=0; i<len; i++){
        let time = 0
        const now = prices[i]
        
        for (let j=i+1; j<len; j++){
            const next = prices[j]
            time++;
            if (now > next){
                break;
            }
        }
        ans_lst.push(time);
    }
    return ans_lst;
}