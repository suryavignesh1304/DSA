import math

def linear(a,x):
    n=len(a)
    for i in (0,n):
        return a[i] == x
    
# Given a list of words, generate a list of their lengths.

words=['one','hello','me']
word=[len(word) for word in words]
print(word)


# Given a list of words, generate a list of their first letters.
f_l=[f[0] for f in words]
print(f_l)

# Given a list of words, generate a list with each word converted to uppercase.
to_upper=[word.upper() for word in words]
print(to_upper)

# Given a string of mixed characters, generate a list of digits present in the string.

str="21vd1a6657"
list=[l for l in str if l.isdigit()]
print(list)

# Given a string, generate a list of vowels present in the string.
str = 'hello'
vowels = 'aeiou'
list = [l for l in str.lower() if l in vowels]
print(list)
# OR
str = 'hello'
v1 = 'aeiou'
v2='AEIOU'
list = [l for l in str if l in v1 or l in v2]
print(list)

# Given a list of words, generate a list of words that are longer than three characters.
word=[word for word in words if len(word)>3]
print(word)


# Given a list of words, generate a list with each word reversed.
reversed_words = [word[::-1] for word in words]
print(reversed_words)

