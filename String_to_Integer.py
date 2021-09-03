## Read input as specified in the question.
## Print output as specified in the question.
def strtoint(str,n):
    if(n > len(str) or len(str)==0):
        return 0
    # print(int(str[-n]))
    return (ord(str[-n]) - ord('0')) + 10* strtoint(str,n+1)
str= input()
print(strtoint(str,1))
