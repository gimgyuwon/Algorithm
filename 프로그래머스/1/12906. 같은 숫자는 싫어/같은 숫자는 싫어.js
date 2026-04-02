function solution(arr)
{   
    const ans = []
    
    for (const i of arr){
        if (ans[ans.length -1] !== i){
            ans.push(i);
        }
    }
    
    return ans;
}