function solution(n, times) {
    let left = 1;
    let right = Math.max(...times) * n;
    let ans = right
    
    while (left <= right){
        let mid = Math.floor((left+right)/2)
        let cap = 0
        
        for (const t of times){
            cap += Math.floor(mid/t)
        }
        
        if (cap >= n){
            ans = mid
            right = mid - 1
        }
        else {
            left = mid + 1
        }
    }
    
    return ans
}