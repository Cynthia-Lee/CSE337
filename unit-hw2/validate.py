# Cynthia Lee
# 111737790
# cyllee
#
# CSE 337 (Fall 2019)
# Unit Homework 2

def validate(filename):
    # ADD YOUR CODE HERE
    # reading and saving the data into a dict
    rooms = {}
    data = {
        "TITLE": "",
        "DESC": "",
        "EXITS": "",
        "ITEMS": "",
        "PUZZLE": ""
    }
    desc = []
    exits = []
    items = []
    puzzle = []
    def pInt(n):
        return int(n)
    
    f = open(filename, "r")
    for line in f:
        if (line[0:4] == "ROOM"): # integer number
            num = line[5:].strip()
            num = int(num)
        elif (line[0:5] == "TITLE"): # string name
            data["TITLE"] = line[6:].strip()
        elif (line[0:4] == "DESC"): # up to 60 characters, line maybe repeated
            desc.append(line[5:].strip())
        elif (line[0:5] == "EXITS"): # north, east, south, west = integers
            str = line[6:]
            exits = str.split()
            exits = list(map(pInt, exits))
        elif (line[0:5] == "ITEMS"): # one or more strings (optional)
            str = line[6:]
            items = str.split()
            data["ITEMS"] = items
            # data.setdefault("ITEMS", items)
            items = []
        elif (line[0:6] == "PUZZLE"): # string item (optional)
            str = line[7:]
            puzzle = str.split()
            data["PUZZLE"] = puzzle
            # data.setdefault("PUZZLE", puzzle)
            puzzle = []
        elif (line[0:3] == "---"):
            data["DESC"] = desc
            data["EXITS"] = exits
            rooms.setdefault(num, data)
            desc = []
            exits = []
            data = {
                "TITLE": "",
                "DESC": "",
                "EXITS": "",
                "ITEMS": "",
                "PUZZLE": ""
            }
    # outside for loop for reading lines
    data["DESC"] = desc
    data["EXITS"] = exits
    rooms.setdefault(num, data)
    desc = []
    exits = []
    data = {
        "TITLE": "",
        "DESC": "",
        "EXITS": "",
        "ITEMS": "",
        "PUZZLE": ""
    }
    f.close()
    # processing the data
    answer = {
        "phantoms": [],
        "missing": [],
        "mismatches": []
    }
    tItems = []
    tPuzzle = []
    for k in rooms:
        # print(rooms[k]["EXITS"])
        # print(rooms[k].keys())
        c = 0
        for r in rooms[k]["EXITS"]:
            if (r != -1 and r not in rooms.keys() and r not in answer["phantoms"]):
                answer["phantoms"].append(r)
            if (r != -1 and r not in rooms.keys()):
                # if it does not lead to a known room, add tuple
                # (room number, exit direction index, "unknown")
                answer["mismatches"].append((k, c, "unknown"))
            elif (r != -1):
                # c is exit index in r
                oppIndex = (c + 2) % 4
                # if the room's matching exit does not match the current room, append tuple
                # (room number, exit direction index, "mismatch")
                # each exit's opposite exit direction is its number plus 2, mod 4
                if (rooms[r]["EXITS"][oppIndex] != k):
                    answer["mismatches"].append((k, c, "mismatch"))
            c += 1
        for i in rooms[k]["ITEMS"]:
            tItems.append(i)
        for p in rooms[k]["PUZZLE"]:
            tPuzzle.append(p)
    # print(tItems)
    # print(tPuzzle)
    for p in tPuzzle:
        if (p not in tItems):
            answer["missing"].append(p)
    
    return answer # CHANGE OR DELETE THIS STATEMENT


# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    print('validate("map1.txt") produces:', validate("map1.txt"),sep="\n")
    print()
    print('validate("map2.txt") produces:', validate("map2.txt"),sep="\n")
    print()
    print('validate("map3.txt") produces:', validate("map3.txt"),sep="\n")
    print()
    print('validate("map4.txt") produces:', validate("map4.txt"),sep="\n")
    print()
    print()

