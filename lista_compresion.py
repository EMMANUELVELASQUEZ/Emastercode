secuencia = [1, 2, 3, 4, 5]  # Define secuencia as a list of numbers
nueva_lista = [elemento * 2 for elemento in secuencia if elemento % 2 == 0]  # Example expression and condition

numeros=[1,2,3,4,5]
cuadrados = [x**2 for x in numeros if x % 2 == 0]

print(cuadrados)#imprime[4,16]
