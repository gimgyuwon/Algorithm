function solution(s){
    let cnt = 0
    
    for (const gwalho of s){
        if (cnt < 0){
            return false
        }
        
        if (gwalho == '('){
            cnt++
        } else {
            cnt--
        }
    }
    
    return cnt == 0 ? true : false;
}