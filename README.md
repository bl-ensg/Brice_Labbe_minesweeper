
# Minesweeper by Brice Labbe

Ce projet est une implémentation du célèbre jeu **Minesweeper** en Python. L'interface utilisateur permet de jouer avec une grille de taille personnalisable et un nombre de mines défini par l'utilisateur.

## Installation et Lancement

1. Clonez ou téléchargez ce dépôt.
2. Placez tous les fichiers du dossier `code` dans le même dossier sur votre machine. (fait par défaut lors du clonage normalement)
3. Assurez-vous d'avoir Python installé sur votre machine.

### Exécution du Jeu

Pour lancer le jeu, exécutez le fichier `Main.py` sur un terminal ou sur un IDE python tels que Spyder

## Instructions de Jeu

1. **Définir les paramètres** : Le jeu vous demandera d'entrer deux valeurs entières :
   - `size` : la taille de la grille (par exemple, 10 pour une grille 10x10).
   - `dif` : le nombre de mines que vous souhaitez placer sur la grille.
   
2. **Conditions et Exceptions** : 
   - Assurez-vous que `size` et `dif` sont des entiers.
   - Le nombre de mines (`dif`) doit être inférieur ou égal au nombre de cases disponibles (`size²`). Si ce n'est pas le cas, une exception sera levée.

3. **Interface de jeu** : Une fois les paramètres valides, l'interface de jeu s'ouvrira, et vous pourrez commencer à jouer.
   Les contrôles sont les mêmes que pour le démineur classique: Clic gauche pour révéler, Clic droit pour marquer.

5. **Redémarrage automatique** : En cas de victoire ou de défaite, une nouvelle partie sera automatiquement lancée avec les mêmes paramètres `size` et `dif`.

6. **Modifier les paramètres** : Pour changer les paramètres de la grille, fermez l'interface et relancez `Main.py`.

## Exigences

- Python 3.7 or later
- PyQt5 pour l'interface graphique

## Auteur

- Brice Labbe
