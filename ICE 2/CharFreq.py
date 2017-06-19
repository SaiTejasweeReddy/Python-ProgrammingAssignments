def char_frequency(str1): #defining a function 'char_frequency' which can take string type parameters
    dict = {} #initializing a dictionary of letters in the string
    #forming key:value pairs of alphabets and their frequency
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
str1=input('enter a string: ') #taking input from the user
print(char_frequency(str1)) #printing the output showing the frequency of characters