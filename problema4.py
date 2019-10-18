"""
    file: problema4.py
    autor: davidpillco
"""
# Evaluacion de las notas
def eval_notas(x):
    # Lista con lo que queremos incluir
    exc_notas = ["Regular", "Bueno"]
    # Evaluacion de la lista de notas 
    if x[3] in exc_notas:
        return True
    else:
        return False
# Lista de notas 
notas = [(5, 5, 10, "Regular"), (10, 2, 4, "Bueno"), (10, 1, 9, "Muy Bueno"), (7, 2, 3, "Sobresaliente")]

# Filtrar lo que queremos mostrar 
resultado = filter(eval_notas, notas)
# Print 
print(list(resultado))