function solution(maps) {
    const n = maps.length
    const m = maps[0].length
    
    const dx = [0, 0, -1, 1]
    const dy = [-1, 1, 0, 0]
    
    let head = 0
    const queue = [[0,0,1]]
    maps[0][0] = 0
    
    while (head < queue.length){
        const [y,x,dist] = queue[head++]
        if (y===n-1 && x===m-1) return dist;
        
        for (let i = 0; i < 4; i++){
            let ny = y + dy[i]
            let nx = x + dx[i]
            
            if (ny>=0 && nx >=0 && ny<n && nx<m && maps[ny][nx]===1){
                maps[ny][nx] = 0
                queue.push([ny,nx,dist+1])
            }
        }
    }
    
    return -1
    
}