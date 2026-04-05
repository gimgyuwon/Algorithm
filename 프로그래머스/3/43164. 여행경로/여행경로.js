function solution(tickets) {
    const tLen = tickets.length
    const visited = Array(tLen).fill(false)
    tickets.sort((a,b) => a[1] < b[1] ? -1 : 1)
    
    function dfs(curr, path){
        if (path.length === tLen + 1){
            return path
        }
        for (let i = 0 ; i < tLen; i++){
            if (!visited[i] && tickets[i][0] === curr){
                visited[i] = true
                const res = dfs(tickets[i][1], [...path, tickets[i][1]])
                
                if (res) return res
                visited[i] = false
            }
        }
    }
    
    return dfs("ICN", ["ICN"])
}