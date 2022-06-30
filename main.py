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

print(problem2(1, 2, 4000000))