# Problem: Remove x from string
def removeX(s): 
    if(len(s) == 0):
        return s
    substring = removeX(s[1:])
    if(s[0] == "x"):
        return substring
    else:
        return s[0] + substring

# Main
string = input()
print(removeX(string))
