# main.py

import sys
from PyQt5.QtWidgets import QApplication
from minesweeper_gui import MinesweeperGUI

def main():
    """
    Point d'entrée de l'application de démineur. Demande à l'utilisateur de saisir
    la taille de la grille et le nombre de mines, puis initialise l'interface graphique.

    Exceptions
    ----------
    ValueError
        Levée si les entrées utilisateur ne sont pas des entiers positifs.
    """
    size = input("Sélectionnez la taille de la grille (int) : ")
    dif = input("Sélectionnez le nombre de mines (int). Le nombre de mines doit être inférieur ou égal au nombre de cases : ")

    try:
        grid_size = int(size)
        num_mines = int(dif)

        if grid_size <= 0 or num_mines <= 0:
            raise ValueError

        app = QApplication(sys.argv)
        window = MinesweeperGUI(num_mines, grid_size, grid_size)
        sys.exit(app.exec_())

    except ValueError:
        print("Entrée invalide. Veuillez entrer des entiers positifs pour la taille et le nombre de mines.")


if __name__ == "__main__":
    main()
