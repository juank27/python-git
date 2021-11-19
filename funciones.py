def saludar():
   print("Hola a todos desde funcion saludar")

def suma_dos_numeros(a,b):
   return a + b

def potencia(base,potencia):
   resultado = base ** potencia
   return resultado

saludar()
numero_uno = int(input("Dijite el numero uno "))
numero_dos = int(input("Dijite el numero 2 "))
print("Mostrando la suma")
print(suma_dos_numeros(numero_uno,numero_dos))
print(potencia(2,5))


numero = int(input("Dijite un numero "))
print(type(numero))
print(numero * 5)
print("finalizo")

#condicional
def numero_al_cuadrado(numero,veces):
   resul = numero ** veces
   return resul 

print("El resultado del numero al cuadrado es: " , numero_al_cuadrado(4,5))