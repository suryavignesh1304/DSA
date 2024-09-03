# Problem 1: Longest Substring with K Distinct Characters
# Description:
# Given a string S and a number K, find the length of the longest substring that contains exactly K distinct characters.
# Input: S = "araaci", K = 2  
# Output: 4  
# Explanation: The longest substring with 2 distinct characters is "araa".
def longest_substring_with_k_distinct(s,k):
    if k==0 or not s:
        return 0
    char_frequent={}
    window_start=0
    max_length=0
    for window_end in range(len(s)):
        right_char =s[window_end]
        if right_char not in char_frequent:
            char_frequent[right_char]=0
        char_frequent[right_char]+=1
        
        while len(char_frequent)>k:
            left_char = s[window_start]
            char_frequent[left_char]-=1
            if char_frequent[left_char]==0:
                del char_frequent[left_char]
            window_start+=1
        max_length=max(max_length,window_end-window_start+1)
    return max_length
print(longest_substring_with_k_distinct("araaci", 2))