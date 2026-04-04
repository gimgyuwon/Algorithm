function solution(N, road, K) {
    const graph = Array.from({length: N+1}, ()=>[]);
    for (const [u,v,w] of road){
        graph[u].push([v,w])
        graph[v].push([u,w])
    }
    
    const dist = new Array(N+1).fill(Infinity)
    dist[1] = 0
    
    const queue = [[1,0]]
    while (queue.length > 0){
        queue.sort((a,b) => a[1] - b[1])
        const [now, d] = queue.shift()
        
        if (dist[now] < d) continue;
        
        for (const [next, weight] of graph[now]){
            const cost = d + weight;
            
            if (cost < dist[next]){
                dist[next] = cost
                queue.push([next, cost])
            }
        }
    }
    return dist.filter(d => d <= K).length;
}