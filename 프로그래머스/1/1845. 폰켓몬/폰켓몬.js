function solution(nums) {
    const pMap = new Map()
    const pCap = nums.length/2
    
    for (const ponkemon of nums){
        pMap.set(ponkemon, (pMap.get(ponkemon) || 0) +1)
    }
    
    const pSize = pMap.size
    
    return pSize >= pCap ? pCap : pSize
}