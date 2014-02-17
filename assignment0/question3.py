def sortcat (arg1, *vararg):
    strings = {}
    # put al input strings into a dictionary
    for var in vararg:
        strings[len(var)] = var
    # sort the dictionary by length
    strings = sorted(strings.items())
    strings.reverse()
    
    # prepare variables for printing concat of largest arg1 strings
    num = arg1
    count = 0
    final_string = ""
    words = [x[1] for x in strings]
    
    # print largest num strings
    while num > 0:
        final_string+=words[count]
        count+=1
        num-=1
    print final_string
