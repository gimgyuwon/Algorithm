function solution(priorities, location) {
    const q = priorities.map((p, i)=>({priority: p, idx: i}))
    let seq = 0
    
    while (q.length>0){
        const maxPriority = Math.max(...q.map(item=>item.priority))
        const current = q.shift()
        
        if (current.priority < maxPriority){
            q.push(current)
        } else {
            seq++
            if (current.idx == location){
                return seq
            }
        }
    }
}