def is_accepted(string):
    stack = []
    i = 0
    n = 0
    m = 0
    
    while i < len(string) and string[i] == 'a':
        stack.append('a')
        i = i + 1;
        n = n + 1;
        
    while i < len(string) and string[i] == 'b':
        if not stack:
            break
        stack.pop()
        m = m + 1
        i = i + 1
    
    while i < len(string) and string[i] == 'b':
        m = m + 1
        i = i + 1
        
    return 2*n == m and i == len(string)

if __name__ == "__main__":
    string = input("Enter a string: ")
    if is_accepted(string):
        print("String is accepted (a^n b^2n)")
    else:
        print("String is not accepted")
        
    
