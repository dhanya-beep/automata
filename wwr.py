def is_accepted(string):
    stack = []
    length = len(string)
    
    if length % 2 != 0:
        return False
    
    mid = length//2
    
    for i in range(mid):
        stack.append(string[i])
    
    for i in range(mid,length):
        if not stack or stack.pop() != string[i]:
            return False
        
    return not stack
    

if __name__ == "__main__":
    string = input("enter a string")
    if is_accepted(string):
        print("string is accepted")
    else:
        print("string is not accepted")
