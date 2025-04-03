from tabulate import tabulate

moves = input("type moves (separated by spaces); ") # e.g. "d4 c6 Nf3 d5"

move_list = moves.split() # turning the user input into a list of strings
paired_moves = [move_list[i:i+2] for i in range(0, len(move_list), 2)] # grouping moves into pairs

data = paired_moves
column_names = ["white", "black"]


def createMoveTable(data, column_names):
    print(tabulate(data, column_names, tablefmt="fancy_grid"))


createMoveTable(data, column_names)
