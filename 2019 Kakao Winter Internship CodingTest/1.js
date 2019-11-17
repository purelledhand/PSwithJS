function solution(board, moves) {
    let pop_index = [];
    let doll_entry;
    let bucket = [];
    let pop_count = 0;
    moves.map(i => {
        pop_index[1]=i-1;

        doll_entry = board.map(line=>line[i-1]).find(e=>e!==0);// 크레인의 pop


        pop_index[0]=board.map(line=>line[i-1]).findIndex(e=>e!==0);// 크레인의 pop index
        if(pop_index[0]=== -1) {
            return;
        }

        //console.log(`${pop_index} : ${doll_entry}`);
        board[pop_index[0]][pop_index[1]] = 0;

        if(bucket[bucket.length-1] === doll_entry){
            bucket.pop();
            pop_count += 2;
        }
        else (bucket.push(doll_entry));
    });

    console.log(pop_count);
}

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]);