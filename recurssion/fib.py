def fib(n):
    if n <=0:
        return "Input should be a greater than zero."
    elif  n==1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = [0, 1]
        while len(fib_series) < n:
            fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

try:
    n = int(input(""))
    print(fib(n))
except ValueError:
    print("Invalid input. Please enter a number.")
    
    
def fib_pos(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return fib_pos(n-1) + fib_pos(n-2)
    
try:
    n = int(input(""))
    print(fib_pos(n))
except ValueError:
    print("Invalid input. Please enter only numbers.")
    
""" write a palindrome using recursive approach"""

""" write a array program in such way that the sum of the number should be equal to the largest number in the array"""
def find_combination(arr, target_sum, s, c_c, result):
    if target_sum == 0:
        result.append(c_c.copy())
        return 
    for i in range(s, len(arr)):
        if arr[i] <= target_sum:
            c_c.append(arr[i])
            find_combination(arr, target_sum - arr[i], i + 1, c_c, result)
            c_c.pop()

def main():
    arr = list(map(int, input("Enter the array elements: ").split()))
    max_num = max(arr)
    result = []

    find_combination(arr, max_num, 0, [], result)
    print("Combinations that sum up to the largest number:")
    for combination in result:
        print(combination)

if __name__ == "__main__":
    main()
    
    
"""product of two numbers using recursion"""
def recursive_product(a, b):
    if b == 0 or a==0:
        return 0
    else:
        return a + recursive_product(a, b-1)
    
print(recursive_product(5,4))

"""minimum number in a array using recursion method"""
import numpy as np
def min_num_recursive(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        m=min_num_recursive(arr[1:])
        if arr[0]<m:
            return arr[0] 
        else:
            return m
        
arr = np.array([3, 1, 4, 2, 5])
print(min_num_recursive(arr))
"""using numpy"""
arr=np.array([3,1,2,5,4])
print(np.min(arr))

""" checking array sorted or not"""
def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))
if is_sorted(arr):
    print("The array is sorted.")
else:
    print("The array is not sorted.")
    
    
