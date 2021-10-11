def FizzBuzz(val):
    if (val == 1):
        return '1'
    elif (val == 2):
        return '2'
    elif (val % 3 == 0 and val % 5 == 0):
        return 'FizzBuzz'
    elif (val % 3 == 0):
        return 'Fizz'
    elif (val % 5 == 0):
        return 'Buzz'