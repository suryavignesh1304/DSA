# Problem 2: Smallest Sub array with a Sum Greater Than or Equal to S
# Description:
# Given an array of integers and a number S, find the length of the smallest contiguous sub array whose sum is greater than or equal to S. 
# Return 0 if no such sub array exists.Input: arr = [2, 1, 5, 2, 3, 2], S = 7  
# Output: 2  
# Explanation: The smallest sub array with a sum greater than or equal to 7 is [5,2].
# Input: arr = [2, 1, 5, 2, 3, 2], S = 7  
# Output: 2  
# Explanation: The smallest subarray with a sum greater than or equal to 7 is [5, 2].
def min_sub_array_length(arr, S):
    min_length = float('inf')
    left = 0
    current_sum = 0
    for right in range(len(arr)):
        current_sum += arr[right]
        while current_sum >= S:
            min_length = min(min_length, right - left + 1)
            current_sum -= arr[left]
            left += 1
    return min_length if min_length != float('inf') else 0
arr = [2, 1, 5, 2, 3, 2]
S = 7
print(min_sub_array_length(arr, S))