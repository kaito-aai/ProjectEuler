from functools import reduce
from math import floor, sqrt
import string

def problem1(num):
    result = 0
    for n in range(num - 1, 0, -1):
        if (n % 3 == 0):
            result += n
            continue
        if (n % 5 == 0):
            result += n
            continue
    return result

def problem2(num1: int, num2: int, max: int):
    result = 0
    escape = 0
    while (num2 < max):
        if (num2 % 2 == 0):
            result += num2
        escape = num1
        num1 = num2
        num2 = escape + num1
    return result

def problem3(num: int):
    arr: list[int] = []
    for n in range(2, num, 1):
        if (num % n != 0):
            continue
        for f in arr:
            if (n % f == 0):
                return arr[-1]
        arr.append(n)
    return arr[-1]

def problem4(num: int):
    startNum = 10 ** num - 1
    num1 = startNum
    num2 = startNum
    result = 0
    for n1 in range(num1, 10 ** (num - 1), -1):
        for n2 in range(num2, 10 ** (num - 1), -1):
            target = n1 * n2
            targetString = str(target)
            firstHalf = targetString[0:num]
            reversedSecondHalf = targetString[num:len(targetString)][::-1]
            if (firstHalf != reversedSecondHalf):
                continue
            if (result > target):
                continue
            result = target
    return result

def problem5(num: int):
    used: list[int] = []
    result = 1

    for n in range(2, num+1, 1):
        tmp = n
        for u in used:
            if (tmp % u == 0):
                tmp = int(tmp / u)
        used.append(tmp)

    for n in used:
        result *= n
    return result

def problem6(num: int):
    factorialSum = 0
    sumForFactorial = 0
    for n in range(1, num+1, 1):
        sumForFactorial += n
        factorialSum+= n**2
    sumForFactorial **= 2
    return sumForFactorial - factorialSum

def problem7(num: int):
    primeNumbers: list[int] = []
    targetNum = 2
    while (len(primeNumbers) < num):
        for n in range(2, targetNum+1, 1):
            if (targetNum % n != 0):
                continue
            if (targetNum != n):
                targetNum+=1
                continue
            primeNumbers.append(targetNum)
            targetNum+=1
            continue
    return primeNumbers[-1]

def problem8(num: int):
    numList = [int(x) for x in list(str(num))]
    greatestProduct = 0
    index = 0
    length = 13
    while (len(numList) - index >= length):
        target = 1
        targetNumList: list[int] = []
        for n in range(index, index+length, 1):
            targetNumList.append(numList[n])
            target *= numList[n]
        if (greatestProduct < target):
            greatestProduct = target
        index+=1
    return greatestProduct

def problem9(num: int):
    for c in range(num - 2, 0, -1):
        cFact = c**2
        for a in range(num - c - 1, 0, -1):
            aFact = a**2
            if (cFact - aFact <= 0):
                continue
            bFloat = sqrt(cFact - aFact)
            if not (bFloat.is_integer()):
                continue
            b = int(bFloat)
            if (a + b + c != num):
                continue
            return a * b * c

def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    m = floor(sqrt(n)) + 1
    for p in range(3, m, 2):
        if n % p == 0:
            return False
    return True

def problem10(num: int):
    primes: list[int] = []

    for n in range(2, num+1, 1):
        if (isPrime(n)):
            primes.append(n)
    return sum(primes)

def problem11(nums: list[list[int]]):
    dimension1 = len(nums[0])
    dimension2 = len(nums)

    sideList = []
    for i in range(dimension2):
        for j in range(dimension1 -3):
            fNums = map(lambda k: nums[i][k], range(j, j+4))
            sideList += [reduce(lambda a,b: a* b, fNums)]

    topList = []
    for i in range(dimension2 - 3):
        for j in range(dimension1):
            fNums = map(lambda k: nums[k][j], range(i, i+4))
            topList += [reduce(lambda a,b: a * b, fNums)]
    
    leftNanameList = []
    for i in range(dimension2 - 3):
        for j in range(dimension1 - 3):
            fNums = map(lambda k: nums[i+k][j+k], range(4))
            leftNanameList += [reduce(lambda a,b: a * b, fNums)]
    
    rightNanameList = []
    for i in range(dimension2 - 3):
        for j in range(dimension1 - 1, dimension1 - 17, -1):
            fNums = map(lambda k: nums[i+k][j-k], range(4))
            rightNanameList += [reduce(lambda a,b: a * b, fNums)]
    
    return max(sideList + topList + leftNanameList + rightNanameList)

def getCountOfDivisorsOf(num):
    count = 0
    sqrtDouble = sqrt(num)
    sqrtInt = int(sqrtDouble)
    for i in range(1, sqrtInt+1):
        if num % i == 0:
            count+=2
    if sqrtDouble - sqrtInt == 0:
        count-=1
    return count

def problem12(so: int):
    num = 1
    triangleNumber = 0
    while True:
        triangleNumber += num
        num += 1
        if getCountOfDivisorsOf(triangleNumber) >= so:
            break
    return triangleNumber

nums = [
    [37107287533902102798797998220837590246510135740250],
    [46376937677490009712648124896970078050417018260538],
    [74324986199524741059474233309513058123726617309629],
    [91942213363574161572522430563301811072406154908250],
    [23067588207539346171171980310421047513778063246676],
    [89261670696623633820136378418383684178734361726757],
    [28112879812849979408065481931592621691275889832738],
    [44274228917432520321923589422876796487670272189318],
    [47451445736001306439091167216856844588711603153276],
    [70386486105843025439939619828917593665686757934951],
    [62176457141856560629502157223196586755079324193331],
    [64906352462741904929101432445813822663347944758178],
    [92575867718337217661963751590579239728245598838407],
    [58203565325359399008402633568948830189458628227828],
    [80181199384826282014278194139940567587151170094390],
    [35398664372827112653829987240784473053190104293586],
    [86515506006295864861532075273371959191420517255829],
    [71693888707715466499115593487603532921714970056938],
    [54370070576826684624621495650076471787294438377604],
    [53282654108756828443191190634694037855217779295145],
    [36123272525000296071075082563815656710885258350721],
    [45876576172410976447339110607218265236877223636045],
    [17423706905851860660448207621209813287860733969412],
    [81142660418086830619328460811191061556940512689692],
    [51934325451728388641918047049293215058642563049483],
    [62467221648435076201727918039944693004732956340691],
    [15732444386908125794514089057706229429197107928209],
    [55037687525678773091862540744969844508330393682126],
    [18336384825330154686196124348767681297534375946515],
    [80386287592878490201521685554828717201219257766954],
    [78182833757993103614740356856449095527097864797581],
    [16726320100436897842553539920931837441497806860984],
    [48403098129077791799088218795327364475675590848030],
    [87086987551392711854517078544161852424320693150332],
    [59959406895756536782107074926966537676326235447210],
    [69793950679652694742597709739166693763042633987085],
    [41052684708299085211399427365734116182760315001271],
    [65378607361501080857009149939512557028198746004375],
    [35829035317434717326932123578154982629742552737307],
    [94953759765105305946966067683156574377167401875275],
    [88902802571733229619176668713819931811048770190271],
    [25267680276078003013678680992525463401061632866526],
    [36270218540497705585629946580636237993140746255962],
    [24074486908231174977792365466257246923322810917141],
    [91430288197103288597806669760892938638285025333403],
    [34413065578016127815921815005561868836468420090470],
    [23053081172816430487623791969842487255036638784583],
    [11487696932154902810424020138335124462181441773470],
    [63783299490636259666498587618221225225512486764533],
    [67720186971698544312419572409913959008952310058822],
    [95548255300263520781532296796249481641953868218774],
    [76085327132285723110424803456124867697064507995236],
    [37774242535411291684276865538926205024910326572967],
    [23701913275725675285653248258265463092207058596522],
    [29798860272258331913126375147341994889534765745501],
    [18495701454879288984856827726077713721403798879715],
    [38298203783031473527721580348144513491373226651381],
    [34829543829199918180278916522431027392251122869539],
    [40957953066405232632538044100059654939159879593635],
    [29746152185502371307642255121183693803580388584903],
    [41698116222072977186158236678424689157993532961922],
    [62467957194401269043877107275048102390895523597457],
    [23189706772547915061505504953922979530901129967519],
    [86188088225875314529584099251203829009407770775672],
    [11306739708304724483816533873502340845647058077308],
    [82959174767140363198008187129011875491310547126581],
    [97623331044818386269515456334926366572897563400500],
    [42846280183517070527831839425882145521227251250327],
    [55121603546981200581762165212827652751691296897789],
    [32238195734329339946437501907836945765883352399886],
    [75506164965184775180738168837861091527357929701337],
    [62177842752192623401942399639168044983993173312731],
    [32924185707147349566916674687634660915035914677504],
    [99518671430235219628894890102423325116913619626622],
    [73267460800591547471830798392868535206946944540724],
    [76841822524674417161514036427982273348055556214818],
    [97142617910342598647204516893989422179826088076852],
    [87783646182799346313767754307809363333018982642090],
    [10848802521674670883215120185883543223812876952786],
    [71329612474782464538636993009049310363619763878039],
    [62184073572399794223406235393808339651327408011116],
    [66627891981488087797941876876144230030984490851411],
    [60661826293682836764744779239180335110989069790714],
    [85786944089552990653640447425576083659976645795096],
    [66024396409905389607120198219976047599490197230297],
    [64913982680032973156037120041377903785566085089252],
    [16730939319872750275468906903707539413042652315011],
    [94809377245048795150954100921645863754710598436791],
    [78639167021187492431995700641917969777599028300699],
    [15368713711936614952811305876380278410754449733078],
    [40789923115535562561142322423255033685442488917353],
    [44889911501440648020369068063960672322193204149535],
    [41503128880339536053299340368006977710650566631954],
    [81234880673210146739058568557934581403627822703280],
    [82616570773948327592232845941706525094512325230608],
    [22918802058777319719839450180888072429661980811197],
    [77158542502016545090413245809786882778948721859617],
    [72107838435069186155435662884062257473692284509516],
    [20849603980134001723930671666823555245252804609722],
    [53503534226472524250874054075591789781264330331690],
]

def problem13(nums: list[list[int]]):
    sum = 0
    for num in nums:
        sum += num[0]
    l = [int(x) for x in str(sum)]
    tenDigits =  int("".join(map(str, l[0:10])))
    return tenDigits

def problem14(num: int):
    target = num
    longestArr = []
    while target > 1:
        test = target
        arr = []
        arr.append(test)
        while test > 1:
            if test % 2 == 0:
                test = int(test / 2)
                arr.append(test)
                continue
            test = test * 3 + 1
            arr.append(test)
            continue
        if len(longestArr) < len(arr):
            longestArr = arr
        target -= 1
    return longestArr

def problem15(num: int):
    bunsi = 1
    bunbo = 1
    for n in range(num+1, num*2+1):
        bunsi *= n
        bunbo *= (n - num)
    return int(bunsi/bunbo)

def problem16(num: int):
    return sum([int(x) for x in str(2**num)])

nums = [
    [75],
    [95, 64,],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82,  47, 65,],
    [19, 1, 23,  75, 3 , 34],
    [88, 2, 77,  73, 7 , 63, 67],
    [99, 65, 4,  28, 6 , 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4,  68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98,  27, 23, 9 ,70 , 98, 73, 93, 38, 53, 60, 4, 23], 
]

def problem18(numsList: list[int]):
    for i in range(len(numsList)-1, 0, -1):
        for index, num in enumerate(nums[i - 1]):
            s = index if nums[i][index] > nums[i][index+1] else index+1
            nums[i - 1][index] += nums[i][s]
    return numsList[0][0]

def problem19():
    dow = ["Mon", "Tue", "Wed", "Thu", "Fry", "Sat", "Sun"]
    lastDow = "Mon"
    sunCount = 0

    def setLastWeek(w):
        nonlocal dow
        nonlocal lastDow
        lastDowIndex = dow.index(lastDow)
        dowFirst = dow[0:lastDowIndex+1]
        dowSecond = dow[lastDowIndex+1:]
        dowSecond.extend(dowFirst)
        dow = dowSecond
        lastDow = dow[w-1]

    for y in range(1901, 2001):
        for m in range(1, 13):
            if lastDow == "Sat":
                sunCount += 1
            if (m == 4 or m == 6 or m == 9 or m == 11):
                w = 30 % 7
                setLastWeek(w)
                continue
            if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
                w = 31 % 7
                setLastWeek(w)
                continue
            if (m == 2 and y % 4 == 0 and y % 400 != 0):
                w = 29 % 7
                setLastWeek(w)
                continue
            w = 28 % 7
            setLastWeek(w)
    return sunCount

def problem20(num: int):
    digits = 1
    for n in range(1,num+1):
        digits *= n
    digitsArr = [int(n) for n in str(digits)]
    result = 0
    for d in digitsArr:
        result += d
    return result

def getDivisorsSum(num: int):
    arr = [[1,num]]
    for n in range(2,int(num/2)+1):
        if (num % n == 0):
            divided = int(num/n)
            small = n if n <= divided else divided
            big = n if n != small else divided
            arr.append([small, big])
            continue
    numlis = list(map(list, set(map(tuple, arr))))
    return sum(map(sum, numlis)) - num

def problem21(num: int):
    arr = []
    for n in range(num, 0, -1):
        s = getDivisorsSum(n)
        if n == getDivisorsSum(s):
            if (s == n):
                continue
            arr.append(n)
            arr.append(s)
            continue
    print(set(arr))
    return sum(set(arr))

def problem22():
    score = 0
    arr = [c for c in string.ascii_uppercase]
    f = open('p022_names.txt', 'r', encoding='UTF-8')
    data = f.read().split(",")
    for i in range(0, len(data), 1):
        data[i] = data[i].strip('"')
    data.sort()

    for d in data:
        charScore = 0
        sortScore = data.index(d)+1 
        for c in d:
            charScore += arr.index(c)+1
        score += charScore*sortScore

    return score

print(problem22())
