function solution(n, s, a, b, fares) {
    const graph = Array.from({length: n+1}, ()=>[])
    for (const [c,d,f] of fares){
        graph[c].push([d,f]);
        graph[d].push([c,f]);
    }
    
    function getDist(start){
        const distance = Array(n+1).fill(Infinity)
        distance[start] = 0
        const queue = [[start,0]]
        while (queue.length > 0){
            queue.sort((a, b) => a[1] - b[1]);
            const [now, d] = queue.shift()
            if (distance[now] < d) continue;
            for (const [next, weight] of graph[now]){
                const cost = d + weight
                if (cost < distance[next]){
                    distance[next] = cost
                    queue.push([next, cost])
                }
            }
        }
        return distance
    }
    
    const fromS = getDist(s)
    const fromA = getDist(a)
    const fromB = getDist(b)
    
    let ans = Infinity;
    for (let i = 0; i <= n; i++){
        const total = fromS[i] + fromA[i] + fromB[i]
        ans = Math.min(total, ans)
    }
    
    return ans
}