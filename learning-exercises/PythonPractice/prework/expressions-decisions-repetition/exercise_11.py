# Read required string
# ====================

# 1. Use a loop to confirm that the user-entered
# `value` variable is not blank (all whitespace) or empty.
# (Hint: use the `strip` method.)
# If `value` is blank or empty, display an error message
# and re-prompt the user (re-loop).


while True:  # Start an infinite loop to keep prompting the user
    value = input("This value is required: ").strip()  # Strip whitespace from input

    if value == "":  # Check if the stripped value is empty
        print("Please enter a valid input")  # Display error message
    else:
        print("Thank you!")  # Thank the user
        break  # Exit the loop if valid input is provided