# grille.py

import random
from case import Case

class Grille:
    def __init__(self, taille_x, taille_y, dif):
        """
        Initialise la grille du jeu contenant les cases du démineur.

        Paramètres
        ----------
        taille_x : int
            Largeur de la grille.
        taille_y : int
            Hauteur de la grille.
        dif : int
            Nombre de mines à placer sur la grille.

        Attributs
        ---------
        taille_x : int
            Largeur de la grille.
        taille_y : int
            Hauteur de la grille.
        dif : int
            Nombre de mines sur la grille.
        grid : list
            Grille de jeu composée d'instances de Case.
        """
        self.taille_x = int(taille_x)
        self.taille_y = int(taille_y)
        self.dif = int(dif)
        self.grid = [[Case(x, y) for y in range(taille_y)] for x in range(taille_x)]
        self.placement_mines()
        self.calc_adj()

    def calc_adj(self):
        """
        Calcule le nombre de mines adjacentes pour chaque case de la grille.
        """
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]

        for x in range(self.taille_x):
            for y in range(self.taille_y):
                count = 0
                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < self.taille_x and 0 <= ny < self.taille_y:
                        if self.grid[nx][ny].mine:
                            count += 1
                self.grid[x][y].adj = count

    def placement_mines(self):
        """
        Place des mines aléatoirement sur la grille en fonction du niveau de difficulté.

        Exceptions
        ----------
        ValueError
            Levée si le nombre de mines dépasse le nombre de cases dans la grille.
        """
        total_cells = self.taille_x * self.taille_y

        if self.dif > total_cells:
            raise ValueError("Nombre de mines trop élevé pour la taille de la grille")

        all_positions = [(x, y) for x in range(self.taille_x) for y in range(self.taille_y)]
        mine_positions = random.sample(all_positions, self.dif)

        for x, y in mine_positions:
            self.grid[x][y].toggle_mine()

    def reveal_all(self):
        """
        Révèle toutes les cases de la grille.
        """
        for x in range(self.taille_x):
            for y in range(self.taille_y):
                self.grid[x][y].reveal_case()
