a = int(input("Enter Number 1 :-"))
b = int(input("Enter Number 2 :-"))

if(a and b):
    print("Same")
elif(a or b):
    print("AT LEAST ONE OPERAND IS TRUE")
elif(not(a)):
    print("Change Value")
else:
    print("Bye")