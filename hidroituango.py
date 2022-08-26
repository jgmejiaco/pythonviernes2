#nivel de agua

nivelAgua = int(input("Digita el niveld de agua "))

#Condiciones multiples

if(nivelAgua >= 0 and nivelAgua < 20):

    print(f'Nivel de agua bajo {nivelAgua}')

elif(nivelAgua >= 20 and nivelAgua < 400):

    print(f'Nivel de agua optimo {nivelAgua}')

elif(nivelAgua >= 400):

    print(f'Nivel de agua alto {nivelAgua}')

else:

    print(f'Nivel de agua inválido')