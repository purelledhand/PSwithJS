function solution(s) {
    let recoveredTuple = [];
    let tupleSet = s.split("{").filter(r=>r!=='');
    tupleSet = tupleSet.map(i => {
        return i.replace('}','').replace('}','').split(',').filter(r=>r!=='');
    });


    for(let i=1;i<=tupleSet.length;i++) {
        tupleSet.find(set => set.length===i).forEach(e=>{
            if(recoveredTuple.indexOf(Number(e))<0) {
                recoveredTuple.push(Number(e));
                return;
            }
        });

    }

    console.log(tupleSet);
    console.log(recoveredTuple);
}

solution("{{2},{2,1},{2,1,3},{2,1,3,4}}");
solution("{{1,2,3},{2,1},{1,2,4,3},{2}}");