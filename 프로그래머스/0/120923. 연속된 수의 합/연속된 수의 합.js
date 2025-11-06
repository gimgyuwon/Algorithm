function solution(num, total) {
    var answer = [];
    const md = Math.floor(total/num)
    if (num%2){
        // odd
        answer.push(md)
        for (i=1; i<=Math.floor(num/2); i++){
            answer.push(md-i)
            answer.push(md+i)
        }
    } else {
        // even
        answer.push(md);
        answer.push(md+1);
        for (i=1; i<Math.floor(num/2); i++){
            answer.push(md-i)
            answer.push(md+1+i)
        }
    }
    return answer.sort((a,b) => a-b);
}