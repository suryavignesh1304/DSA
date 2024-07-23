def is_sorted1(arr) -> bool:
    return set(arr) == set(sorted(arr))

arr={1,2,3,4,5}
print(is_sorted1(arr))

"""exponential"""
def exp_f(base_value, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base_value
    
    if exp % 2 == 0:
        h = exp_f(base_value, exp // 2)
        return h * h
    else:
        h = exp_f(base_value, exp // 2)
        return base_value *h*h


b = int(input("Enter base value:"))
e = int(input("Enter exponent value:"))
result = exp_f(b, e)
print(f"{b}^{e} = {result}")

"""Write a recursive function to convert a decimal number to its binary equivalent."""


# def decimal_to_binary(n):
#     binary = ''
#     while n > 0:
#         binary = str(n % 2) + binary
#         n = n // 2
#     print(binary)


def decimal_to_binary(n):
    if n > 1:
        decimal_to_binary(n // 2)
    print(n % 2, end='')

n = int(input("Enter a decimal number: "))
print("The binary representation of", n, "is: ", end='')
decimal_to_binary(n)


# def binary_to_decimal(n):
#     decimal = 0
#     i = 0
#     while n > 0:
#         decimal = decimal + (n % 10) * pow(2, i)
#         n = n // 10
#         i += 1
#         print(decimal)
        
# binary_to_decimal(10)

def binary_to_decimal_rec(n):
    if n > 0:
        return n % 10 + 2 * binary_to_decimal_rec(n // 10)
    else:
        return 0

n=input("\nenter the binary number:")
print(binary_to_decimal_rec(int(n)))

""""""
def two_sum(l, t):
    l.sort()
    for i, num in enumerate(l):
        c = t - num
        if c in l[i+1:]:
            return list(l).index(num), l.index(c)
    return -1, -1

l = list(map(int, input("Enter the list of numbers: ").split(" ")))
t = int(input("Enter the target sum: "))
result = two_sum(l, t)
if result != (-1, -1):
    print(f"The indices of the two numbers that add up to {t} are {result[0]} and {result[1]}.")
else:
    print("No two numbers in the list add up to the target sum.")