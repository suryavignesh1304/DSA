# Problem 3: Maximum of All Subarrays of Size K
# Description:
# Given an array of integers and a number K, find the maximum of each subarray of size K.
# Input: arr = [1, 3, -1, -3, 5, 3, 6, 7], K = 3  
# Output: [3, 3, 5, 5, 6, 7]  
# Explanation: Maximum of each subarray of size 3 is [3, 3, 5, 5, 6, 7]

def maximum(arr,k):
    arr1 =[]
    n = len(arr) 
    if n == 0 or k == 0:
        return result
    for i in range(n-k+1):
        maxi = arr[i]
        for j in range(1,k):
            if arr[i+j] >  maxi:
                maxi = arr[i+j]
        arr1.append(maxi)
    return arr1
arr = [1,3,-1,-3,5,3,6,7]
k=int(input("enter k value"))
print(maximum(arr,k))