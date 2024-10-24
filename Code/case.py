class Case:
    def __init__(self, pos_x, pos_y):
        """
        Constructeur de la classe Case, qui représente les case du tableau de jeu

        Parameters
        ----------
        pos_x : int
            indice de la ligne contenant la case dans le tableau
        pos_y : int
            indice de la colonne contenant la case dans le tableau

        """
        self.pos_x = int(pos_x)
        self.pos_y = int(pos_y)
        self.mine = False
        self.reveal = False
        self.flag = False
        self.adj = 0
    
    def reveal_case(self):
        """
        Révéle une case
        """
        self.reveal = True
        
    def toggle_flag(self):
        """
        Change le statut "flag" d'une case
        """
        self.flag = not self.flag
        
    def toggle_mine(self):
        """
        Change le statut "mine" d'une case
        utilisé uniquement à la création du jeu
        """
        self.mine = not self.mine
    
    def __str__(self):
        """
        Renvoie un string correspondant au statut d'une case
        utilisé lors de l'affichage du jeu dans la console
        """
        if self.reveal:
            if self.mine:
                return "M"
            elif self.adj > 0:
                return str(self.adj)
            else:
                return " "
        else:
            if self.flag:
                return "F"
            else:
                return "."
