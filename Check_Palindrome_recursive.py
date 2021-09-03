## Read input as specified in the question.
## Print output as specified in the question.
def strrev(str,n):
    if n == len(str):
        return ""
    return strrev(str,n+1) + str[n]
str = input()
if(str == strrev(str,0)):
    print("true")
else:
    print("false")
