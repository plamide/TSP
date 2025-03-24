import tkinter as tk
import random


#####################################
###### GENERER UN GRAPHE #######
#####################################
import tkinter as tk

class Sommet:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.couleur = None
        self.voisins = {}  # Dictionnaire pour stocker les voisins et leurs poids

    def ajouter_voisin(self, id_voisin, poids):
        self.voisins[id_voisin] = poids


class Graphe:
    def __init__(self):
        self.sommets = {}  # Dictionnaire pour les sommets et leurs coordonnées
        self.aretes = {}   # Dictionnaire pour les arêtes avec poids (distances)

    def ajouter_sommet(self, id, x, y):
        """Ajoute un sommet avec des coordonnées (x, y)"""
        if id not in self.sommets:
            self.sommets[id] = Sommet(id, x, y)  # Création du sommet avec coordonnées

    def ajouter_arete(self, id1, id2, poids):
        """Ajoute une arête entre deux sommets avec un poids (distance)"""
        self.sommets[id1].ajouter_voisin(id2, poids)
        self.sommets[id2].ajouter_voisin(id1, poids)

    def obtenir_distance(self, id1, id2):
        """Retourne la distance entre deux sommets"""
        return self.sommets[id1].voisins[id2]

    def obtenir_voisins(self, id):
        """Retourne la liste des voisins d'un sommet"""
        return list(self.sommets[id].voisins.keys())
    
    def __str__(self):
        return f"Sommets: {self.sommets}\nArêtes: {self.aretes}"
    
    def colorier_graphe(self):
        """Colorier tous les sommets avec la même couleur"""
        couleur_unique = "red"  # ou toute autre couleur de ton choix
        for sommet in self.sommets.values():
            sommet.couleur = couleur_unique

    def afficher_tkinter(self):
        """Affiche le graphe avec Tkinter"""
        fenetre = tk.Tk()
        fenetre.title("Graphe avec Arêtes et Poids")

        canvas = tk.Canvas(fenetre, width=600, height=600, bg="white")
        canvas.pack()

        # Dessiner les arêtes avec poids
        for sommet in self.sommets.values():
            for voisin, poids in sommet.voisins.items():
                x1, y1 = sommet.x, sommet.y
                x2, y2 = self.sommets[voisin].x, self.sommets[voisin].y
                canvas.create_line(x1, y1, x2, y2, fill="black", width=2)

                # Calculer la position du texte du poids (centre de l'arête)
                mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
                offset = 10  # Ajustement pour que le texte ne chevauche pas l'arête
                canvas.create_text(mid_x + offset, mid_y - offset, text=str(poids), font=("Arial", 10, "bold"), fill="black")

        # Dessiner les sommets
        for sommet in self.sommets.values():
            canvas.create_oval(sommet.x - 20, sommet.y - 20, sommet.x + 20, sommet.y + 20, fill=sommet.couleur, outline="black")
            canvas.create_text(sommet.x, sommet.y, text=str(sommet.id), font=("Arial", 12, "bold"))

        fenetre.mainloop()






