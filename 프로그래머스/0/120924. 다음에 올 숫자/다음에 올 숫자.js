function solution(common) {
    let ap = common[1] - common[0]
    let gp = Math.floor(common[1]/common[0])
    let is_ap = common[2]-common[1] === ap
    
    return is_ap ? common[common.length-1]+ap : common[common.length-1]*gp
}