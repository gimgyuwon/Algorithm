function solution(progresses, speeds) {
    // 100 - 93 = 7 / 1 => 7
    // 100 - 30 = 70 / 30 => 3
    // 100 - 55 = 45 / 5 => 9
    // 7>3 => deployDate = 7, qty = 2
    // 9>7 => deployDate = 9, qty = 1
    
    let qty = 1
    let need = Math.ceil((100 - progresses[0])/speeds[0])
    let ans = []
    
    for (i=1; i<progresses.length; i++){
        const new_need = Math.ceil((100 - progresses[i])/speeds[i])
        if (need >= new_need){
            // console.log('기다림이 필요해. 배포 대기', need, '>', new_need)   
            qty++;
        } else {
            // console.log('다음 프로세스 완료 전까지 배포 가능. 배포 진행', need, '>', new_need)
            need = new_need
            ans.push(qty)
            qty = 1
        }
        // console.log('현재 ans', ans, '현재 qty', qty)
    }
    if (qty !== 0){
        ans.push(qty)
    }
    return ans;
}