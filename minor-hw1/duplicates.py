# Cynthia Lee
# 111737790
# cyllee
#
# CSE 337 (Fall 2019)
# Minor Homework 1, Problem 2

def duplicates(installed):
    # ADD YOUR CODE HERE
    # return None # CHANGE OR DELETE THIS LINE
    
    # For example, if the argument contained "/bin/mvdir" and "/opt/local/bin/mvdir",thelistofduplicateprogramswouldcontain(a single copy of) "mvdir".
    # If there are no duplicate programs, your function should return an empty list.
    # NOTE 1: Remember that your result should only contain the program names, not the associated paths. You may ﬁnd the rfind() function and string slicing to be extremely helpful in solving this problem.
    list_of_programs = []
    list_of_duplicates = []
    
    for i in installed: # each string element in the array
        end_path = i.rfind("/")
        program = i[end_path + 1:]
        list_of_programs.append(program)
        
    # checking for duplicates
    for i in range(len(list_of_programs)):
        check = list_of_programs[i]
        for r in range(i + 1, len(list_of_programs)):
            if list_of_programs[r] == check and check not in list_of_duplicates:
                list_of_duplicates.append(check)
        
    return list_of_duplicates

# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    print('Testing duplicates(["/bin/less", "/opt/local/bin/nice", "/usr/local/bin/host", "/usr/local/bin/apropos", "/usr/local/bin/touch"]):')
    print()
    print(duplicates(["/bin/less", "/opt/local/bin/nice", "/usr/local/bin/host", "/usr/local/bin/apropos", "/usr/local/bin/touch"]))
    print('\n')
    print('Testing duplicates(["/opt/local/bin/cp", "/usr/local/bin/ls", "/usr/bin/touch", "/usr/bin/head", "/bin/ls"]):')
    print()
    print(duplicates(["/opt/local/bin/cp", "/usr/local/bin/ls", "/usr/bin/touch", "/usr/bin/head", "/bin/ls"]))
    print('\n')
    print('Testing duplicates(["/opt/local/bin/su", "/usr/bin/yacc", "/bin/strings", "/usr/bin/nice", "/usr/bin/su", "/usr/bin/rm", "/usr/bin/awk", "/opt/local/bin/uptime", "/bin/ed", "/usr/bin/talk", "/usr/bin/less", "/opt/local/bin/cd", "/usr/local/bin/cd", "/usr/local/bin/sed", "/opt/local/bin/sudo", "/usr/bin/uptime", "/usr/bin/gzip", "/usr/bin/uniq", "/usr/local/bin/man", "/usr/local/bin/top"]):')
    print()
    print(duplicates(["/opt/local/bin/su", "/usr/bin/yacc", "/bin/strings", "/usr/bin/nice", "/usr/bin/su", "/usr/bin/rm", "/usr/bin/awk", "/opt/local/bin/uptime", "/bin/ed", "/usr/bin/talk", "/usr/bin/less", "/opt/local/bin/cd", "/usr/local/bin/cd", "/usr/local/bin/sed", "/opt/local/bin/sudo", "/usr/bin/uptime", "/usr/bin/gzip", "/usr/bin/uniq", "/usr/local/bin/man", "/usr/local/bin/top"]))
    print('\n')
    print('Testing duplicates(["/usr/bin/echo", "/bin/screen", "/usr/bin/rm", "/opt/local/bin/grep", "/usr/local/bin/talk", "/opt/local/bin/echo", "/bin/awk", "/bin/vi", "/usr/bin/vi", "/usr/bin/touch", "/bin/make", "/bin/su", "/usr/bin/less", "/opt/local/bin/quota", "/usr/local/bin/grep", "/opt/local/bin/w", "/usr/local/bin/vi", "/bin/sed", "/usr/local/bin/touch", "/bin/emacs"]):')
    print()
    print(duplicates(["/usr/bin/echo", "/bin/screen", "/usr/bin/rm", "/opt/local/bin/grep", "/usr/local/bin/talk", "/opt/local/bin/echo", "/bin/awk", "/bin/vi", "/usr/bin/vi", "/usr/bin/touch", "/bin/make", "/bin/su", "/usr/bin/less", "/opt/local/bin/quota", "/usr/local/bin/grep", "/opt/local/bin/w", "/usr/local/bin/vi", "/bin/sed", "/usr/local/bin/touch", "/bin/emacs"]))
    print()

