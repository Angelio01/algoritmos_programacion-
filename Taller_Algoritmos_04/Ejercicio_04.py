"""
Entradas: ---

Salidas: 2 valores enteros uno que el dato en la posición 12 de la sucesión, y la suma de los 
primeros 12 valores de la sucesión

Posición 12 --> int --> A
Suma --> int --> B

"""

# Caja negra
B = 0
for i in range(12):
    A = 5*i + 6
    B = B + A
    
# Salidas
print("\nEl término doceavo en la suceción es:",A) 
print("La suma de los primeros 12 numeros de la sucesión es:",B,"\n") 
    