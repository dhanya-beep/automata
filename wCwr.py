def is_accepted(string):
    stack = []
    length = len(string)
    
    if string.count('C') != 1 or string[0] == 'C' or string[-1] == 'C':
        return False
    
    mid = string.index('C')
    
    for i in range(mid):
        stack.append(string[i])
    for i in range(mid+1,length):
        if not stack or stack.pop() != string[i]:
            return False
    return not stack
    
if __name__ == "__main__":
    string = input("Enter a string")
    if is_accepted(string):
        print("the string is accepted")
    else:
        print("string is not accepted")
