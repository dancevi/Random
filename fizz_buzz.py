n = int(input())

for num in range(1, n+1):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzBuzz")
    elif num % 3 == 0 and num % 5 != 0:
        print("Fizz")
    elif num % 5 == 0 and num % 3 != 0:
        print("Buzz")
    else:
        print(num)
