from functools import reduce
from math import floor, sqrt

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

print(problem12(500))