let citationTable;
let result = "";
function main(input) {
    const lines = input.split("\n");

    for(let i=0;i<lines[0];i++) {
        citationTable = Array.apply(null, new Array(Number(lines[2*i+1]))).map(e => 0);
        result+=`Case #${i+1}:`;

        const citations = lines[2*(i+1)].split(" ");
        let hIndex = 0;
        let hPaper = 0;

        citations.map((p, key) => {
            //console.log(key);
            for (let i = 0; i < Number(p); i++) {
                if (i >= citationTable.length) break;
                citationTable[i]++;
            }

            //console.log(citationTable);

            if (citationTable[hIndex] == hIndex + 1) {
                hIndex++;
            }

            result+=` ${hIndex}`;
        });

        result+= "\n";
    }

    console.log(result);
}

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let stdin_input = "";

process.stdin.on("data", function(input) {
    stdin_input += input;
});

process.stdin.on("end", function() {
    main(stdin_input);
});