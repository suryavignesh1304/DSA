#bit manipulation

a=0b0101#5
b=0b0011#3
#and operation
print(bin(a&b))
#or operation
print(bin(a|b))
#exor operation
print(bin(a^b))

#left shift
print(bin(a<<1))

#right shift
print(bin(b>>1))

#not operation
print(bin(~a))


def set_bit(n,k):
    return n | (1<<k)

print(set_bit(0b0101,2))

def remove_bit(n,k):
    return n & ~(1<<(k))

print(remove_bit(0b0101,1))

def toggle(n,k):
    return n ^ (1<<(k-1))

print(toggle(12,3))

def check_bit(n,k):
    if n &(1<<k):
        print('Set')
    else:
        print('Not Set')
        
        
