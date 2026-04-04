function solution(begin, target, words) {
    function diffCnt(w1, w2){
        let cnt = 0
        for (let i = 0; i < w1.length; i++){
            if (w1[i] !== w2[i]) cnt++
        }
        return cnt
    }
    let head = 0
    // word, step
    const queue = [[begin, 0]]
    const visited = Array(words.length-1).fill(0)
    
    while (head < queue.length){
        const [word, step] = queue[head++]
        if (word === target) return step;
        
        for (let i = 0; i < words.length; i++){
            if (!visited[i] && diffCnt(word, words[i]) === 1) {
                visited[i] = 1
                queue.push([words[i], step+1])
            }
        }
    }
    return 0
}