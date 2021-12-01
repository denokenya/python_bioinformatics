def mathFunction(x, y):
    z = (x+y)*(x-y)
    return z


x = int(input("Enter the value of X\n"))
y = int(input("Enter the value of y"))

answer = mathFunction(x, y)
print(answer)
