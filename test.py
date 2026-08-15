num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 < num2:
    start = num1
    end = num2
else:
    start = num2
    end = num1
prime_numbers = []
for number in range(start, end + 1):
    if number >= 2:
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(number)
print("Prime numbers between", start, "and", end, "are:")
print(prime_numbers)
print("Total:", len(prime_numbers))



num1 = int(input("Enter first: "))
num2 = int(input("Enter second: "))
if num1 < num2:
    start = num1
    end = num2
else:
    start = num2
    end = num1
perfect_numbers = []
for n in range(start, end + 1):
    if n >= 1:
        divisor_sum = 0
        for i in range(1, n):
            if n % i == 0:
                divisor_sum = divisor_sum + i
        if divisor_sum == n:
            perfect_numbers.append(n)
print("Perfect numbers:", perfect_numbers)
print("Count:", len(perfect_numbers))


n = int(input("Enter number of terms: "))
fib = [1, 1]

for i in range(2, n):
    fib.append(fib[i - 1] + fib[i - 2])

print("Fibonacci:", fib)

colors = [["crimson", "pink"], ["red", "white"], ["blue", "gray"], ["green", "yellow"]]

for i in range(1, len(colors) + 1):
    print(colors[-i])


    num = int(input("Enter a number: "))
print("Starting number:", num)
while num != 1:
    if num % 2 == 0:
        num = num // 2
        print(num)
    else:
        num = (num * 3) + 1
        print(num)
print("Reached 1!")


num = int(input("Enter a number: "))
sum_of_divisors = 0
i = 1
while i < num:
    if num % i == 0:
        sum_of_divisors = sum_of_divisors + i
    i = i + 1
if sum_of_divisors == num:
    print(num, "is a perfect number!")
else:
    print(num, "is NOT a perfect number.")
    print("Sum of divisors:", sum_of_divisors)



    n = int(input("Enter the size of diamond: "))
i = 1
while i <= n:
    j = 1
    while j <= n - i:
        print(" ", end="")
        j = j + 1
    j = 1
    while j <= 2 * i - 1:
        if j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
        j = j + 1
    print()
    i = i + 1
i = n - 1
while i >= 1:
    j = 1
    while j <= n - i:
        print(" ", end="")
        j = j + 1
    j = 1
    while j <= 2 * i - 1:
        if j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
        j = j + 1
    print()
    i = i - 1