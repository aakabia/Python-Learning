needle = input("Needle: ")
haystack = input("Haystack: ")

# 1. Collect user input: needle and haystack.
# 2. Use an if/else statement to decide if the needle is
# a substring of haystack. Print the appropriate message.
# (Hint: use the `in` operator.)


#        needle |      haystack |        prints
# ---------------------------------------------------------
#       station | space station | "station" found in "space station"
#          stat | space station | "stat" found in "space station"
#            St | space station | "St" NOT found in "space station"
#           1.0 |  Version 11.0 | "1.0" found in "Version 11.0"
# space station |       station | "space station" NOT found in "station"




if needle == "station" and needle in haystack:
    print("station found in 'space station' ")
elif needle == "stat" and needle in haystack:
    print("stat found in 'space station' ")
elif needle == "St" and not(needle in haystack):
    print(" 'St' NOT found in 'space station' ")
elif needle == "1.0" and needle in haystack:
    print(" '1.0' found in 'Version 11.0'")
elif needle == "space station" and not(needle in haystack):
    print( "'space station' NOT found in 'station'" )
else:
    print("Default case: Needle is not in haystack")
