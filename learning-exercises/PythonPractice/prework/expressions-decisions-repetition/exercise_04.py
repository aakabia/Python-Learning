value = 7 / 3
# 1. Use the variable above to print this
# expected output:
#
# Value: 2.3333333333333335
# Two decimals: 2.33
# Percent, one decimal: 233.3%


print(f"Value:{value}")
print(f"Two decimal places: {value:.2f}")

percent = value *100

print(f"Percent to one decimal place: {percent:.1f}")


red = "red"
blue = "blue"
yellow = "yellow"
# 2. Use the three variables above to print this
# expected output:
#
# ----------------------------------
# |       red|      blue|    yellow|
# |red       |blue      |yellow    |
# |   red    |   blue   |  yellow  |
# ----------------------------------

lineWidth = 50
row1 = ["red","blue","yellow"]
row2 = ["red","blue","yellow"]
row3 = ["red","blue","yellow"]



print("-" * lineWidth)
print(f"|{row1[0]:>15}| {row1[1]:>15}| {row1[2]:>15}|" )# right aligined 
print(f"|{row1[0]:<15}| {row1[1]:<15}| {row1[2]:<15}|" ) # left aligned
print(f"|{row1[0]:^15}| {row1[1]:^15}| {row1[2]:^15}|") # center aligned 




print("-" * lineWidth)