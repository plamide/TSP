import tkinter as tk
import random

#####################################
###### TEST #######
#####################################
# Créer un graphe avec des villes et des arêtes
graphe = Graphe()

# Ajouter des sommets avec leurs coordonnées (x, y)
graphe.ajouter_sommet(0, 0, 0)
graphe.ajouter_sommet(1, 1, 0)
graphe.ajouter_sommet(2, 1, 1)
graphe.ajouter_sommet(3, 0, 1)

# Ajouter des arêtes entre les sommets avec des poids (distances)
graphe.ajouter_arete(0, 1, 1)
graphe.ajouter_arete(1, 2, 1)
graphe.ajouter_arete(2, 3, 1)
graphe.ajouter_arete(3, 0, 1)
graphe.ajouter_arete(0, 2, 1.5)
graphe.ajouter_arete(1, 3, 1.5)

# Initialiser les phéromones (valeurs initiales faibles)
pheromones = {city: {neighbor: 0.1 for neighbor in graphe.obtenir_voisins(city)} for city in graphe.sommets}

# Paramètres de l'algorithme
alpha = 1  # Poids des phéromones
beta = 2   # Poids de la visibilité (inverse de la distance)
rho = 0.5  # Taux d'évaporation des phéromones

# Créer une fourmi et lui faire construire un tour
ant = Ant(graphe, start_city=0)
ant.construct_tour(pheromones, alpha, beta)

# Afficher le tour et la distance totale
print(ant)

# Mise à jour des phéromones après que la fourmi ait fait son tour
ant.update_pheromones(pheromones, rho)

# Affichage des phéromones après mise à jour
print(pheromones)

# Coloration du graphe
graphe.colorier_graphe()

# Affichage avec Tkinter
graphe.afficher_tkinter()