import sys

def swapchars (string):
    most_char = string[0]
    least_char = string[0]
    most = string.count(string[0])
    least = string.count(string[0])
    for l in string:
        if l.isalpha():
            if string.count(l) >= most:
                most_char = l
                most = string.count(l)
            elif string.count(l) <= least:
                least_char = l
                least = string.count(l)
                
    for l in string:
        if l == most_char:
            sys.stdout.write(least_char)
        elif l == least_char:
            sys.stdout.write(most_char)
        else:
            sys.stdout.write(l)
    print
