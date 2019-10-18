"""
    file: problema2.py
    autor: davidpillco
"""
# Lista de las notas 
notas = [(5, 5, 10), (10, 2, 4), (10, 1, 9), (10, 2, 3)]

# Se suma las notas 
suma = lambda x: (x[0] + x[1] + x[2])

# Print, y se le coloca el map para recorrer
print(list(map(suma, notas)))
