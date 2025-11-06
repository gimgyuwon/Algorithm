function solution(phone_book) {
    let bookMap = new Map();
    for (const phone of phone_book){
        bookMap.set(phone, (bookMap.get(phone) || 0) +1)
    }
    
    for (const phone of phone_book){
        for (i=0; i<phone.length; i++){
            if (bookMap.has(phone.substring(0,i))){
                return false
            }
        }
    }
    
    return true
}