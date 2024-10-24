# main.py

from minesweeper import Minesweeper

def main():
    """
    fonction responsable du déroullement du jeu
    """
    
    size = input("Select grid size (int): ")
    dif = input("Select number of mines (int): ")


    game = Minesweeper(int(dif), int(size), int(size))
    
    print("Initial Minesweeper Grid:")
    game.grid.show()

    game_over = False
    while not game_over:
        command = input("\nEnter a command (r for reveal, f for flag) and coordinates (x y): ")
        inputs = command.split()

        if len(inputs) != 3:
            print("Invalid input. Please enter a command followed by two coordinates.")
            continue
        
        cmd, x, y = inputs[0], int(inputs[1]), int(inputs[2])

        if cmd == 'r':  
            game_over = not game.reveal_cell(x, y)
        elif cmd == 'f':  
            game.toggle_flag(x, y)
        else:
            print("Unknown command. Use 'r' to reveal and 'f' to flag.")

    print("Game over!")

if __name__ == "__main__":
    main()