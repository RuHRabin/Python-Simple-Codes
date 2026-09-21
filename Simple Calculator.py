#This is a simple calculator.

x = int(input("Input a number:"))
op = str(input("Input the operation type:"))
y = int(input("Input another number:"))
if op == "+":
    print(x+y)
elif op == "-":
    print(x-y)
elif op =="*":
    print(x*y)
elif op == "/":
    print(x/y)
else:
    print("Somrthing was wrong. Please try again.")



