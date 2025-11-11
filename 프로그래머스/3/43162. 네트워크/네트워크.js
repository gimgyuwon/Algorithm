function solution(n, computers) {
    let visited = Array(n).fill(false);
    let ans = 0
    
    function dfs(i){
        visited[i] = true;
        
        for (let j=0; j<n; j++){
            if (computers[i][j] === 1 && !visited[j]){
                dfs(j)
            }
        }
    }
    
    for (let k=0; k<n; k++){
        if (!visited[k]){
            ans++
            dfs(k)
        }
    }
    
    return ans
}