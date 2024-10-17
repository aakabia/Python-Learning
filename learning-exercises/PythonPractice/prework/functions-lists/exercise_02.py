# String Length Greater Than One
# ==============================

# 1. Define a function that confirms a string length is greater
# than one. It should return a `bool`.
#
# Name: str_len_greater_than_one
# Inputs: str
# Outputs: bool
#
# 2. Call that function more than once.
# (Uncomment the code below if your function name is `str_len_greater_than_one`.)


# Example
# result = str_len_greater_than_one("rhubarb")
# print(result)  # True
#
# print(str_len_greater_than_one(""))  # False
# print(str_len_greater_than_one("a"))  # False
# print(str_len_greater_than_one("idiomatic Python"))  # True



def str_len_greater_than_one(str):
    if len(str.strip()) > 1:
        return True
    
    return False
    

result = str_len_greater_than_one("rhubarb")
print(result)
print(str_len_greater_than_one(""))  
print(str_len_greater_than_one("a"))  
print(str_len_greater_than_one("idiomatic Python"))  


# 2. Challenge: Write a second function that trims the string and confirms
# the length is greater than one.
