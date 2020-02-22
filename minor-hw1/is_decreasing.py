# Cynthia Lee
# 111737790
# cyllee
#
# CSE 337 (Fall 2019)
# Minor Homework 1, Problem 3

def is_decreasing(numbers):
    # ADD YOUR CODE HERE
    # return None # CHANGE OR DELETE THIS STATEMENT
    i = 0
    if numbers == [] or len(numbers) <= 1:
        return True
    if numbers[i] >= numbers[i + 1]:
        return(is_decreasing(numbers[3:]))
    return False

# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    print('Testing is_decreasing([]):', is_decreasing([]))
    print()
    print('Testing is_decreasing([2]):', is_decreasing([2]))
    print()
    print('Testing is_decreasing([28, 28, 24, 14]):', is_decreasing([28, 28, 24, 14]))
    print()
    print('Testing is_decreasing([98, 39, 37, 36, 68]):', is_decreasing([98, 39, 37, 36, 68]))
    print()
    print('Testing is_decreasing([4, 14, 43, 26, 49, 39, 4, 20]):', is_decreasing([4, 14, 43, 26, 49, 39, 4, 20]))
    print()
    print('Testing is_decreasing([97, 95, 75, 74, 67, 66, 48, 42, 42, 18, -5, -5]):', is_decreasing([97, 95, 75, 74, 67, 66, 48, 42, 42, 18, -5, -5]))
    print()

