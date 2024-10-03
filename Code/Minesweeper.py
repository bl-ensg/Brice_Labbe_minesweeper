# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 14:24:14 2024

@author: Formation
"""
import random

class Case:
    def __init__(self, pos_x, pos_y):
        self.pos_x = int(pos_x)
        self.pos_y = int(pos_y)
        self.mine = False
        self.reveal = False
        self.flag = False
        self.adj = 0
    
    def reveal_case(self):
        self.reveal = True
        
    def toggle_flag(self):
        self.flag = not self.flag
        
    def toggle_mine(self):
        self.mine = not self.mine
    
    def __str__(self):
        # If the cell is revealed
        if self.reveal:
            if self.mine:
                return "M" 
            elif self.adj > 0:
                return str(self.adj)
            else:
                return " "  # Empty space (can be changed to number of nearby mines)
        else:
            if self.flag:
                return "F"  
            else:
                return "."  


class Grille:
    def __init__(self, taille_x, taille_y, dif):
        self.taille_x = int(taille_x)
        self.taille_y = int(taille_y)
        self.dif = int(dif)
        self.grid = [[Case(x, y) for y in range(taille_y)] for x in range(taille_x)]
            
    def calc_adj(self):
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
        total_cells = self.taille_x * self.taille_y

        if self.dif > total_cells:
            raise ValueError("Too many mines for the grid size")

        all_positions = [(x, y) for x in range(self.taille_x) for y in range(self.taille_y)]

        mine_positions = random.sample(all_positions, self.dif)

        for x, y in mine_positions:
            self.grid[x][y].toggle_mine()  # Call toggle_mine instead of cases
            
        self.calc_adj()
                
    def reveal_all(self):
        for x in range(self.taille_x):
            for y in range(self.taille_y):
                self.grid[x][y].reveal_case()
    
    def show(self):
        for row in self.grid:
            print(" ".join(str(cell) for cell in row))
                
          

class Minesweeper:
    def __init__(self,dif,taille_x,taille_y):
        self.dif = int(dif)
        self.taille_x = int(taille_x)
        self.taille_y = int(taille_y)
        self.grid = Grille(taille_x,taille_y,dif)
        self.grid.placement_mines()
        
        
        
    


    

        
        
    
    