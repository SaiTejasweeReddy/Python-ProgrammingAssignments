def print_horiz_line(): #defining a function for horizontal lines
    print(" ---" * board_size)
def print_vert_line(): #defining a function for vertical lines
    print("|   " * (board_size + 1))
#this is the main function from where the actual execution starts
if __name__ == "__main__":
    board_size = int(input("What size of game board? ")) #taking input from the user for the size of the board
    #loop for horizontal and vertical lines in consecutive lines
    for index in range(board_size):
      print_horiz_line()    #calling the functions
      print_vert_line()
    print_horiz_line() #printing the last line