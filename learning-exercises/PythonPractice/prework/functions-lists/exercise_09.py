import random

haystack = [None] * 100
haystack[random.randrange(len(haystack))] = "needle" # produces random range in haystack 

# We have a 100 element `None` list (absence of a value).
# A "needle" is randomly placed in the haystack (list).

# 1. Loop over elements in the haystack.
# When you find the needle, print its index.
# (Hint: use the enumerate function.)

for index, needle in enumerate(haystack):
    if haystack[index] == "needle":
        print(index)
        break