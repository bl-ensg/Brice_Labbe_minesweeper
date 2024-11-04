import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QGridLayout, QPushButton, QMessageBox)
from minesweeper import Minesweeper

class MinesweeperGUI(QMainWindow):
    def __init__(self, dif, taille_x, taille_y):
        """
        Initialise l'interface graphique pour le jeu de démineur utilisant PyQt5.

        Paramètres
        ----------
        dif : int
            Nombre de mines dans le jeu.
        taille_x : int
            Largeur de la grille de jeu.
        taille_y : int
            Hauteur de la grille de jeu.

        Attributs
        ---------
        game : Minesweeper
            Instance du jeu de démineur.
        buttons : dict
            Dictionnaire des boutons représentant chaque case.
        """
        super().__init__()
        self.dif = dif
        self.taille_x = taille_x
        self.taille_y = taille_y
        self.game = Minesweeper(dif, taille_x, taille_y)

        self.initUI()

    def initUI(self):
        """
        Initialise l'interface utilisateur de la fenêtre principale.
        """
        self.setWindowTitle('Minesweeper')
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.createGrid()
        self.show()

    def createGrid(self):
        """
        Crée la grille de boutons pour représenter les cases du jeu.
        """
        self.grid_layout = QGridLayout()
        self.buttons = {}

        for x in range(self.taille_x):
            for y in range(self.taille_y):
                button = QPushButton('')
                button.setFixedSize(40, 40)
                button.setStyleSheet('background-color: lightgray;')
                button.setContextMenuPolicy(Qt.CustomContextMenu)
                button.customContextMenuRequested.connect(lambda pos, x=x, y=y: self.flagCell(x, y))
                button.clicked.connect(lambda checked, x=x, y=y: self.revealCell(x, y))
                self.grid_layout.addWidget(button, x, y)
                self.buttons[(x, y)] = button

        self.central_widget.setLayout(self.grid_layout)

    def revealCell(self, x, y):
        """
        Gère le clic pour révéler une case dans l'interface.

        Paramètres
        ----------
        x : int
            Position X de la case.
        y : int
            Position Y de la case.
        """
        result = self.game.reveal_cell(x, y)
        self.updateGUI()
        if not result:
            self.showGameOver(won=False)
        elif self.game.check_victory():
            self.showGameOver(won=True)

    def flagCell(self, x, y):
        """
        Gère le clic droit pour placer un drapeau sur une case.

        Paramètres
        ----------
        x : int
            Position X de la case.
        y : int
            Position Y de la case.
        """
        self.game.toggle_flag(x, y)
        self.updateGUI()
        if self.game.check_victory():
            self.showGameOver(won=True)

    def updateGUI(self):
        """
        Met à jour l'affichage de la grille en fonction de l'état de chaque case.
        Affiche les mines, drapeaux et chiffres adjacents.
        """
        colors = {
            1: 'blue',
            2: 'green',
            3: 'red',
            4: 'darkblue',
            5: 'maroon',
            6: 'turquoise',
            7: 'black',
            8: 'gray'
        }

        for x in range(self.taille_x):
            for y in range(self.taille_y):
                cell = self.game.grid.grid[x][y]
                button = self.buttons[(x, y)]
                if cell.reveal:
                    if cell.mine:
                        button.setText('💣')
                        button.setStyleSheet('background-color: red; font-weight: bold;')
                    elif cell.adj > 0:
                        color = colors.get(cell.adj, 'black')
                        button.setText(str(cell.adj))
                        button.setStyleSheet(f'color: {color}; background-color: white; font-weight: bold;')
                    else:
                        button.setText('')
                        button.setStyleSheet('background-color: white;')
                    button.setEnabled(False)
                elif cell.flag:
                    button.setText('🚩')
                    button.setStyleSheet('background-color: lightgray;')
                    button.setEnabled(True)
                else:
                    button.setText('')
                    button.setStyleSheet('background-color: lightgray;')
                    button.setEnabled(True)

    def showGameOver(self, won):
        """
        Affiche un message indiquant la fin de la partie, gagnée ou perdue.

        Paramètres
        ----------
        won : bool
            Indique si le joueur a gagné.
        """
        if won:
            message = "Félicitations! Vous avez gagné la partie!"
        else:
            message = "Boom! Vous avez touché une mine. Partie terminée."

        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText(message)
        msg_box.setWindowTitle("Fin de la partie")
        msg_box.setStandardButtons(QMessageBox.Ok)
        retval = msg_box.exec_()

        if retval == QMessageBox.Ok:
            self.game.reset_game()
            self.updateGUI()
