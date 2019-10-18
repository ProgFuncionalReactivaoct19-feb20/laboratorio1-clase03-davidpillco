"""
    file: problema3.py
    autor: davidpillco
"""
# Se guarda es una variable la frase
frase= "No hay medicina que cure lo que no cura la felicidad"
# Variable con un espacio      
espacio = " "
# A la frase se la separa por el espacio
frase2 = frase.split(espacio)
# Se evalua el numero de letras de la frase 
resultado = filter(lambda x: len(x)<= 3, frase2)
# Se imprime la frase con las cadenas que fueron aceptadas
print(list(resultado))





