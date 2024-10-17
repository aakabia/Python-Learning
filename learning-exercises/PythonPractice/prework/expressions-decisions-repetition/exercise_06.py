quote = """The human world is made of stories, not people.
The people the stories use to tell themselves are not to be blamed."""
# -- David Mitchell, Ghostwritten

print(quote[4:9])  # human

# 1. Use string slicing to print a substring
# from `quote` to the terminal.
#
# Expected output:
# ================
# The human
# world
# stories
# ,
# people
# The
# to be blamed.

print(quote[0:9])    # "The human"
print(quote[10:15])  # "world"
print(quote[27:34])  # "stories"
print(quote[34:36])  # ","
print(quote[40:46])  # "people"
print(quote[47:51])  # "The"
print(quote[102:]) # "to be blamed."