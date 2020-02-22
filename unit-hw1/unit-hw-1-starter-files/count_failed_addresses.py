# Cynthia Lee
# 111737790
# cyllee
#
# CSE 337 (Fall 2019)
# Unit Homework 1

def count_failed_addresses(logname):
    # ADD YOUR CODE HERE
    # logname is a string representing the name of the file
    # also includes necessary path information for that data file
    # return a dictionary whose keys and strings correspond to IP addresses in doted quad format
    # each key has a positive integer as its value
    dict = {}
    # dictionary.setdefault(keyname, value)
    f = open(logname, "r")
    for x in f:
        if ("Disconnected from" in x):
            # print(x)
            start = x.find("Disconnected from ") + 18 
            end = x.find(" ", start)
            ip = x[start:end]
            if (ip in dict):
                dict[ip] = dict[ip] + 1
            else: # first time
                dict.setdefault(ip, 1)
    
    f.close()
    return dict  # CHANGE OR REMOVE THIS LINE


# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    print("test-log-1.txt produced the dictionary:")
    print(count_failed_addresses("test-log-1.txt"))
    print()

    print("test-log-2.txt produced the dictionary:")
    print(count_failed_addresses("test-log-2.txt"))
    print()

    print("test-log-3.txt produced the dictionary:")
    print(count_failed_addresses("test-log-3.txt"))
    print()

    print("test-log-4.txt produced the dictionary:")
    print(count_failed_addresses("test-log-4.txt"))
    print()


