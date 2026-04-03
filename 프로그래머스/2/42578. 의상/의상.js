function solution(clothes) {
    const cMap = new Map()
    for (const [item, type] of clothes) {
        cMap.set(type, (cMap.get(type) || 0) + 1)
    }
    
    let ans = 1
    
    for (const [type, cnt] of cMap) {
        ans *= (cnt+1)
    }
    
    return ans-1
}