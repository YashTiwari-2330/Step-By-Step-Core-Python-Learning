num = int(input("Enter a number :-"))
orignal = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num //10

if(orignal == rev):
    print("palidrome")
else:
    print("Not palidrome")