import tkinter as tk
import random


#####################################
###### CLASSE DES FOURMIS #######
#####################################

class Ant:
    def __init__(self, graphe, start_city):
        self.graphe = graphe  # Le graphe avec les villes et les arêtes
        self.start_city = start_city  # La ville de départ
        self.tour = [start_city]  # Liste des villes visitées, commence avec la ville de départ
        self.total_distance = 0  # Distance totale parcourue
        self.visited = set([start_city])  # Ensemble des villes déjà visitées (pour éviter les répétitions)
    
    def __str__(self):
        return f"Tour: {self.tour} Distance: {self.total_distance}"

    def choose_next_city(self, pheromones, alpha, beta):
        """Choisir la prochaine ville en fonction des phéromones et des distances"""
        current_city = self.tour[-1]
        unvisited_cities = [city for city in self.graphe.obtenir_voisins(current_city) if city not in self.visited]

        probabilities = []
        total_pheromone = 0

        # Calcul des probabilités de choix de chaque ville
        for city in unvisited_cities:
            distance = self.graphe.obtenir_distance(current_city, city)
            pheromone = pheromones[current_city][city] ** alpha  # Influence des phéromones
            visibility = (1.0 / distance) ** beta  # Influence de la visibilité (inverse de la distance)
            total_pheromone += pheromone * visibility
            probabilities.append((city, pheromone * visibility))

        # Normalisation des probabilités
        probabilities = [(city, prob / total_pheromone) for city, prob in probabilities]

        # Choisir la prochaine ville en fonction des probabilités
        r = random.random()
        cumulative_probability = 0.0
        for city, probability in probabilities:
            cumulative_probability += probability
        if cumulative_probability >= r:
            return city

        return unvisited_cities[0]  # Si aucune ville n'a été choisie, choisir la première ville restante

    def construct_tour(self, pheromones, alpha, beta):
        """Construire un tour complet en choisissant les villes une par une"""
        while len(self.visited) < len(self.graphe.sommets):
            next_city = self.choose_next_city(pheromones, alpha, beta)
            self.visited.add(next_city)
            self.tour.append(next_city)
            self.total_distance += self.graphe.obtenir_distance(self.tour[-2], next_city)

    def update_pheromones(self, pheromones, rho):
        """Mettre à jour les phéromones en fonction du parcours de la fourmi"""
        for i in range(1, len(self.tour)):
            city1 = self.tour[i - 1]
            city2 = self.tour[i]
            pheromones[city1][city2] += 1.0 / self.total_distance
            pheromones[city2][city1] += 1.0 / self.total_distance
