from module.add import double_number


def fizzbuzz(num):
    if num % 15 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)


print(double_number(1))
print(fizzbuzz(3))
