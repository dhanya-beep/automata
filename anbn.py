def is_accepted(string):
    stack = []
    
    for char in string:
        if char == 'a':
            stack.append('a')
        elif char == 'b':
            if not stack:
                return False
            stack.pop()
        else:
            return False
    return not stack

if __name__ == "__main__":
    string = input("Enter a string")
    if is_accepted(string):
	    print("string is accepted")
    else:
	    print("string is not accepted")
