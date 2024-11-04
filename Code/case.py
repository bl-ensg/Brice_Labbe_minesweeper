class Case:
    def __init__(self, pos_x, pos_y):
        """
        Initialise une instance de la classe Case représentant une case du jeu de démineur.

        Paramètres
        ----------
        pos_x : int
            Position X de la case.
        pos_y : int
            Position Y de la case.

        Attributs
        ---------
        pos_x : int
            Position X de la case.
        pos_y : int
            Position Y de la case.
        mine : bool
            Indique si la case contient une mine.
        reveal : bool
            Indique si la case est révélée.
        flag : bool
            Indique si la case est marquée avec un drapeau.
        adj : int
            Nombre de mines adjacentes.
        """
        self.pos_x = int(pos_x)
        self.pos_y = int(pos_y)
        self.mine = False
        self.reveal = False
        self.flag = False
        self.adj = 0

    def reveal_case(self):
        """
        Révèle la case en la marquant comme découverte.

        Modifie
        -------
        reveal : bool
            Passe à True pour indiquer que la case est révélée.
        """
        self.reveal = True

    def toggle_flag(self):
        """
        Bascule l'état du drapeau sur la case.

        Modifie
        -------
        flag : bool
            Inverse l'état actuel du drapeau.
        """
        self.flag = not self.flag

    def toggle_mine(self):
        """
        Bascule l'état de la mine dans la case.

        Modifie
        -------
        mine : bool
            Inverse l'état actuel de la mine.
        """
        self.mine = not self.mine
