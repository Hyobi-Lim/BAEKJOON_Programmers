function solution(k, score) {
    var answer = [];
    var num3=[]
    for(let i=0;i<score.length;i++){
        if(i<k){
            num3.push(score[i])
            answer.push(Math.min(...num3))
        }
        else{
            if(score[i]>Math.min(...num3)){
                num3[num3.indexOf(Math.min(...num3))]=score[i]
            }
            answer.push(Math.min(...num3))
        }
    }
    return answer;
}