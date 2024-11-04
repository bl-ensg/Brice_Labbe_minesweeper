# minesweeper.py

from grille import Grille

class Minesweeper:
    def __init__(self, dif, taille_x, taille_y):
        """
        Initialise la classe Minesweeper qui gère la logique du jeu.

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
        grid : Grille
            Instance de la grille de jeu.
        """
        self.dif = int(dif)
        self.taille_x = int(taille_x)
        self.taille_y = int(taille_y)
        self.grid = Grille(taille_x, taille_y, dif)

    def reveal_cell(self, x, y):
        """
        Révèle une case de la grille. Si une mine est découverte, la partie se termine.

        Paramètres
        ----------
        x : int
            Position X de la case.
        y : int
            Position Y de la case.

        Retourne
        -------
        bool
            False si une mine est découverte (partie perdue), True sinon (continue la partie).
        """
        if 0 <= x < self.taille_x and 0 <= y < self.taille_y:
            cell = self.grid.grid[x][y]

            if cell.reveal or cell.flag:
                return True

            if cell.mine:
                self.grid.reveal_all()
                return False

            cell.reveal_case()

            if cell.adj == 0:
                self.reveal_adjacent_cells(x, y)

            return True
        else:
            return True

    def reveal_adjacent_cells(self, x, y):
        """
        Révèle de manière récursive les cases adjacentes si elles ne contiennent pas de mine
        et ont un nombre de mines adjacentes de zéro.

        Paramètres
        ----------
        x : int
            Position X de la case.
        y : int
            Position Y de la case.
        """
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.taille_x and 0 <= ny < self.taille_y:
                neighbor = self.grid.grid[nx][ny]
                if not neighbor.reveal and not neighbor.flag:
                    neighbor.reveal_case()
                    if neighbor.adj == 0:
                        self.reveal_adjacent_cells(nx, ny)

    def toggle_flag(self, x, y):
        """
        Ajoute ou retire un drapeau sur une case.

        Paramètres
        ----------
        x : int
            Position X de la case.
        y : int
            Position Y de la case.
        """
        if 0 <= x < self.taille_x and 0 <= y < self.taille_y:
            cell = self.grid.grid[x][y]
            if not cell.reveal:
                cell.toggle_flag()

    def check_victory(self):
        """
        Vérifie si toutes les conditions de victoire sont remplies.

        Retourne
        -------
        bool
            True si le joueur a gagné, False sinon.
        """
        for x in range(self.taille_x):
            for y in range(self.taille_y):
                cell = self.grid.grid[x][y]
                if cell.mine and not cell.flag:
                    return False
                if not cell.mine and not cell.reveal:
                    return False
        return True

    def reset_game(self):
        """
        Réinitialise la grille pour démarrer une nouvelle partie.
        """
        self.grid = Grille(self.taille_x, self.taille_y, self.dif)
