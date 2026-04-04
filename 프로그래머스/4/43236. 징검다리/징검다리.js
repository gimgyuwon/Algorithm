function solution(distance, rocks, n) {
    const sortedR = rocks.sort((a,b) => a-b)
    let left = 1
    let right = distance
    let ans = 0
    
    while (left <= right){
        let mid = Math.floor((left+right)/2)
        let removeStone = 0
        let lastPos = 0
        
        for (let i = 0 ; i < sortedR.length; i++){
            if (sortedR[i] - lastPos < mid) removeStone++
            else lastPos = sortedR[i]
        }
        
        if (distance - lastPos < mid) {
            removeStone++;
        }
        
        if (removeStone > n){
            right = mid - 1
        } else {
            ans = mid
            left = mid + 1
        }
    }
    
    return ans
}