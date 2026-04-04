function solution(n, edge) {
    const graph = Array.from({length: n+1}, () => [])
    for (const [u,v] of edge){
        graph[u].push(v)
        graph[v].push(u)
    }
    const visited = Array(n+1).fill(false)
    const dists = Array(n+1).fill(0)
    visited[1] = true
    dists[1] = 0
    const queue = [[1,0]]
    
    while (queue.length > 0){
        const [now, d] = queue.shift()
        for (const neighbor of graph[now]){
            if (!visited[neighbor]){
                visited[neighbor] = true
                dists[neighbor] = d+1
                queue.push([neighbor, d+1])
            }
        }
    }
    
    return dists.filter(f=>f===Math.max(...dists)).length
}