import random
from case import Case  

class Grille:
    def __init__(self, taille_x, taille_y, dif):
        """
        Constructeur de la classe Grille, qui représente le tableau de jeu

        Parameters
        ----------
        taille_x : int
            Nombre de lignes du tableau
        taille_y : int
            Nombre de colonnes du tableau
        dif : int
            Nombre de mines dans le tableau, indicateur de difficulté

        """
        self.taille_x = int(taille_x)
        self.taille_y = int(taille_y)
        self.dif = int(dif)
        self.grid = [[Case(x, y) for y in range(taille_y)] for x in range(taille_x)]
            
    def calc_adj(self):
        """
        Calcule la valeur d'adjacence des cases du tableau (le nombre de mines dans le voisinage des case)
        S'applique a l'entiéreté du tableau
        
        """
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        
        for x in range(self.taille_x):
            for y in range(self.taille_y):
                S = 0
                for dx,dy in directions:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < self.taille_x and 0 <= ny < self.taille_y:
                        if self.grid[nx][ny].mine:
                            S += 1
                self.grid[x][y].adj = S
    
    def placement_mines(self):
        """
        Place les mines dans le tableau en fonction de dif
        

        Raises
        ------
        ValueError
            Renvoie une erreur lorsqu'il y a trop de mine pour la taille choisie

        """
        total_cells = self.taille_x * self.taille_y

        if self.dif > total_cells:
            raise ValueError("Too many mines for the grid size")

        all_positions = [(x, y) for x in range(self.taille_x) for y in range(self.taille_y)]

        mine_positions = random.sample(all_positions, self.dif)

        for x, y in mine_positions:
            self.grid[x][y].toggle_mine() 
            
        self.calc_adj()
                
    def reveal_all(self):
        """
        Révéle toutes les cases
        utilisé en fin de partie en cas de défaite
        """
        for x in range(self.taille_x):
            for y in range(self.taille_y):
                self.grid[x][y].reveal_case()
    
    def show(self):
        """
        Permet l'affichage dans la console du tableau de jeu

        """
        for row in self.grid:
            print(" ".join(str(cell) for cell in row))
