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

nums = [
    [8, 2, 22, 97, 38, 15, 00, 40, 00, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
    [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 00],
    [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
    [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
    [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
    [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
    [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
    [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
    [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
    [21, 36, 23, 9, 75, 00, 76, 44, 20, 45, 35, 14, 00, 61, 33, 97, 34, 31, 33, 95],
    [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
    [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 00, 17, 54, 24, 36, 29, 85, 57],
    [86, 56, 00, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
    [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
    [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
    [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
    [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
    [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
    [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
    [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48],
]

print(problem11(nums))
