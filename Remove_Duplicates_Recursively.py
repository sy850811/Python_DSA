# Problem ID 91, removeConsecutiveDuplicates
def rcd(s):
    if(len(s) == 0 or len(s) == 1):
        return s
    sub = rcd(s[1:])
    if(s[0] == sub[0]):
        return sub
    else:
        return s[0] + sub

# Main
string = input().strip()
print(rcd(string))

