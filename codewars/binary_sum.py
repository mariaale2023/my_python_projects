# https://www.codewars.com/kata/551f37452ff852b7bd000139/train/python
# Implement a function that adds two numbers together and returns their sum in binary. 

# eg
# 1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)


def add_binary(a,b):
    sum = a+b
    #remove the '0b' prefix 
    binary = bin(sum)[2:]
    # print(type(binary)) # now is a string
    print(f'{a}, {b} --> "{binary}" ({a} + {b} = {sum} in decimal or {binary} in binary)')
    return (binary)
    
#testing

add_binary(3,4)
add_binary(3,8)
add_binary(3,825)