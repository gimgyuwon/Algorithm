function solution(array, commands) {
    const ans = []
    for (const [i,j,k] of commands){
        ans.push(array.slice(i-1,j).sort((a,b) => a-b)[k-1])
    }
    
    return ans
}