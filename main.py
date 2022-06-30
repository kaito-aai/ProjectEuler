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

print(problem1(1000))