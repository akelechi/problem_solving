# Enter your code here. Read input from STDIN. Print output to STDOUT
def camelCase(rawInput):
    combined_list = ""
    first = rawInput[0]
    second = rawInput[1]
    third = rawInput[2]
    if first == 'S':
        print('Split incoming ...')
        indices = [idx for idx in range(len(third)) if third[idx].isupper()]
        third = third.lower()
        
        if indices[0]==0:
            combined_list = third[0]
        else:
            combined_list = third[0:indices[0]-1]
        
        for idx in range(len(indices)-1):
            combined_list = "".join((combined_list, third[indices[idx]+1:indices[idx+1]-1], " ", third[indices[idx]]))
            print("".join(('The upper case letter is ', third[indices[idx+1]])))
        combined_list = "".join((combined_list, third[indices[-1]:]))
        if second=='M':
            print('We have a method to split...')
            print(combined_list[:-2])
        else:
            print('Definitely a Class or Variable...')
            print(combined_list)
    else:
        print('Combine incoming...')
        theInput = third.split()
        pos = 0
        for word in theInput:
            word = word.lower()
            if pos > 0:
                word[0] = word[0].upper()
            pos = pos + 1
            theInput[pos] = word
        combined_list = "".join(theInput)
        
        if second == 'M':
            print('You need to result in a method')
            print("".join((combined_list, "()")))
        else:
            print(combined_list)
    
    


if __name__ == '__main__':
    rawInput = list(map(str, input().rstrip().split(';')))

    camelCase(rawInput)
            
    

    
    
