# Enter your code here. Read input from STDIN. Print output to STDOUT
def camelCase(rawInput):
    first = rawInput[0]
    second = rawInput[1]
    third = rawInput[2]
    if first == 'S':
        if second == 'M':
            output = getSplit(third[:-2])
        elif second == 'C':
            word = "".join((third[0].lower(), third[1:]))
            output = getSplit(word)
        else:
            output = getSplit(third)
        
        print(output.strip())
        
    else:
        theInput = third.split()
        pos = 0
        for word in theInput:
            word = word.lower()
            if (pos > 0) or (pos == 0 and second == 'C'):
                beg = word[0].upper()
                word = "".join((beg, word[1:]))
            pos = pos + 1
            theInput[pos-1] = word
        combined_list = "".join(theInput)
        
        if second == 'M':
            print("".join((combined_list, "()")))
        else:
            print(combined_list.strip())
    
    
def getSplit(camelWord):
    combined_list = ""
    indices = [idx for idx in range(len(camelWord)) if camelWord[idx].isupper()]
    
    if len(indices)>0:
        for idx in range(len(indices)):
            if idx == 0:
                combined_list = camelWord[:indices[0]].lower()
            elif idx < len(indices)-1:
                combined_list = "".join((combined_list, " ", camelWord[indices[idx]:indices[idx+1]].lower()))
            else:
                combined_list = "".join((combined_list, " ", camelWord[indices[idx]:].lower()))
    else:
        combined_list = camelWord.lower()
        
    return combined_list.strip()
        

if __name__ == '__main__':
    rawInput = list(map(str, input().rstrip().split(';')))

    camelCase(rawInput)
            
    

    
    
