# Read Required String
# ====================

# 1. Define a function that reads a value from a user
# and issues a warning if the value is blank (whitespace) or empty.
# Re-prompt the user.
# If the value is not blank or empty, return it.
# (Hint: use a loop.)
# 
# Name: read_required_string
# Inputs: str (prompt to the user)
# Output: str (a non-blank, non-empty string)

# Example
# value = read_required_string("Favorite food?: ")
#
# Favorite food?:
# Value is required.
# Favorite food?:
# Value is required.
# Favorite food?:
# Value is required.
# Favorite food?: spaghetti

def read_required_string(str):
    value = input(str)
    while not value.strip():
        print("Error String is empty")
        value = input(str)
    
    return value
        




read_required_string("Favorite food?:")