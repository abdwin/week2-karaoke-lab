
def fizzbuzz(number):
    if number % 3 == 0: 
        if number % 5 == 0:
            return "fizzbuzz"
        else: return "fizz"
    elif number % 5 == 0:
        return "buzz"
    return number

