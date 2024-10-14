function solution(n, arr1, arr2) {
    var answer = [];
    for(let i=0;i<arr1.length;i++){
        let str=''
        for(let j=0;j<n;j++){
            if(arr1[i].toString(2)[arr1[i].toString(2).length-j-1]==1)
                str='#'+str
            else if(arr2[i].toString(2)[arr2[i].toString(2).length-j-1]==1)
                str='#'+str
            else
                str=' '+str
        }
        answer.push(str)
    }
    return answer;
}