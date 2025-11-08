function solution(priorities, location) {
    let priorIdxList = []
    let rank = 1
    
    for (i=0; i<priorities.length; i++){
        priorIdxList.push([priorities[i], i])
    }
    
    while (priorIdxList.length > 0){
        const now = priorIdxList.shift()
        const maxInRest = Math.max(...priorIdxList.map((p) => p[0]))
        
        if (now[0] < maxInRest){
            priorIdxList.push(now)
        } else {
            if (now[1] === location){
                return rank;
            } else {
                rank++;
            }
        }
        
        // console.log('now', now, 'priorIdxList', priorIdxList, 'maxInRest', maxInRest, 'rank', rank)
    }
    return 0
}