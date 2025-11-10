function solution(sizes) {
    let garo = []
    let sero = []
    
    for (const sz of sizes){
        const sortedSz = sz.sort((a, b) => b-a)
        garo.push(sortedSz[0])
        sero.push(sortedSz[1])
    }
    
    const ans = Math.max(...garo) * Math.max(...sero)
    
    return ans;
}