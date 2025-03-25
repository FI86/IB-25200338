# Exemple : Creation et manipulation d'un tableau NumPy

# Import de la bibliotheque NumPy
import numpy as np

# Creation d'un tableau 1D (vecteur)
tableau_1d = np.array([1, 2, 3, 4, 5])

# Creation d'un tableau 2D (matrice)
tableau_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Affichage des tableaux
print("Tableau 1D :", tableau_1d)
print("Tableau 2D :\n", tableau_2d)

# Nombre de dimensions
print("Dimensions :", tableau_2d.ndim)

# Taille du tableau
print("Shape (lignes, colonnes) :", tableau_2d.shape)

# Nombre total de valeurs
print("Nombre total d'elements :", tableau_2d.size)

# Type des donnees
print("Type des elements :", tableau_2d.dtype)

# Acces a un element (ligne 1, colonne 2)
print("Element en (1, 2) :", tableau_2d[1, 2])

# Extraction d'une colonne complete
print("Deuxieme colonne :\n", tableau_2d[:, 1])

# Extraction d'une sous-matrice
print("Sous-matrice :\n", tableau_2d[0:2, 1:3])

# Ajoute 5 a chaque element
print("Addition :", tableau_1d + 5)

# Multiplie chaque element par 2
print("Multiplication :", tableau_1d * 2)

# Exponentielle de chaque element
print("Exponentielle :", np.exp(tableau_1d))

# Moyenne des valeurs du tableau
print("Moyenne :", np.mean(tableau_1d))

# Tableau rempli de zeros
zeros = np.zeros((3, 3))  
print("Tableau de zeros :\n", zeros)

# Tableau rempli de uns
uns = np.ones((2, 4))  
print("Tableau de uns :\n", uns)

# Tableau de valeurs aleatoires
aleatoire = np.random.rand(3, 3)  
print("Tableau aleatoire :\n", aleatoire)

# Matrice identite (1 en diagonales, 0 ailleurs)
identite = np.eye(4)  
print("Matrice identite :\n", identite)

# Definition de deux matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Produit matriciel
produit = np.dot(A, B)
print("Produit matriciel :\n", produit)
