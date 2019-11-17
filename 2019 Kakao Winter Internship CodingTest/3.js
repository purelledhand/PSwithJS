function factorial(n) {
    if (n == 1 || n == 0) return 1;
    return n * factorial(n - 1);
}

function combination(n, r) {
    if (n == r) return 1;
    let a = factorial(n);
    let b = factorial(r);
    let c = factorial(Math.abs(n - r));
    return a / (b * c);
}

function binomial(n, k) {
    if ((typeof n !== 'number') || (typeof k !== 'number'))
        return false;
    var coeff = 1;
    for (var x = n - k + 1; x <= n; x++) coeff *= x;
    for (x = 1; x <= k; x++) coeff /= x;
    return coeff;
}

function solution(user_id, banned_id) {
    let pattern;
    let patDup = {};
    let duplicate_count = 0;

    banned_id.forEach(e => {
        let dupCnt = banned_id.filter(r => r === e).length;
        patDup[banned_id.indexOf(e)] = dupCnt;
    });

    const match = banned_id.map(e => {
        let len = e.length;
        pattern = e.replace(/\*/g, '[a-z0-9]{1}');
        let reg = new RegExp(pattern);

        return user_id.filter(e => {
            return reg.test(e) && e.length === len;
        });
    });

    let sum = 1;

    for (let i = 0; i < banned_id.length; i++) {
        if (patDup[i] === undefined) continue;
        sum *= combination(match[i].length, patDup[i]);
    }
    console.log(match);

    for (let i = 0; i < banned_id.length; i++) {

        match[i].forEach(r => {
            for (let i = 0; i < match.length; i++) {
                if (patDup[i] === undefined) continue;
                for (let j = 0; j < match[i].length; j++) {
                    if (match[i][j] === r) duplicate_count++;
                }
            }
            duplicate_count--;
        });
    }

    console.log(sum - duplicate_count / 2);
}

solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]);
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]);
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]);