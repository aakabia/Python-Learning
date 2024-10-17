# 1. Run this file.
# Collect the user's (your) name.
name = input("What's your name?: ")
favGenre = input("What's your favorite Genre?: ")
rating = int(input("Favorite genre rating? [1-10]: "))
enjoyOthergenre = input("Do you like other Genre's ? [yes or no]: ")

# 2. Collect the user's favorite music genre.



# 3. Collect the user's favorite genre rating, 0-100.
# (No need to validate, but be sure to enter a valid integer.)



# 4. Ask the user if they enjoy other genres.
# The variable should be a boolean.
# You can either convert the `input` function string to a bool(input("prompt"))
# using the boolean literal "True" or "False"
# or compare strings: yes/no, y/n, etc.







if enjoyOthergenre == 'yes':
    enjoyOthergenre = True
elif enjoyOthergenre == 'no':
    enjoyOthergenre = False
else:
    print("Invalid input. Please enter 'yes' or 'no'.")


# 5. Move all `input` operations to the top of the file.
# Collect the four questions.
# Print at the end.
print(f"Name: {name}")
print(f"favorite Genre: {favGenre}")
print(f"Rating: {rating}")
print(f"otherGenre: {enjoyOthergenre}")