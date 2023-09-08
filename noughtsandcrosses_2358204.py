import random
import os.path
import json

random.seed()

def draw_board(board):
     # Draw the board for tic tac toe.
    for row in board:
        print(row[0], "|", row[1], "|", row[2])
        print("---------")
        pass

def welcome(board):
    # Print the welcome message and display the board by calling draw_board(board)
    print("Welcome to Tic Tac Toe!\n Here we go..")
    draw_board(board)
    pass

def initialise_board(board):
    # Set all elements of the board to one space ' '
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '
    return board

def get_player_move(board):
    # Ask the user for the cell to put the X in
    #  and return row and col
    valid_step = False
    while not valid_step:
        try:
            print('\t\t\t\t1 2 3')
            print('\t\t\t\t4 5 6')
            print('\t\t\t\t7 8 9')
            step = int(input("Enter the input number from the given option: "))
            if step<1 or step >9:
                print("Invalid input,\n please try again.")
            row, col=(step-1)//3,(step-1)%3
            if board[row][col] != ' ':
                print("This cell is already occupied,\n please try again.")
            else:
                valid_step = True
        except ValueError:
            print("Invalid input,\n please try again.")
    return row, col

def choose_computer_move(board):
    # Choose a random cell to put a nought in
    # and return row and col
    blank_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                blank_cells.append((i, j))

    if not blank_cells:
        return None

    return random.choice(blank_cells)

def check_for_win(board, mark):
    # Check if either the player or the computer has won
    # Return True if someone won, False otherwise
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == mark:
            return True
        if board[0][i] == board[1][i] == board[2][i] == mark:
            return True
    if board[0][0] == board[1][1] == board[2][2] == mark:
        return True
    if board[0][2] == board[1][1] == board[2][0] == mark:
        return True
    return False

def check_for_draw(board):
    # Check if all cells are occupied
    # Return True if it is, False otherwise
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True
        
def play_game(board):
    # Initialise the board
    board = initialise_board(board)

    # Draw the board
    draw_board(board)

    # Game loop
    while True:
        # Player's move
        row, col = get_player_move(board)
        board[row][col] = "X"
        if check_for_win(board, "X"):
            return 1
        elif check_for_draw(board):
            return 0
        # Computer's move
        row, col = choose_computer_move(board)
        board[row][col] = "O"
        if check_for_win(board, "O"):
            return -1
        elif check_for_draw(board):
            return 0
        draw_board(board)
def menu():
     #Print the instruction in menu bar
    while True:
        print("Menu:")
        print("1 - Play the game")
        print("2 - Save score in file 'leaderboard.txt'")
        print("3 - Load and display the scores from the 'leaderboard.txt'")
        print("q - End the program")
        choice = input("Enter your choice: ")
        if choice in ['1', '2', '3', 'q']:
            return choice
        else:
            print("Invalid choice, please try again.")

def save_score(score):
    #Prompting the player's name
    name = input("Enter your name: ")
    scores = {}
    filename="leaderboard_2358204.txt"
    if is_file(filename):
        try:
            with open('leaderboard_2358204.txt', 'r') as f:
                scores = json.load(f)
        except FileNotFoundError as e:
            raise e
        
        if name in scores:
            scores[name]=score+scores[name]
        else:
            scores[name] = score

        with open('leaderboard_2358204.txt', 'w') as f:
            json.dump(scores, f)

        print("Your point is saved to leaderboard!")
    else:
        print("Leaderboard not found")

def is_file(filename):
    return os.path.exists(filename)

def load_scores():
    #This function is used to load the score in the filename
    scores={}
    filename="leaderboard_2358204.txt"
    if is_file(filename):
        try:
            with open(filename,"r") as file:
                scores = json.load(file)
        except (FileNotFoundError , json.JSONDecodeError):
            print("Sorry! Failed to load score .Try again!")
    else:
        print("Leaderboard not found" )
    return scores 

def display_leaderboard(leaders):
     #This function is used to display the score in the leaderboard
    print("Leaderboard:")
    for name, score in leaders.items():
        print(f"{name}: {score}")



