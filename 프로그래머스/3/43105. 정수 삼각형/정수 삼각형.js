function solution(triangle) {
    const tLen = triangle.length
    
    for (let y = tLen-2; y >= 0; y--){
        for (let x = 0; x < y+1; x++){
            triangle[y][x] += Math.max(triangle[y+1][x+1], triangle[y+1][x])
        }
    }
    
    return triangle[0][0]
}