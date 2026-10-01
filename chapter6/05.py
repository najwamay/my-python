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
    
print("Result of sum: ", sum(5, 6, 7, 8))
print("Result of average: ", average(5, 6, 7, 8))
print("Result of max:", max(5, 6, 7, 8))
print("Result of min:", min(5, 6, 7, 8))

