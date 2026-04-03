function solution(participant, completion) {
    const pMap = new Map()
    for (const name of participant){
        pMap.set(name, (pMap.get(name) || 0) + 1)
    }
    
    for (const name of completion){
        pMap.set(name, pMap.get(name) -1)
    }
    
    for (const [name, cnt] of pMap){
        if (cnt > 0){
            return name
        }
    }
}