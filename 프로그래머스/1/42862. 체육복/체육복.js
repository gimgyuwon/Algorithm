function solution(n, lost, reserve) {
    const can = Array(n).fill(1)
    const sortedR = reserve.sort((a,b) =>a-b)
    
    for (const l of lost){
        can[l-1] = 0
    }
    
    const reserved = []
    
    for (const r of sortedR){
        if (can[r-1] === 0){
            can[r-1] = 1
        } else {
            reserved.push(r)
        }
    }
    
    for (const r of reserved){
       if (can[r-2] === 0){
            can[r-2] = 1
        }
        else if (can[r] === 0){
            can[r] = 1
        }
    }
    return can.reduce((acc, c)=> acc + c, 0)
}