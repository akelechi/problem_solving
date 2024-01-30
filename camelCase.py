# Enter your code here. Read input from STDIN. Print output to STDOUT
def camelCase(rawInput):
    combined_list = ""
    first = rawInput[0]
    second = rawInput[1]
    third = rawInput[2]
    if first == 'S':
        indices = [idx for idx in range(len(third)) if third[idx].isupper()]
        third = third.lower()
        
        if indices[0]==0:
            combined_list = third[0]
        else:
            combined_list = third[:indices[0]]
        
        for idx in range(len(indices)-1):
            combined_list = "".join((combined_list, third[indices[idx]+1:indices[idx+1]], " "))
        
        combined_list = "".join((combined_list, third[indices[-1]:]))
        if second=='M':
            print(combined_list[:-2])
        else:
            print(combined_list)
    else:
        theInput = third.split()
        pos = 0
        for word in theInput:
            word = word.lower()
            if pos > 0:
                beg = word[0].upper()
                word = "".join((beg, word[1:]))
            pos = pos + 1
            theInput[pos-1] = word
        combined_list = "".join(theInput)
        
        if second == 'M':
            print("".join((combined_list, "()")))
        else:
            print(combined_list)
    
    


if __name__ == '__main__':
    rawInput = list(map(str, input().rstrip().split(';')))

    camelCase(rawInput)
            
    

    
    
