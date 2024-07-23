1.# def count_digits(numb):
#     numb_str = str(numb)
#     count = 0
#     for i in numb_str:
#         if i.isdigit():
#             count += 1
    
#     return count

# n = int(input(""))
#print(f"The number of digits in {n} is {count_digits(n)}")



2.# n = int(input(""))
# n_str=str(n)

# count=0
# for i in n_str:
#     if i.isdigit():
#         count+=1

# print(f"The number of digits in {n} is {count}")


# 3.import math

# def count_digits_2(num):
#     return math.floor(math.log10(num))
# n=int(input(""))
# print(count_digits_2(n))


#palindrome
# def palindrome_num(num):
#     return str(num) == "".join(reversed(str(num)))

# n = int(input("Enter a number: "))
# print(palindrome_num(n))

# #palindrome using slicing method

# def palindrome_num(num):
#     num_str = str(num)
#     return num_str == num_str[::-1]

# n = int(input("Enter a number: "))
# print(palindrome_num(n))


#palindrome using mid number 
# 0<n<10^6
#using mid number as a reference compare left and right side of the numbers like 121 take mid as 2 and then compare left and right clusters
#make three clusters

# def is_palindrome(n: int) -> bool:
#     s = str(n)
#     length = len(s)
    
#     middle_index = length // 2
    
#     if length % 2 != 0:
#         middle_number = s[middle_index]
#         left_half = s[:middle_index]
#         right_half = s[middle_index + 1:]
#     else:
#         middle_number = ""
#         left_half = s[:middle_index]
#         right_half = s[middle_index:]

#     return left_half == right_half[::-1]
# number=int(input("enter the number"))
# print(f"{number} is a palindrome: {is_palindrome(number)}")


# test_numbers = [121, 1221, 12321, 123421, 1234321, 1, 22, 1234322]
# for number in test_numbers:
#     print(f"{number} is a palindrome: {is_palindrome(number)}")





# def is_palindrome(numb: int) -> bool:
#     digits = [int(digit) for digit in str(numb)]
#     return digits == digits[::-1]

# number = int(input("Enter the number: "))
# print(f"{number} is a palindrome: {is_palindrome(number)}")

