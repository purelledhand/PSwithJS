let result = "";
let n;
let oddDigSum = 0;
let evenDigSum = 0;
let digits = [];

function main(input) {
    const lines = input.split("\n");

    for (let i = 0; i < Number(lines[0]); i++) {
        digits = [];
        result += `Case #${i + 1}:`;

        lines[i + 1].split(' ').forEach((d, Key) => {
            for (let i = 0; i < d; i++) {
                digits.push(Key+1);
            }

        });

        oddDigSum = 0, evenDigSum = 0;
        for (let j = 0; j < digits.length; j++) {
            // When i is even, position of digit is odd
            if (j % 2 == 0)
                oddDigSum += Number(digits[j]);
            else
                evenDigSum += Number(digits[j]);
        }

        if ((oddDigSum - evenDigSum) % 11 == 0) {
            result += " YES\n";
        } else {
            result += " NO\n";
        }
    }

    console.log(result);
}

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let stdin_input = "";

process.stdin.on("data", function (input) {
    stdin_input += input;
});

process.stdin.on("end", function () {
    main(stdin_input);
});