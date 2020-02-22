# Cynthia Lee
# 111737790
# cyllee
#
# CSE 337 (Fall 2019)
# Unit Homework 1

from count_failed_addresses import count_failed_addresses

def consolidate_sources(logname):
    # ADD YOUR CODE HERE
    # logname is string name of file
    # return dictionary, key is ip and value is are ints
    # dictionary key octets
    # based on their first three number
    # dictionary.setdefault(keyname, value)
    
    sources = count_failed_addresses(logname)
    dict = {}
    for x in sources:
        octetEnd = x.find(".")
        octetEnd = x.find(".", octetEnd + 1)
        octetEnd = x.find(".", octetEnd + 1)
        # print(x)
        # print(octetEnd)
        octet = x[0:octetEnd]
        # print(octet)
        # print("stop")
        
        if (octet in dict):
            dict[octet] = dict[octet] + sources[x]
        else: # first time
            dict.setdefault(octet, sources[x])
    
    return dict  # CHANGE OR REMOVE THIS LINE


# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    print("test-log-1.txt produced the consolidated dictionary:")
    print(consolidate_sources("test-log-1.txt"))
    print()

    print("test-log-2.txt produced the consolidated dictionary:")
    print(consolidate_sources("test-log-2.txt"))
    print()

    print("test-log-3.txt produced the consolidated dictionary:")
    print(consolidate_sources("test-log-3.txt"))
    print()

    print("test-log-4.txt produced the consolidated dictionary:")
    print(consolidate_sources("test-log-4.txt"))
    print()

