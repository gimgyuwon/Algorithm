function solution(array, commands) {
    let ans = []
    for (const cmd of commands){
        const filterLst = array.slice(cmd[0]-1, cmd[1]).sort((a,b) => a-b)
        ans.push(filterLst[cmd[2]-1])
        // console.log(filterLst, cmd, ans)
    }
    return ans
}