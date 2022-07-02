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

val = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450

print(problem8(val))

