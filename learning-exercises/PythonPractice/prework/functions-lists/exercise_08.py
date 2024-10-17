import random


def create_random_int_list(count):
    result = []
    for _ in range(count):
        result.append(random.randrange(100))
    return result


# 1. Use the create_random_int_list function to build
# a random 25 element integer list.

result = create_random_int_list(25)




# 2. Calculate the sum. (Results will vary because of randomness.)

totalSum = 0 
for dig in result:
    totalSum = totalSum + dig

print(f"Sum: {totalSum}")



# 3. Challenge: calculate the average.

average = totalSum / len(result)

print(f"Average: {average}")



# 4. Challenge, Challenge: calculate the standard deviation.

variance = sum((x - average) ** 2 for x in result) / (len(result) -1) # Use sum() to get the total
std_dev = variance ** 0.5  # Standard deviation is the square root of variance

print(f"Standard Deviation: {std_dev}")
