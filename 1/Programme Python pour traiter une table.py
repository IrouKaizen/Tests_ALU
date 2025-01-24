# Programme Python pour traiter un tableau de "n" nombres entiers et 
# afficher les nombres distincts avec leurs fréquences correspondantes.

# Fonction pour calculer les fréquences des nombres distincts
def compter_frequences(nombres):
    frequences = {}
    for nombre in nombres:
        if nombre in frequences:
            frequences[nombre] += 1
        else:
            frequences[nombre] = 1
    return frequences

# Fonction principale
if __name__ == "__main__":
    print("Bienvenue dans le programme de comptage des nombres distincts!")
    
    # Demander à l'utilisateur d'entrer la taille du tableau
    n = int(input("Entrez le nombre d'éléments dans le tableau: "))
    
    # Vérifier que la taille est positive
    if n <= 0:
        print("La taille du tableau doit être un nombre positif.")
    else:
        # Lire les nombres depuis l'utilisateur
        print(f"Entrez {n} nombres entiers :")
        tableau = []
        for i in range(n):
            nombre = int(input(f"Nombre {i+1}: "))
            tableau.append(nombre)
        
        # Calculer les fréquences des nombres distincts
        resultats = compter_frequences(tableau)
        
        # Afficher les résultats
        print("\nNombres distincts et leurs fréquences :")
        for nombre, frequence in resultats.items():
            print(f"Nombre: {nombre}, Fréquence: {frequence}")
