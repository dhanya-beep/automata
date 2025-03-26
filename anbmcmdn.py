def is_accepted(string):
    stack = []
    length = len(string)
    
    i = 0
    while i < len(string) and string[i] == '0':
        stack.append('0')
        i = i + 1

        
    while i < len(string) and string[i] == '1':
        stack.append('1')
        i = i + 1

        
    while i < len(string) and string[i] == '2':
        if not stack or stack[-1] != '1':
            return False
        stack.pop()
        i = i + 1
        
    
    while i < len(string) and string[i] == '3':
        if not stack or stack[-1] != '0':
            return False
        stack.pop()
        i = i + 1
        
    return not stack and i == len(string)

if __name__ == "__main__":
    string = input("enter a string")
    if is_accepted(string):
        print("the string is accepted")
    else:
        print("string not accepted")
