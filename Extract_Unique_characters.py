def uniqueChar(s): 
    d = {}
    for char in s:
        if not d.get(char,False):
            d[char] = 1
            print(char,end = '')






# Main 
s=input() 
uniqueChar(s)
