# Aide-mémoire Python pour débutants

## Table des matières
1. [Bases du langage](#bases-du-langage)
2. [Variables et types](#variables-et-types)
3. [Opérateurs](#opérateurs)
4. [Structures de contrôle](#structures-de-contrôle)
5. [Structures de données](#structures-de-données)
6. [Fonctions](#fonctions)
7. [Gestion des erreurs](#gestion-des-erreurs)
8. [Fichiers](#fichiers)
9. [Modules et imports](#modules-et-imports)
10. [Bonnes pratiques](#bonnes-pratiques)

---

## Bases du langage

### Premier programme
```python
# Afficher du texte
print("Hello World!")

# Commentaire sur une ligne
"""
Commentaire
sur plusieurs
lignes
"""
```

### Indentation (très important !)
Python utilise l'indentation pour délimiter les blocs de code :
```python
# CORRECT
if True:
    print("Ceci est dans le bloc if")
    print("Ceci aussi")

# INCORRECT - IndentationError
if True:
print("Erreur d'indentation")
```

---

## Variables et types

### Déclaration et affectation
```python
# Python détermine automatiquement le type
nom = "Alice"          # str (chaine)
age = 25               # int (entier)
taille = 1.65          # float (décimal)
est_etudiant = True    # bool (booléen)
```

### Types de base
```python
# Chaines de caractères
texte = "Bonjour"
texte2 = 'Monde'
texte_long = """Texte
sur plusieurs
lignes"""

# Nombres
entier = 42
decimal = 3.14
complexe = 2 + 3j

# Booléens
vrai = True
faux = False
```

### Vérifier le type
```python
nom = "Alice"
print(type(nom))             # <class 'str'>
print(isinstance(nom, str))  # True
```

---

## Opérateurs

### Arithmétiques
```python
a, b = 10, 3

addition = a + b           # 13
soustraction = a - b       # 7
multiplication = a * b     # 30
division = a / b           # 3.333...
division_entiere = a // b  # 3
modulo = a % b             # 1
puissance = a ** b         # 1000
```

### Comparaison
```python
a, b = 5, 3

egal = a == b           # False
different = a != b      # True
superieur = a > b       # True
inferieur = a < b       # False
sup_egal = a >= b       # True
inf_egal = a <= b       # False
```

### Logiques
```python
# ET, OU, NON
resultat = True and False   # False
resultat = True or False    # True
resultat = not True         # False
```

### Chaines de caractères
```python
nom = "Alice"
prenom = "Dupont"

# Concaténation
nom_complet = nom + " " + prenom    # "Alice Dupont"

# f-strings (recommandé Python 3.6+)
message = f"Bonjour {nom}, vous avez {age} ans"

# Méthodes utiles
texte = "  Python  "
print(texte.upper())            # "  PYTHON  "
print(texte.lower())            # "  python  "
print(texte.strip())            # "Python"
print(texte.replace("P", "J"))  # "  Jython  "
```

---

## Structures de contrôle

### Conditions (if/elif/else)
```python
age = 18

if age < 13:
    print("Enfant")
elif age < 18:
    print("Adolescent")
else:
    print("Adulte")

# Condition ternaire
statut = "majeur" if age >= 18 else "mineur"
```

### Boucles

#### Boucle for
```python
# Parcourir une séquence
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):       # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8
    print(i)

# Parcourir une liste
fruits = ["pomme", "banane", "orange"]
for fruit in fruits:
    print(fruit)

# Avec index
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

#### Boucle while
```python
compteur = 0
while compteur < 5:
    print(compteur)
    compteur += 1

# Boucle infinie (attention !)
# while True:
#     print("Infini")
```

#### Contrôle de boucle
```python
for i in range(10):
    if i == 3:
        continue    # Passer à l'itération suivante
    if i == 7:
        break       # Sortir de la boucle
    print(i)        # Affiche: 0, 1, 2, 4, 5, 6
```

---

## Structures de données

### Listes (tableaux modifiables)
```python
# Création
ma_liste = [1, 2, 3, 4, 5]
liste_mixte = [1, "texte", 3.14, True]
liste_vide = []

# Acces aux éléments
premier = ma_liste[0]       # 1
dernier = ma_liste[-1]      # 5
tranche = ma_liste[1:3]     # [2, 3]

# Modification
ma_liste[0] = 10            # [10, 2, 3, 4, 5]
ma_liste.append(6)          # [10, 2, 3, 4, 5, 6]
ma_liste.insert(1, 99)      # [10, 99, 2, 3, 4, 5, 6]
element = ma_liste.pop()    # Enlève et retourne le dernier
ma_liste.remove(99)         # Enlève la première occurrence de 99

# Méthodes utiles
taille = len(ma_liste)
ma_liste.sort()                    # Trie sur place
nouvelle_liste = sorted(ma_liste)  # Retourne une nouvelle liste triée
```

### Tuples (tableaux non modifiables)
```python
# Création
mon_tuple = (1, 2, 3)
tuple_simple = 1, 2, 3      # Parentheses optionnelles
tuple_vide = ()
tuple_un_element = (1,)     # Virgule obligatoire !

# Acces (comme les listes)
premier = mon_tuple[0]

# Les tuples sont immutables
# mon_tuple[0] = 10  # TypeError !
```

### Dictionnaires (clé-valeur)
```python
# Création
personne = {
    "nom": "Dupont",
    "prenom": "Alice",
    "age": 25
}
dict_vide = {}

# Accès
nom = personne["nom"]                   # "Dupont"
age = personne.get("age", 0)            # 25 (0 si clé absente)

# Modification
personne["age"] = 26
personne["ville"] = "Paris"             # Nouvelle clé

# Parcours
for cle in personne:
    print(f"{cle}: {personne[cle]}")

for cle, valeur in personne.items():
    print(f"{cle}: {valeur}")

# Méthodes utiles
cles = list(personne.keys())            # ["nom", "prenom", "age", "ville"]
valeurs = list(personne.values())       # ["Dupont", "Alice", 26, "Paris"]
```

### Sets (ensembles - valeurs uniques)
```python
# Création
mon_set = {1, 2, 3, 3, 3}   # {1, 2, 3} - pas de doublons
set_vide = set()            # {} crée un dict vide !

# Opérations
mon_set.add(4)              # {1, 2, 3, 4}
mon_set.remove(2)           # {1, 3, 4}

# Opérations d'ensembles
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union = set1 | set2          # {1, 2, 3, 4, 5}
intersection = set1 & set2   # {3}
difference = set1 - set2     # {1, 2}
```

---

## Fonctions

### Définition et appel
```python
# Fonction simple
def saluer():
    print("Bonjour !")

saluer()  # Appel

# Fonction avec parametres
def saluer_personne(nom, age):
    print(f"Bonjour {nom}, vous avez {age} ans")

saluer_personne("Alice", 25)

# Fonction avec valeur de retour
def additionner(a, b):
    return a + b

resultat = additionner(3, 5)  # 8
```

### Paramètres par défaut
```python
def saluer(nom, message="Bonjour"):
    print(f"{message} {nom}")

saluer("Alice")              # "Bonjour Alice"
saluer("Bob", "Salut")       # "Salut Bob"
```

### Arguments nommés
```python
def presenter(nom, age, ville):
    print(f"Je suis {nom}, j'ai {age} ans et j'habite à {ville}")

# Appel avec arguments nommés (ordre libre)
presenter(age=25, nom="Alice", ville="Paris")
```

### Arguments variables
```python
# *args pour arguments positionnels
def somme(*nombres):
    return sum(nombres)

print(somme(1, 2, 3, 4))     # 10

# **kwargs pour arguments nommés
def afficher_infos(**infos):
    for cle, valeur in infos.items():
        print(f"{cle}: {valeur}")

afficher_infos(nom="Alice", age=25, ville="Paris")
```

### Fonctions lambda (anonymes)
```python
# Fonction lambda simple
carre = lambda x: x ** 2
print(carre(5))              # 25

# Utilisation avec map, filter
nombres = [1, 2, 3, 4, 5]
carres = list(map(lambda x: x**2, nombres))     # [1, 4, 9, 16, 25]
pairs = list(filter(lambda x: x % 2 == 0, nombres))  # [2, 4]
```

---

## Gestion des erreurs

### Try/Except
```python
# Gestion d'erreur simple
try:
    nombre = int(input("Entrez un nombre: "))
    resultat = 10 / nombre
    print(f"Résultat: {resultat}")
except ValueError:
    print("Ce n'est pas un nombre valide")
except ZeroDivisionError:
    print("Division par zéro impossible")
except Exception as e:
    print(f"Erreur inattendue: {e}")
else:
    print("Tout s'est bien passé")
finally:
    print("Cette ligne s'exécute toujours")
```

### Lancer des erreurs
```python
def diviser(a, b):
    if b == 0:
        raise ValueError("Le diviseur ne peut pas être zéro")
    return a / b

try:
    resultat = diviser(10, 0)
except ValueError as e:
    print(f"Erreur: {e}")
```

---

## Fichiers

### Lecture
```python
# Lecture complète
with open("fichier.txt", "r", encoding="utf-8") as f:
    contenu = f.read()
    print(contenu)

# Lecture ligne par ligne
with open("fichier.txt", "r", encoding="utf-8") as f:
    for ligne in f:
        print(ligne.strip())  # strip() enlève le \n

# Lecture de toutes les lignes
with open("fichier.txt", "r", encoding="utf-8") as f:
    lignes = f.readlines()
```

### Écriture
```python
# Écriture (écrase le fichier)
with open("fichier.txt", "w", encoding="utf-8") as f:
    f.write("Première ligne\n")
    f.write("Deuxième ligne\n")

# Ajout à la fin
with open("fichier.txt", "a", encoding="utf-8") as f:
    f.write("Ligne ajoutée\n")

# Écriture de plusieurs lignes
lignes = ["Ligne 1\n", "Ligne 2\n", "Ligne 3\n"]
with open("fichier.txt", "w", encoding="utf-8") as f:
    f.writelines(lignes)
```

---

## Modules et imports

### Import de modules
```python
# Import complet
import math
print(math.pi)               # 3.14159...
print(math.sqrt(16))         # 4.0

# Import spécifique
from math import pi, sqrt
print(pi)                    # 3.14159...
print(sqrt(16))              # 4.0

# Import avec alias
import math as m
print(m.pi)

from math import pi as PI
print(PI)

# Import de tout (déconseillé)
from math import *
```

### Modules utiles pour débutants
```python
# Mathématiques
import math
import random

# Dates et heures
import datetime
from datetime import date, time

# Système et fichiers
import os
import sys

# Expressions régulières
import re

# JSON
import json

# Requêtes HTTP
import requests  # Module externe (pip install requests)
```

### Créer son propre module
```python
# fichier: mon_module.py
def ma_fonction():
    return "Hello from module"

CONSTANTE = 42

# fichier: main.py
import mon_module
print(mon_module.ma_fonction())
print(mon_module.CONSTANTE)
```

---

## Bonnes pratiques

### Nommage
```python
# Variables et fonctions : snake_case
nom_utilisateur = "Alice"
age_utilisateur = 25

def calculer_moyenne(notes):
    return sum(notes) / len(notes)

# Constantes : UPPER_CASE
PI = 3.14159
MAX_TENTATIVES = 3

# Classes : PascalCase (pour plus tard)
class PersonneUtilisateur:
    pass
```

### PEP 8 (Style Guide)
```python
# Espaces autour des opérateurs
a = b + c               # Correct
a=b+c                   # Incorrect

# Pas d'espaces avant les parenthèses de fonction
print("hello")          # Correct
print ("hello")         # Incorrect

# Lignes maximum 79 caractères
# Si trop long, couper ainsi :
message = ("Ceci est un très long message qui dépasse "
           "la limite de 79 caractères par ligne")

# Imports en haut du fichier
import sys
import os
from math import pi
```