function solution(triangle) {
    const tLen = triangle.length
    for (let i = tLen-2; i >= 0; i--){
        for (let j = 0; j < i+1; j++){
            triangle[i][j] += Math.max(triangle[i+1][j], triangle[i+1][j+1])
        }
    }
    return triangle[0][0]
}