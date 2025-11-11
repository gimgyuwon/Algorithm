function solution(participant, completion) {
    const pMap = new Map();
    
    for (const p of participant){
        pMap.set(p, (pMap.get(p) || 0) + 1)
    }
    
    // console.log(pMap)
    
    for (const p of completion){
        pMap.set(p, (pMap.get(p) || 0) - 1)
    }
    
    for (const [k,v] of pMap){
        if (v !== 0){
            return k
        }
    }
}