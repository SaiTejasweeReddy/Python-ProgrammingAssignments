str1=input("enter a string: ")#taking an input from the user which is a mix of alphabets and numbers
#initializing two variables to count digits and letters
d=0
l=0
#reading the string given by the user
for i in str1:
    if i.isdigit(): #using isdigit() to check if the string has numbers
        d=d+1
    elif i.isalpha(): #using isalpha() to check if the string has letters
        l=l+1
    else: #anything other than a number or letter in the given string is skipped
        pass
#printing the number of digits and lettes in the given string
print("Letters", l)
print("Digits", d)