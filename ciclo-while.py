#ciclo while
print("Iniciando")
i = 0
while (i <= 6):
    print(i)
    i = i + 1

# modificando wl while
print("while modificado")
j = 0
bandera = True
while (bandera):
    #print("Entre una vez al cilco modificado")
    j = int(input("Dijite un numero: "))
    print(j)
    #j = j + 1
    if(j == 3):
        bandera = False