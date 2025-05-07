frutas = ["manzanas", "bananas","naranja"]

frutas.append("pera")
print (frutas)#imprime ["manzanas","banana","naranja","pera"]

frutas.insert(1,"uva")
print(frutas)#imprime ["manzanas","uva","banana","naranja","pera"]

frutas.remove("banana")
print(frutas)#imprime ["manzanas","uva","naranja","pera"]

fruta_eliminada = frutas.pop(2)
print(frutas)#imprime ["manzanas","uva","pera"]
print (fruta_eliminada)# imprime "naranja"

frutas.sort()
print(frutas)#["manzanas","pera","uva"]

frutas.reverse()
print(frutas) #imprime ["uva","pera","manzana"]

