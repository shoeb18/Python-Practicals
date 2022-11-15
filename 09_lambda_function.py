# lambda function
def x(a, b, c): return a+b+c
print(x(3, 2, 1))

# uses of lambda function
numbers = [2, 43, 54, 65, 76, 55]
odd_num = list(filter(lambda num: (num % 2 != 0), numbers))

print("The odd numbers are :", odd_num)