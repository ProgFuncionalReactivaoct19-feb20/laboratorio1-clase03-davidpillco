"""
    file: problema1.py
    autor: davidpillco
"""
# Lista de las notas 
notas = [10,20,18,19,20,17,18,16,16,11,12,13]

# Se evalua las notas 
eval_notas = filter(lambda x: x > 16.5, notas)

# Se imprime como lista las notas 
print(list(eval_notas))

