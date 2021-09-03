## Read input as specified in the question.
## Print output as specified in the question.
def star(str):
    if len (str) == 0:
        return ""
    if len (str) == 1:
        return str
    sub = star(str[1:])
    if(str[0] == sub[0]):
        return str[0] + "*" + sub
    else:
        return str[0] + sub
    
print(star(input()))
    
