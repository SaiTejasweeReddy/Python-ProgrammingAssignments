text = input("Enter a sentence: ") #taking an input from the user
longest = 0 #initializing the longest word to be 0
for words in text.split(" "): #splitting the sentence into words separated by 'spaces'
    #finding the length of words and comparing them to find the longest
    if len(words) > longest:
        longest = len(words)
        longest_word = words
#printing the longest word with its length
print("Longest word is", longest_word, "with length", len(longest_word))