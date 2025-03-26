exp = input("enter an expression").split()
temp = 1

while len(exp) > 1:
    print(f"t{temp} = {exp[0]}{exp[1]}{exp[2]}")
    exp[:3] = [f"t{temp}"]
    temp = temp + 1
