function solution(phone_book) {
    sortedPB = phone_book.map(String).sort()
    
    for (let i = 0; i < phone_book.length -1; i++){
        const a = sortedPB[i]
        const b = sortedPB[i+1]
        if (a == b.slice(0,a.length)){
            return false
        }
    }
    return true
}