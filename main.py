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

print(problem4(3))