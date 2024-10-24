from grille import Grille

class Minesweeper:
    def __init__(self, dif, taille_x, taille_y):
        """
        Constructeur de la classe minesweeper, qui represente le jeu

        Parameters
        ----------
        dif : int
            Nombre de mines. Indicateur de la difficulté
        taille_x : int
            Nombre de lignes du tableau
        taille_y : int
            Nombre de colonnes du tableau

        """
        self.dif = int(dif)
        self.taille_x = int(taille_x)
        self.taille_y = int(taille_y)
        self.grid = Grille(taille_x, taille_y, dif)
        self.grid.placement_mines()
        self.revealed_cells = 0  
    
    def reveal_cell(self, x, y):
        """
        Permet de révéle une case en fonction de ces coordonnées dans le tableau

        Parameters
        ----------
        x : int
            Première coordonnée de la case, réprésente l'indice de la ligne où se trouve la case
        y : int
            Deuxième coordonnée de la case, réprésente l'indice de la colonne où se trouve la case

        Returns
        -------
        bool
            Ce return permet de gérer la continuation ou non du jeu

        """
        if 0 <= x < self.taille_x and 0 <= y < self.taille_y:
            cell = self.grid.grid[x][y]
            
            if cell.reveal: 
                return True
            
            if cell.flag: 
                print("Cell is flagged. Unflag it first if you want to reveal.")
                return True
            
            if cell.mine:
                print("Boom! You hit a mine. Game over!")
                self.grid.reveal_all() 
                self.grid.show()
                return False
            
            cell.reveal_case()
            self.revealed_cells += 1 
            
            if cell.adj == 0:
                self.reveal_adjacent_cells(x, y)

            if self.check_win():
                print("Congratulations! You've won the game!")
                self.grid.show()  
                return False  
            
            self.grid.show()
            return True  
        else:
            print("Invalid coordinates.")
            return True 
    
    def reveal_adjacent_cells(self, x, y):
        """
        Fonction récursive qui révélé automatiquement les cases qui on un nombre d'adjacence 0 ainsi que toutes les
        cases adjacentes en fonction des coordonnées d'une case de départ

        Parameters
        ----------
        x : int
            Première coordonnée de la case, réprésente l'indice de la ligne où se trouve la case
        y : int
            Deuxième coordonnée de la case, réprésente l'indice de la colonne où se trouve la case

        """
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.taille_x and 0 <= ny < self.taille_y:
                neighbor = self.grid.grid[nx][ny]
                
                if not neighbor.reveal and not neighbor.flag:  
                    neighbor.reveal_case()
                    self.revealed_cells += 1
                    
                    if neighbor.adj == 0:
                        self.reveal_adjacent_cells(nx, ny)
    
    def toggle_flag(self, x, y):
        """
        Même que pour la fonction dans Case, gère aussi les coordonnées invalides

        Parameters
        ----------
        x : int
            Première coordonnée de la case, réprésente l'indice de la ligne où se trouve la case
        y : int
            Deuxième coordonnée de la case, réprésente l'indice de la colonne où se trouve la case

        """
        if 0 <= x < self.taille_x and 0 <= y < self.taille_y:
            self.grid.grid[x][y].toggle_flag()
            self.grid.show()
        else:
            print("Invalid coordinates.")

    def check_win(self):
        """
        Vérifie si le tableau est dans un étât ou le joueur a gagné

        Returns
        -------
        bool
            True si la partie est gagné, False sinon

        """
        total_cells = self.taille_x * self.taille_y
        return self.revealed_cells == total_cells - self.dif