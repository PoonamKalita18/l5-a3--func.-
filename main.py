def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def add(x,y):
    return x+y
def substract(x,y):
    return x-y
x = int(input("enter a number"))
y = int(input("enter another number"))

print("Sum :", add(x,y))
print("difference :", substract(x,y))
print("multiply :", multiply(x,y))
print("quotient :", divide(x,y))