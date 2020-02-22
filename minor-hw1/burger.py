# Cynthia Lee
# 111737790
# cyllee
#
# CSE 337 (Fall 2019)
# Minor Homework 1, Problem 1

def burger(order):
    # ADD YOUR CODE HERE
    # return -1  # CHANGE OR REMOVE THIS LINE
    
    protien_types = "BTV"
    toppings_types = "ltopjcbsmf"
    condiment_types = "kuyaq"
    
    num_protien = 0
    num_toppings = 0
    num_condiments = 0
    
    for i in order:
        if i in protien_types:
            num_protien += 1
        elif i in toppings_types:
            num_toppings += 1
        elif i in condiment_types:
            num_condiments += 1
        else:
            return "unrecognized order code"
    
    if num_protien != 1 or num_toppings > 5 or num_condiments > 2:
        return "invalid order"    
    # valid order has exactly 1 protien, up to 5 toppings and 2 condiments
    # elements can be in any order
    
    # calculate the cost
    cost = 0.0
    protein_cost = 0.0
    
    if "B" in order:
        protein_cost = 2
    elif "T" in order:
        protein_cost = 2.5
    else:
        protein_cost = 2.25 # veggie is left
    
    cost = protein_cost + (0.5 * num_toppings)
    return cost

# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    print('burger("Bck"):', burger("Bck")) # simple cheeseburger
    print()
    print('burger("Tpmlmy"):', burger("Tpmlmy")) # turkey burger w/ stuff
    print()
    print('burger("altop"):', burger("altop")) # error: no protein
    print()
    print('burger("VtojsT"):', burger("VtojsT")) # error: too many protein choices
    print()
    print('burger("lsucjV"):', burger("lsucjV")) # okay; protein at end
    print()
    print('burger("Bqcbksmfy"):', burger("Bqcbksmfy")) # error: too many condiments
    print()
    print('burger("Toxpk"):', burger("Toxpk")) # error: invalid character (x)
    print()
    print('burger("Vqltopjm"):', burger("Vqltopjm")) # error: too many toppings
    print()

