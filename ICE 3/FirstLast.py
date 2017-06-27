#defining a function to print the first and last element of the given list
def print_list_ends(a):
    print([a[0], a[len(a)-1]])
#this is the main function where the execution starts
if __name__ == "__main__":
    a=[5,10,15,20,25] #an input can be given in the program or can be taken from the user
    #a= input('Enter a list of numbers ')
    print_list_ends(a) #calling the function