def sum(*args):
    result = 0
    for number in args:
        result += number
    return result

def average(*args):
    if not args:
        return 0

    total = sum(*args)
    result = total / len(args)
    return result

def max(*args):
    if not args:
        print("Result of max: None")
        return None

    highest = args[0]
    for number in args[1:]:
        if number > highest:
            highest = number
    return highest

def min(*args):
    if not args:
        print("Result of min: None")
        return None

    lowest = args[0]
    for number in args[1:]:
        if number < lowest:
            lowest = number
    return lowest

print("Data A")
print("Result of sum: ", sum(5, 10, 4, 9, 30, 16, 2, 11))
print("Result of average: ", average(5, 10, 4, 9, 30, 16, 2, 11))
print("Result of max:", max(5, 10, 4, 9, 30, 16, 2, 11))
print("Result of min:", min(5, 10, 4, 9, 30, 16, 2, 11))

print("Data B")
print("Result of sum: ", sum(81, 98, 12, 83, 45, 77, 69, 30, 56))
print("Result of average: ", average(81, 98, 12, 83, 45, 77, 69, 30, 56))
print("Result of max:", max(81, 98, 12, 83, 45, 77, 69, 30, 56))
print("Result of min:", min(81, 98, 12, 83, 45, 77, 69, 30, 56))


