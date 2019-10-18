"""
    file: problema5.py
    autor: davidpillco
"""
# Evaluacion de las edades
def eval_edades(x):
    # Edades que queremos excluir
    exc_edades = [10, 14, 30, 32, 40, 16]
    if x in exc_edades:
        return False
    else:
        return True
# Lista de edades
edades = [10, 12, 13, 14, 16, 18, 20, 30, 31, 32, 33, 40, 50]

# Fitra las edades que si queremos mostrar
resultado = filter(eval_edades, edades)

# Print final
print(list(resultado))
