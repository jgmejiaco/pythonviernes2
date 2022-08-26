#nivel de agua

mes = input("Ingrese el mes ")

#Condiciones multiples

if(mes == "enero" or mes == "febrero" or mes == "marzo"):

    print(f'Estamos en Otoño {mes}')

elif(mes == "abril" or mes == "mayo" or mes == "junio"):

    print(f'Estamos en Primavera {mes}')

elif(mes == "julio" or mes == "agosto" or mes == "septiembre"):

    print(f'Estamos en Verano {mes}')

elif(mes == "octubre" or mes == "noviembre" or mes == "diciembre"):

    print(f'Estamos en Otoño {mes}')

else:

    print(f'Ingrese un mes correcto')