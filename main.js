const problem1 = (num) => {
    let sum = 0;

    for (i = 0; i < num; i++) {
        if (i % 3 === 0) {
            sum += i;
            continue;
        }

        if (i % 5 === 0) {
            sum += i;
            continue;
        }
        continue;
    }

    return sum;
}

const problem2 = (max) => {
    let isBelowFourMillion = true;

    const arr = [1, 2];
    let sum = 2;
    let firstIndex = 0;
    while (true) {
        const num = arr[firstIndex] + arr[firstIndex + 1]
        if (num > max) {
            break;
        }

        if (num % 2 === 0) {
            sum += num;
        }

        arr.push(num);
        firstIndex++;
    }

    return sum;
}

const problem3 = (num) => {
    const primeFactors = [2];

    let n = 2;
    while (num > 1) {
        if (num % n === 0) {
            primeFactors.push(n);
            num /= n;
            continue;
        }

        n++;
        continue;
    }

    return primeFactors.reduce((a, b) => Math.max(a, b))
}

const problem4 = () => {
    let largestProduct = 0;
    for (i = 100; i < 1000; i++) {
        for (n = 100; n < 1000; n ++) {
            const product = (i * n).toString();
            if (product.length % 2 !== 0) {
                continue;
            }

            const separator = product.length / 2;
            const copy = product;
            const first = copy.toString().slice(0, separator);
            const second = [...copy.toString().slice(separator, product.length)].reverse().join('');

            if (first !== second) {
                 continue;
            }

            if (largestProduct > product) {
                continue;
            }

            largestProduct = product;
        }
    }

    return largestProduct;
}

const problem5 = (num) => {
    const nums = [];
    let fact = 1;
    for (i = 1; i <= num; i++) {
        fact *= i;
    }

    for (i = num; i <= fact; i++) {
        for (n = 1; n <= num; n++) {
            if (i % n !== 0) {
                break;
            }

            if (n === num) {
                return i;
            }
        }
    }
}

const problem6 = (num) => {
    const nums = Array.from({ length: num }, (v, i) => i + 1);
    const sumOfTheSquares = nums.reduce((p, c) => p + Math.pow(c, 2));
    const squareOfTheSum = Math.pow(nums.reduce((p, c) => p + c), 2)
    return squareOfTheSum - sumOfTheSquares;
}

const problem7 = (num) => {
    const primes = [];
    let target = 2;
    while (primes.length <= num) {
        for (i = 2; i <= target; i++) {
             if (i === target) {
                primes.push(target);
                break;
            }

            if (target % i === 0) {
                break;
            }
        }
        target++;
    }
    return primes[num - 1];
}

const isPrime = (n) => {
    if (n === 1) return false;
    if (n < 4) return true;
    
    if (n % 2 === 0) return false;
    if (n < 9) return true; 
    if (n % 3 === 0) return false;

    const root = Math.floor(Math.sqrt(n));
    let f = 5;
    while (f <= root) {
        if (n % f === 0) {
            return false;
        }

        if (n % (f + 2) === 0) {
            return false;
        }
        f += 6;
    }
    return true;
}

const problem7_2 = (num) => {
    let count = 1;
    let candidate = 1;

    while (true) {
        candidate += 2;
        if (isPrime(candidate)) {
            count += 1;
        }

        if (count === num) {
            return candidate;
        }
    }
}

const problem8Nums = "73167176531330624919225119674426574742355349194934"+
"96983520312774506326239578318016984801869478851843"+
"85861560789112949495459501737958331952853208805511"+
"12540698747158523863050715693290963295227443043557"+
"66896648950445244523161731856403098711121722383113"+
"62229893423380308135336276614282806444486645238749"+
"30358907296290491560440772390713810515859307960866"+
"70172427121883998797908792274921901699720888093776"+
"65727333001053367881220235421809751254540594752243"+
"52584907711670556013604839586446706324415722155397"+
"53697817977846174064955149290862569321978468622482"+
"83972241375657056057490261407972968652414535100474"+
"82166370484403199890008895243450658541227588666881"+
"16427171479924442928230863465674813919123162824586"+
"17866458359124566529476545682848912883142607690042"+
"24219022671055626321111109370544217506941658960408"+
"07198403850962455444362981230987879927244284909188"+
"84580156166097919133875499200524063689912560717606"+
"05886116467109405077541002256983155200055935729725"+
"71636269561882670428252483600823257530420752963450";

const problem8 = (num) => {
    const nums = Array.from(problem8Nums, v => Number(v));

    let largest = 0;
    for (i = 0; i <= nums.length - num; i++) {
        const product = nums.slice(i, i + num).reduce((p, c) => p * c);
        if (product < largest) {
            continue;
        }
        largest = product;
    }
    return largest;
}

const problem9 = (num) => {
    for (i = 1; i <= num; i++) {
        for (n = 1; n <= num - i; n++) {
            const c = Math.sqrt(Math.pow(i, 2) + Math.pow(n, 2))
            if (!isFinite(c)) {
                continue;
            }

            if (i + n + c === num) {
                return i * n * c;
            }
        }
    }
}

const problem10 = (num) => {
    const primes = [];
    let target = 2;

    while (target <= num) {
        for (i = 2; i <= target; i++) {
            if (target === i) {
                primes.push(target);
                target++;
                break;
            }

            if (target % i === 0) {
                target++;
                break;
            }
        }
    }

    return primes.reduce((p, c) => p + c);
}

const problem10_2 = (num) => {
    const sievebound = (num - 1) / 2;
    const sieve = Array.from({ length: sievebound }, (v, k) => false);
    const crosslimit = (Math.sqrt(num) - 1) / 2;
    for (i = 1; i <= crosslimit; i++) {
        if (!sieve[i]) {
            for (j = 2*i*(i+1); j <= sievebound; j+=2*i+1) {
                sieve[j] = true;
            }
        }
    }
    let sum = 2;
    for (i = 1; i <= sievebound; i++) {
        if (!sieve[i]) {
            sum += 2*i+1
        }
    }
    return sum;
}

const problem10_3 = (num) => {
    const sieve = Array.from({ length: num }, (v, k) => false);
    sieve[0] = true;
    for (let i = 4 - 1; i < num; i+=2) {
        sieve[i] = true;
    }
    for (let n = 3 - 1; n < num; n+=2) {
        if (!sieve[n]) {
            for (let r = Math.pow(n + 1, 2) - 1; r <= num; r += 2*(n + 1)) {
                sieve[r] = true;
            }
        }
    }
    let sum = 0
    for (let i = 2 - 1; i < num; i++) {
        if (!sieve[i]) {
            sum += i+1;
        }
    }
    return sum;
}

const problem11_grid = [
[08, 02, 22, 97, 38, 15, 00, 40, 00, 75, 04, 05, 07, 78, 52, 12, 50, 77, 91, 08,],
[49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 04, 56, 62, 00,],
[81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 03, 49, 13, 36, 65,],
[52, 70, 95, 23, 04, 60, 11, 42, 69, 24, 68, 56, 01, 32, 56, 71, 37, 02, 36, 91,],
[22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80,],
[24, 47, 32, 60, 99, 03, 45, 02, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50,],
[32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70,],
[67, 26, 20, 68, 02, 62, 12, 20, 95, 63, 94, 39, 63, 08, 40, 91, 66, 49, 94, 21,],
[24, 55, 58, 05, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72,],
[21, 36, 23, 09, 75, 00, 76, 44, 20, 45, 35, 14, 00, 61, 33, 97, 34, 31, 33, 95,],
[78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 03, 80, 04, 62, 16, 14, 09, 53, 56, 92,],
[16, 39, 05, 42, 96, 35, 31, 47, 55, 58, 88, 24, 00, 17, 54, 24, 36, 29, 85, 57,],
[86, 56, 00, 48, 35, 71, 89, 07, 05, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58,],
[19, 80, 81, 68, 05, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 04, 89, 55, 40,],
[04, 52, 08, 83, 97, 35, 99, 16, 07, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66,],
[88, 36, 68, 87, 57, 62, 20, 72, 03, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69,],
[04, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 08, 46, 29, 32, 40, 62, 76, 36,],
[20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 04, 36, 16,],
[20, 73, 35, 29, 78, 31, 90, 01, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 05, 54,],
[01, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 01, 89, 19, 67, 48,],
];

const problem11 = () => {
    let largest = 0;
    let largestArr = [];
    const products = [];

    // right left
    problem11_grid.forEach(arr => {
        for (i = 0; i < arr.length - 3; i++) {
            const rightProdcut = arr.slice(i, i+4).reduce((p, c) => p * c);
            products.push(rightProdcut);
        }
    })

    // up down
    for (i = 0; i < 20; i++) {
        for (n = 0; n < 20 - 3; n++) {
            const getProduct = (arr) => {
                return arr[n][i] * arr[n + 1][i] * arr[n + 2][i] * arr[n + 3][i];
            }
            const downProduct = getProduct(problem11_grid);
            products.push(downProduct);
        }
    }

    // diagonal
    for (i = 0; i < 20 - 3; i++) {
        for (n = 0; n < 20 - 3; n++) {
            const getProduct = (arr) => {
                return arr[i][n] * arr[i + 1][n + 1] * arr[i + 2][n + 2] * arr[i + 3][n + 3];
            }
            const downDiagonal = getProduct(problem11_grid);
            products.push(downDiagonal);
    
            const upDiagonal = getProduct([...problem11_grid].reverse().map(v => v.reverse()));
            products.push(upDiagonal);
        }

    }

    return Math.max(...products);
}

const problem12 = () => {

    let base = 1;
    while (true) {
        let num = 0;
        for (i = 1; i <= base; i++) {
            num += i;
        }
    
        let divisor = [];
        for (i = 1; i <= num; i++) {
            if (num % i === 0) {
                divisor.push(i);
            }
        }
    
        if (divisor.length > 5) {
            return divisor
        }
        divisor = [];
        base++;
    }



}

const problem12_2 = () => {
    let triangleNum = 1;
    let a = 1;
    let count = 1;

    while (count <= 6) {
        count = 0;
        a++;
        triangleNum += a;

        const ttx = Math.sqrt(triangleNum);
        for (i = 1; i <= ttx; i++) {
            if (triangleNum % i === 0) {
                count += 2;
            }
        }
        if (triangleNum === Math.pow(ttx, 2)) {
            count--;
        }
    }
    return triangleNum;
}

const problem12_3 = () => {
    let t = 1;
    let a = 1;
    let cnt = 0;
    var tt, i, exponent;

    let primearray =[];
    for (i = 1; i <= 50000000; i++) {
        if (isPrime(i)) {
            primearray.push(i);
        }
    }

    while (cnt <= 500) {
        cnt = 1;
        a += 1;
        t += a;
        tt = t;
        for (i = 0; i < primearray.slice(-1)[0]; i++){
            if (primearray[i] * primearray[i] > tt) {
                cnt *= 2;
                break;
            }
            exponent = 1;
            while (tt % primearray[i] === 0) {
                exponent++;
                tt /= primearray[i];
            }
            if (exponent > 1) {
                cnt *= exponent;
            }
            if (tt === 1) {
                break;
            }
        }
    }
    return t;
}

const problem14 = () => {
    let largestArr = [];
    let largestTarget = 0;

    for (n = 1000000; n > 1; n--) {
        const arr = []
        let target = n;

        while (target > 1) {
            if (target % 2 === 0) {
                target /= 2
                arr.push(target)
                continue;
            }

            target = 3 * target + 1
            arr.push(target);
        }

        if (largestArr.length < arr.length) {
            largestArr = arr;
            largestTarget = n;
        }
    }
    return largestTarget;
}

const problem14_2 = (num) => {
    const values = Array.from({length: num}, (v, k) => undefined);
    values[2] = 1;
    const countChanin = (n) => {
        if (values[n] !== undefined) {
            return values[n];
        }

        if (n % 2 === 0) {
            values[n] = 1 + countChanin(n/2);
        }
        else {
            values[n] = 2 + countChanin((3 * n + 1) / 2)
        }
        return values[n];
    }

    let longestChain = 0;
    let answer = -1;

    for (i = num / 2; i <= num - 1; i++) {
        const n = countChanin(i)
        if (n > longestChain) {
            longestChain = n;
            answer = i;
        }
    }
    return answer;
}

const problem15 = () => { 
    const countRoute = (m, n) => {
        if (m === 0 || n === 0) {
            return 1;
        }
        return countRoute(m, n - 1) + countRoute(m - 1, n);
    }

    return countRoute(2, 2);
}

const problem15_2 = () => {
    const countRoute = (n) => {
        let result = 1;

        for (i = 1; i < n; i++) {
            result *= (n + i) / i;
        }

        return result;
    }

    return (countRoute(20))
}

const problem16 = (n) => {
    const pow = Array.from(String(BigInt(Math.pow(2, n))), Number);

    return pow.reduce((p, c) => p + Math.trunc(c));
}

const problem18_triangle = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]

const arr = [
[3],
[7, 4],
[2, 4, 6],
[8, 5, 9, 3],
]

const problem18 = (n) => {
    let index = 0;
    const result = problem18_triangle.reduce((p, c) => {
        if (c[index] < c[index + 1]) {
            index++;
        }
        return p + c[index];
    }, 0)

    return result;
}

const problem19 = () => {
    let sundayCount = 0;

    for (y = 1901; y <= 2000; y++) {
        for (m = 1; m <= 12; m++) {
            const date = new Date(y, m, 1);
            if (date.getDay() === 0) {
                sundayCount++
            }
        }
    }
    return sundayCount;
}

const problem20 = (n) => {
    const arr = Array.from({length: n}, (v, k) => BigInt(k + 1));
    const num = BigInt(arr.reduce((p, v) => BigInt(p * v, 1)));
    const numArr = Array.from(num.toString(), Number);
    return numArr.reduce((p, c) => p + c);
}

const problem21 = (num) => {
    const index = Array.from({length: num + 1}, undefined);

    const getSumOfDivisors = (n) => {
        const arr = [1];
        if (index[n] !== undefined) {
            return index[n];
        }

        for (i = 2; i <= Math.sqrt(n); i++) {
            if (n % i === 0) {
                // 足す用
                arr.push(i);
                arr.push(n / i);
            }
        }

        index[n] = arr.reduce((p, c) => p + c);
        return index[n];
    }

    const amicables = [];

    for (i = 1; i <= num; i++) {
        const num1 = getSumOfDivisors(i);
        if (num1 <= i) {
            continue;
        }
        const num2 = getSumOfDivisors(num1);

        if (i === num2) {
            amicables.push(num1);
            amicables.push(num2);
        }
    }

    console.log(index);

    return amicables.reduce((p, c) => p + c);
}

const problem22 = () => {
    let score = 0;
    // file 読み込み
    const reader = new FileReader();
    const arrayBuffer = reader.readAsArrayBuffer("p022_names.txt");
    // scoreリスト
    const alphabet = "abcdefghijklmnopqrstuvwxyz"
    const alphabetArr = Array.from(alphabet);
    const getAlphabetScore = (index) => {
        return alphabet.charCodeAt(i);
    }

    const getAlphabetNum = (char) => {
        return alphabetArr.findIndex(v => v === c) + 1;
    }
    // score++
}

const problem23 = () => {
    const abundant = Array.from({length: 28124}, (v, k) => false);
    const getDivisorsSum = (num) => {
        let arr = [1];
        for (i = 2; i <= Math.sqrt(num); i++) {
            if (num % i !== 0) {
                continue;
            }
            arr.push(i);
            arr.push(num / i);
        }
        const distinctArray = [...new Set(arr)];
        return distinctArray.reduce((p, c) => p + c, 0);
    }

    abundant.forEach((v, i, a) => {
        if (i === 0) {
            return;
        }
        const sum = getDivisorsSum(i);
        if (i < sum) {
            a[i] = true;
        }
    })

    const twoAbundant = Array.from({length: 28124}, (v, k) => false);
    let sum = 0;
    let onlyAbundauntArray = [];
    abundant.forEach((v, i) => {
        if (v) {
            onlyAbundauntArray.push(i);
        }
    });

    onlyAbundauntArray.forEach(v => {
        onlyAbundauntArray.forEach(k => {
            twoAbundant[v + k] = true;
        })
    })

    twoAbundant.forEach((v, i) => {
        if (v) {
            return;
        }
        sum += i;
    })
    return sum;
}

const problem25 =() => {
    let index = BigInt(1);
    let before = BigInt(1);
    let now = BigInt(1);
    while (before.toString().length < 1000) {
        const after = BigInt(before + now);
        before = now;
        now = after;
        index++;
    }

    return index;
}

const problem26 = () => {
    const array = Array.from({length: 1001}, undefined)
    const getRecurrringCycle = (k) => {
        let m = 1;
        const mlist = [];
        let dec = "";

        // 余りを記録

        while (true) {
            // 同じ余りが存在するならreturn
            if (mlist.find(v => v === m)) {
                return m;
            }

            mlist.push(m);
            dec += Math.floor((m * 10) / k).toString();
            m = (m * 10) % k
            if (m === 0) {
                return m;
            }
        }
    }
    for (n = 2; n < 1000; n++) {
        let a = getRecurrringCycle(n);
        array[n] = a;
    }

    const max = array.reduce((p, c) => {
        if (c === undefined) {
            c = 0;
        }
        if (p < c) {
            return c;
        }
        return p;
    }, 0);

    return array.findIndex(v => v === max);
}

const problem27 = () => {
    let n = 0;
    while (true) {
        for (a = 1; a < 1000; a++) {
            for (b = 1; b <= 1000; b++) {
                const resultA = Math.pow(n, 2) + (a * n) + b
                const resultB = Math.pow(n, 2) - (a * n) + b
                const resultC = Math.pow(n, 2) + (a * n) - b
                const resultD = Math.pow(n, 2) - (a * n) - b

                const dividedA = resultA % n;
                const dividedB = resultB % n;
                const dividedC = resultC % n;
                const dividedD = resultD % n;

                if (dividedA === 0 || dividedB === 0 || dividedC === 0 || dividedD === 0) {
                    return a * b
                }
            }
        }
    }
}

class Point {
    x;
    y;
    number;

    constructor(x, y, number) {
        this.x = x;
        this.y = y;
        this.number = number;
    }
}

const problem28 = (n) => {
    const array = [1];
    let sqrt = 3;

    while (array[array.length - 1] < Math.pow(n, 2)) {
        let base = array[array.length - 1];
        for (i = 1; i <= 4; i++) {
            array.push(base + ((sqrt - 1) * i))
        }
        sqrt += 2;
    }

    return array.reduce((p, c) => p + c);
}

const problem29 = () => {
    const array = [];
    for (let a = 2; a <= 100; a++) {
        for (let b = 2; b <= 100; b++) {
            array.push(Math.pow(a, b))
        }
    }

    return new Set(array).size
}

const problem30 = () => {
    const pod = [];
    const powTarget =  Array.from({length: 10}, (_, k) => k);
    const pow = 5;
    const powed = powTarget.map(v => Math.pow(v, pow));

    let num = 2;
    while (num < 1000000) {
        const nums = num.toString().split('').map(Number);

        const calculated = nums.reduce((p, c) => p + powed[c], 0);

        if (calculated === num) {
            pod.push(num);
        }

        num++;
    }

    return pod.reduce((p, c) => p+c, 0);
}

console.log(problem30());

