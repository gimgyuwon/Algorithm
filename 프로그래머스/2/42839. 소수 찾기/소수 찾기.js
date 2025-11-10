function solution(numbers) {
    const max = numbers.length
    
    let allCase = new Set()
    let isVisited = Array(max).fill(false)
    
    function combination(nowNum){
        if (nowNum.length > 0){
            allCase.add(Number(nowNum))
        }
        for (let i=0; i<max; i++){
            if (!isVisited[i]){
                isVisited[i] = true
                combination(nowNum + numbers[i])
                isVisited[i] = false
            }
        }
    }
    
    combination('')
    
    const max_num = Math.max(...allCase)
    
    const isPrime = Array(max_num+1).fill(true);
    
    if (max_num > 0){
        isPrime[0] = false
    }
    if (max_num > 1){
        isPrime[1] = false
    }
    
    for (let i=2; i*i<=max_num; i++){
        if (isPrime[i] == true){
            for (j=i*i; j<=max_num; j+=i){
                isPrime[j] = false
            }
        }
    }
    
    
    let ans = 0
    
    for (const p of allCase){
        // console.log('p', p, 'isPrime', isPrime[p-1])
        if (isPrime[p]){
            ans++;
        }
    }
    
    
    
    return ans;
}