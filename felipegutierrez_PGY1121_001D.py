import os
os.system("cls")

escenario=[1,2,3,4,5,6,7,8,9,10,
           11,12,13,14,15,16,17,18,19,20,
           21,22,23,24,25,26,27,28,29,30,
           31,32,33,34,35,36,37,38,39,40,
           41,42,43,44,45,46,47,48,49,50,
           51,52,53,54,55,56,57,58,59,60,
           61,62,63,64,65,66,67,68,69,70,
           71,72,73,74,75,76,77,78,79,80,
           81,82,83,84,85,86,87,88,89,90,
           91,92,93,94,95,96,97,98,99,100]

platinum=[]
gold=[]
silver=[]
rut=[]


def comprar():
    while True:
        try:
            r=int(input("Ingrese su rut sin punto, sin guion y sin numero verificador\n"))
            if (r>=1111111 and r<=99999999):
                rut.append(r)
                break
            else:
                print("Rut no valido")
        except:
            print("no valido")
            
    while True:
        try:            
            cant=int(input("Cuantas entradas desea comprar (entre 1 a 3)\n"))
            if (cant>=1 and cant<=3):
                for i in range (cant):
                    mostrar()
                    print("\n")
                    while True:
                        try:
                            z=int(input("elija un lugar\n"))
                            if (z>=1 and z<=20):
                                platinum.append(1)
                                escenario.remove(z)
                                escenario.insert(z-1,0)
                                mostrar()
                                print("La operacion se ha realizado con exito")
                                break
                            elif(z>=21 and z<=50):
                                gold.append(1)
                                escenario.remove(z)
                                escenario.insert(z-1,0)
                                mostrar()
                                print("La operacion se ha realizado con exito")
                                break
                            elif(z>=51 and z<=100):
                                silver.append(1)
                                escenario.remove(z)
                                escenario.insert(z-1,0)
                                mostrar()
                                print("La operacion se ha realizado con exito")
                                break
                            elif(z==0):
                                print("No esta disponible")
                            else:
                                print("Asientos no existen")
                        except:
                            print("No valido")
                break
            else:
                print("Cantidad no valida")
        except:
            print("Error de datos")



def menu():
    print("""

1.- Comprar entradas
2.- Mostrar ubicaciones disponibles
3.- Ver listado de asistentes
4.- Mostrar ganancias totales
5.- Salir

""")

def mostrar():
    print("|---------------------------------------------------------|")
    print("|                        ESCENARIO                        |")
    print("|---------------------------------------------------------|")
    for i in range (len(escenario)):
        if escenario[i]%10!=0 or escenario[i]==0:
            print(f"|{escenario[i]:3d}|",end=" ")
        elif escenario[i]%10==0:
            print(f"|{escenario[i]:3d}|",end="\n")

def listado():
    print(rut)

def ganancias():
    print("|-------------------+----------+----------------|")
    print("|    Tipo entrada   | Cantidad |      Total     |")
    print("|-------------------+----------+----------------|")
    print(f"|Platinum $120.000  |{len(platinum):10d}| {120000*len(platinum):15d}|")
    print(f"|Platinum $80.000   |{len(gold):10d}| {80000*len(gold):15d}|")
    print(f"|Platinum $50.000   |{len(silver):10d}| {50000*len(silver):15d}|")
    print("|-------------------+----------+----------------|")
    print(f"|Total              |{len(platinum)+len(gold)+len(silver):10d}|{120000*len(platinum)+80000*len(gold)+50000*len(silver):16d}|")
    print("|-------------------+----------+----------------|")


while True:
    menu()
    try:
        opc=int(input("Ingrese una opcion: "))
        if(opc==1):
            comprar()
        elif(opc==2):
            mostrar()
        elif(opc==3):
            listado()
        elif(opc==4):
            ganancias()
        elif(opc==5):
            print("Felipe Gutierrez, 10-07-2023")
            break
        else:
            print("Opcion no valida")
    except:
        print("Error de datos")