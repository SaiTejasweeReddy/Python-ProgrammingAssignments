num1String = input('Please enter an integer: ')
num1 = int(num1String)
rem=0
rev=0
while(num1>0):
    rem=num1%10
    num1=num1//10
    rev=rev*10+rem
print(rev)