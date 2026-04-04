function solution(rectangle, characterX, characterY, itemX, itemY) {
    const board = Array.from({length: 102}, () => Array(102).fill(0))
    const doubleRec = rectangle.map(r=> r.map(v => v*2))
    
    for (const [x1, y1, x2, y2] of doubleRec){
        for (let i = x1; i <= x2; i++){
            for (let j = y1; j <= y2; j++){
                if (i > x1 && i < x2 && j > y1 && j < y2){
                    board[i][j] = -1
                } else if (board[i][j] !== -1){
                    board[i][j] = 1
                }
            }
        }
    }
    
    const q = [[characterX*2, characterY*2, 0]]
    const visited = Array.from({length: 102}, () => Array(102).fill(false))
    visited[characterX*2][characterY*2] = true
    
    const dx = [0, 0, -1, 1]
    const dy = [-1, 1, 0, 0]
    let head = 0
    
    while (head < q.length){
        const [x, y, d] = q[head++]
        
        if (x === itemX*2 && y === itemY*2){
            return d/2
        }
        
        for (let i = 0; i < 4; i++){
            const nx = x + dx[i]
            const ny = y + dy[i]
            
            if (nx >= 0 && nx <= 100 && ny >= 0 && ny <= 100 && board[nx][ny] === 1 && !visited[nx][ny]){
                q.push([nx, ny, d+1])
                visited[nx][ny] = true
            }
        }
        
    }
}