import sys
import random
import string
import pickle
 
def nivel1():
    matriz=[]
    matriz2=[]
    Horizontal=5
    Vertical=5
    n = 3
    print('')
    for i in range (Vertical):
        lista = []
        for j in range (Horizontal):
            lista.append ('-')
        matriz.append (lista)
    def CrearMatriz():
        for r in matriz:
            for d in r:
                print(d, end='   ')
            print()
    def CrearMatrizCompleta(matriz2):
        for r in matriz2:
            for d in r:
                print(d, end='   ')
            print()
    def horizontal (x):
        ubi = True
        if len(x) <= len(matriz):
            while ubi == True:
                inicioColumna = random.randint(0,Horizontal-len(x))                
                inicioFila = random.randint(0,Vertical-1) 
                a = matriz[inicioFila][inicioColumna]
                cont=0
                si = 0
                a=inicioColumna
                contador=inicioColumna
                for letra in x:
                    if matriz[inicioFila][contador]=='-':
                        si+= 1
                        contador+=1
                if si == len(x):
                    lista5=[inicioFila,inicioColumna]
                    ubi = False
            for letra in x:
                matriz[inicioFila][a+cont] = letra   
                cont+=1 
    def vertical (x):
        ubi = True
        if len(x) <= len(matriz):
            while ubi == True:
                inicioColumna = random.randint(0,Horizontal-1)           
                inicioFila = random.randint(0,Vertical-len(x)) 
                a = matriz[inicioFila][inicioColumna]
                cont=0
                si = 0
                a=inicioFila
                contador=inicioFila
                for letra in x:
                    if matriz[contador][inicioColumna]=='-':
                        si+= 1
                        contador+=1
                if si == len(x):
                    lista5=[inicioFila,inicioColumna]
                    ubi = False
            for letra in x:
                matriz[a+cont][inicioColumna] = letra   
                cont+=1  
    def VerticalInversa(x):
        a = x[::-1]
        vertical (a)
    def HorizontalInversa(x):
        a = x[::-1]
        horizontal (a)   
    lista = ['sol', 'pez', 'mago','cafe','pato','casa','bota']
    lista2 =[]
    lista3 = []
    while len(lista2) < n:
        b = random.randint (0,(len(lista))-1) #Como hacer que escoja al azar los elementos de una lista
        if lista[b] not in lista2:
            lista2.append(lista [b])
    if n < 4:
        for i in range (0,n):
            if i == 0:
                horizontal(lista2 [0])
                lista2.remove(lista2[0])
                #CrearMatriz()
            elif i == 1:
                vertical (lista2 [0])
                lista2.remove(lista2[0])
                #CrearMatriz()
            elif i == 2:
                HorizontalInversa(lista2 [0])
                lista2.remove(lista2[0])
                #CrearMatriz()    
    else:
         for i in range (0,4):
            if i == 0:
                horizontal(lista2 [0])
                lista2.remove(lista2[0])
                #CrearMatriz()
            elif i == 1:
                vertical (lista2 [0])
                lista2.remove(lista2[0])
                #CrearMatriz()
            elif i == 2:
                HorizontalInversa(lista2 [0])
                lista2.remove(lista2[0])
                #CrearMatriz()
            elif i == 3:
                VerticalInversa (lista2 [0])
                lista2.remove(lista2[0])
                #CrearMatriz()
    for i in lista2:
        a = random.randint(0,3)
        if a == 0:
            horizontal(i)
            CrearMatriz()
        elif a == 1:
            vertical (i)
            CrearMatriz()
        elif a == 2:
            HorizontalInversa (i)
            CrearMatriz()
        elif a == 3:
            VerticalInversa (i)
            CrearMatriz()
            
    def puntos():
        point=0
        for i in range(0,3):
            HVOI=input("\n¿En que direccion esta tu palabra (Horizontal , vertical, horizontal inversa o vertical inversa)?: ")
            if HVOI == 'horizontal':
                Posx=int(input('Dame la primera posicion x de tu palabra: '))
                Posy=int(input('Dame la primera posicion y de tu palabra: '))
                Posx2=int(input('\nDame la ultima posicion x de tu palabra: '))
                Posy2=int(input('Dame la ultima posicion y de tu palabra: '))
                PI = matriz2[Posy][Posx]
                PF = matriz2[Posy2][Posx2]
                cont=Posx
                palabra=[]
                for i in range(0,Posx2-Posx+1):
                    palabra.extend(matriz2[Posy][cont])
                    cont+=1
                palabraEnLista=''.join([str(elem) for elem in palabra]) 
                if palabraEnLista in lista:
                     point+=1
                print('')
                CrearMatrizCompleta(matriz2)
                print('La palabra es: ', palabraEnLista)
                print('PUNTOS: ', point)
                guardar = input("***¿Quieres guardar el juego? ('Si' o 'No')***: ")
                if guardar == 'Si':
                    pickle.dump(matriz2, open('JuegoGuardado.dat', 'wb'))
                    return
                else:
                    pass

            elif HVOI == 'vertical':
                VPosx=int(input('\nDame la primera posicion x de tu palabra: '))
                VPosy=int(input('Dame la primera posicion y de tu palabra: '))
                VPosx2=int(input('\nDame la ultima posicion x de tu palabra: '))
                VPosy2=int(input('Dame la ultima posicion y de tu palabra: '))
                VPI = matriz2[VPosy][VPosx]
                VPF = matriz2[VPosy2][VPosx2]
                Vcont=VPosy
                Vpalabra=[]
                for j in range(0,VPosy2-VPosy+1):
                    Vpalabra.extend(matriz2[Vcont][VPosx])
                    Vcont+=1
                VpalabraEnLista=''.join([str(elem2) for elem2 in Vpalabra]) 
                if VpalabraEnLista in lista:
                     point+=1
                print('')
                CrearMatrizCompleta(matriz2)
                print('La palabra es: ', VpalabraEnLista)
                print('PUNTOS: ', point)
                guardar2 = input("***¿Quieres guardar el juego? ('Si' o 'No')***: ")
                if guardar2 == 'Si':
                    pickle.dump(matriz2, open('JuegoGuardado.dat', 'wb'))
                    return
                else:
                    pass

            elif HVOI == 'horizontal i':
                HIPosx=int(input('\nDame la primera posicion x de tu palabra: '))
                HIPosy=int(input('Dame la primera posicion y de tu palabra: '))
                HIPosx2=int(input('\nDame la ultima posicion x de tu palabra: '))
                HIPosy2=int(input('Dame la ultima posicion y de tu palabra: '))
                HIPI = matriz2[HIPosy][HIPosx]
                HIPF = matriz2[HIPosy2][HIPosx2]
                HIcont=HIPosx
                HIpalabra=[]
                for k in range(0,HIPosx2-HIPosx+1):
                    HIpalabra.extend(matriz2[HIPosy][HIcont])
                    HIcont-=1
                print(HIpalabra)
                HIpalabraEnLista=''.join([str(elem3) for elem3 in HIpalabra]) 
                if HIpalabraEnLista in lista:
                     point+=1
                print('')
                CrearMatrizCompleta(matriz2)
                print('La palabra es: ', HIpalabraEnLista)
                print('PUNTOS: ', point)
                guardar3 = input("***¿Quieres guardar el juego? ('Si' o 'No')***: ")
                if guardar3 == 'Si':
                    pickle.dump(matriz2, open('JuegoGuardado.dat', 'wb'))
                    return
                else:
                    pass
                
            elif HVOI == 'vertical i':
                VIPosx=int(input('\nDame la primera posicion x de tu palabra: '))
                VIPosy=int(input('Dame la primera posicion y de tu palabra: '))
                VIPosx2=int(input('\nDame la ultima posicion x de tu palabra: '))
                VIPosy2=int(input('Dame la ultima posicion y de tu palabra: '))
                VIPI = matriz2[VIPosy][VIPosx]
                VIPF = matriz2[VIPosy2][VIPosx2]
                VIcont=VIPosy
                VIpalabra=[]
                VIpalabra2=str()
                for l in range(0,VIPosy2-VIPosy+1):
                    VIpalabra.extend(matriz2[VIcont][VIposx])
                    VIcont-=1
                VIpalabraEnLista=''.join([str(elem4) for elem4 in VIpalabra]) 
                if VIpalabraEnLista in lista:
                     point+=1
                print('')
                CrearMatrizCompleta(matriz2)
                print('La palabra es: ', VIpalabraEnLista)
                print('')
        if point == 3:
            print('PUNTOS TOTALES: ', point)
            print('$$$ GANASTE $$$')
        else:
            print('Intentelo de nuevo.')

    def TableroCompleto(matriz):
        for i in matriz:
            lista =[]
            for dato in i:
                if dato == '-':
                    dato = random.choice (string.ascii_lowercase)
                    lista.append(dato)
                else:
                    lista.append(dato)  
            matriz2.append(lista)      
        CrearMatrizCompleta(matriz2)
    TableroCompleto(matriz)
    puntos()
    
def nivel2():
    matriz=[]
    matriz2=[]
    Horizontal=10
    Vertical=10
    n = 4
    print('')
    for i in range (Vertical):
        lista = []
        for j in range (Horizontal):
            lista.append ('-')
        matriz.append (lista)
    def CrearMatriz():
        for r in matriz:
            for d in r:
                print(d, end='   ')
            print()
    def CrearMatrizCompleta(matriz2):
        for r in matriz2:
            for d in r:
                print(d, end='   ')
            print()
    def horizontal (x):
        ubi = True
        if len(x) <= len(matriz):
            while ubi == True:
                inicioColumna = random.randint(0,Horizontal-len(x))                
                inicioFila = random.randint(0,Vertical-1) 
                a = matriz[inicioFila][inicioColumna]
                cont=0
                si = 0
                a=inicioColumna
                contador=inicioColumna
                for letra in x:
                    if matriz[inicioFila][contador]=='-':
                        si+= 1
                        contador+=1
                if si == len(x):
                    lista5=[inicioFila,inicioColumna]
                    ubi = False
            for letra in x:
                matriz[inicioFila][a+cont] = letra   
                cont+=1 
    def vertical (x):
        ubi = True
        if len(x) <= len(matriz):
            while ubi == True:
                inicioColumna = random.randint(0,Horizontal-1)           
                inicioFila = random.randint(0,Vertical-len(x)) 
                a = matriz[inicioFila][inicioColumna]
                cont=0
                si = 0
                a=inicioFila
                contador=inicioFila
                for letra in x:
                    if matriz[contador][inicioColumna]=='-':
                        si+= 1
                        contador+=1
                if si == len(x):
                    lista5=[inicioFila,inicioColumna]
                    ubi = False
            for letra in x:
                matriz[a+cont][inicioColumna] = letra   
                cont+=1  
    def VerticalInversa(x):
        a = x[::-1]
        vertical (a)
    def HorizontalInversa(x):
        a = x[::-1]
        horizontal (a)   
    lista = ['laptop', 'carro', 'cartera','tortuga','llave','lente','zapato']
    lista2 =[]
    lista3 = []
    while len(lista2) < n:
        b = random.randint (0,(len(lista))-1) #Como hacer que escoja al azar los elementos de una lista
        if lista[b] not in lista2:
            lista2.append(lista [b])
    if n < 4:
        for i in range (0,n):
            if i == 0:
                horizontal(lista2 [0])
                lista2.remove(lista2[0])
                #CrearMatriz()
            elif i == 1:
                vertical (lista2 [0])
                lista2.remove(lista2[0])
                #CrearMatriz()
            elif i == 2:
                HorizontalInversa(lista2 [0])
                lista2.remove(lista2[0])
                #CrearMatriz()    
    else:
         for i in range (0,4):
            if i == 0:
                horizontal(lista2 [0])
                lista2.remove(lista2[0])
                #CrearMatriz()
            elif i == 1:
                vertical (lista2 [0])
                lista2.remove(lista2[0])
                #CrearMatriz()
            elif i == 2:
                HorizontalInversa(lista2 [0])
                lista2.remove(lista2[0])
                #CrearMatriz()
            elif i == 3:
                VerticalInversa (lista2 [0])
                lista2.remove(lista2[0])
                #CrearMatriz()
    for i in lista2:
        a = random.randint(0,3)
        if a == 0:
            horizontal(i)
            CrearMatriz()
        elif a == 1:
            vertical (i)
            CrearMatriz()
        elif a == 2:
            HorizontalInversa (i)
            CrearMatriz()
        elif a == 3:
            VerticalInversa (i)
            CrearMatriz()
            
    def puntos():
        point=0
        for i in range(0,4):
            HVOI=input("\n¿En que direccion esta tu palabra (Horizontal , vertical, horizontal inversa o vertical inversa)?: ")
            if HVOI == 'horizontal':
                Posx=int(input('Dame la primera posicion x de tu palabra: '))
                Posy=int(input('Dame la primera posicion y de tu palabra: '))
                Posx2=int(input('\nDame la ultima posicion x de tu palabra: '))
                Posy2=int(input('Dame la ultima posicion y de tu palabra: '))
                PI = matriz2[Posy][Posx]
                PF = matriz2[Posy2][Posx2]
                cont=Posx
                palabra=[]
                for i in range(0,Posx2-Posx+1):
                    palabra.extend(matriz2[Posy][cont])
                    cont+=1
                palabraEnLista=''.join([str(elem) for elem in palabra]) 
                if palabraEnLista in lista:
                     point+=1
                print('')
                CrearMatrizCompleta(matriz2)
                print('La palabra es: ', palabraEnLista)
                print('PUNTOS: ', point)
                guardar = input("***¿Quieres guardar el juego? ('Si' o 'No')***: ")
                if guardar == 'Si':
                    pickle.dump(matriz2, open('JuegoGuardado.dat', 'wb'))
                    return
                else:
                    pass

            elif HVOI == 'vertical':
                VPosx=int(input('\nDame la primera posicion x de tu palabra: '))
                VPosy=int(input('Dame la primera posicion y de tu palabra: '))
                VPosx2=int(input('\nDame la ultima posicion x de tu palabra: '))
                VPosy2=int(input('Dame la ultima posicion y de tu palabra: '))
                VPI = matriz2[VPosy][VPosx]
                VPF = matriz2[VPosy2][VPosx2]
                Vcont=VPosy
                Vpalabra=[]
                for j in range(0,VPosy2-VPosy+1):
                    Vpalabra.extend(matriz2[Vcont][VPosx])
                    Vcont+=1
                VpalabraEnLista=''.join([str(elem2) for elem2 in Vpalabra]) 
                if VpalabraEnLista in lista:
                     point+=1
                print('')
                CrearMatrizCompleta(matriz2)
                print('La palabra es: ', VpalabraEnLista)
                print('PUNTOS: ', point)
                guardar2 = input("***¿Quieres guardar el juego? ('Si' o 'No')***: ")
                if guardar2 == 'Si':
                    pickle.dump(matriz2, open('JuegoGuardado.dat', 'wb'))
                    return
                else:
                    pass

            elif HVOI == 'horizontal i':
                HIPosx=int(input('\nDame la primera posicion x de tu palabra: '))
                HIPosy=int(input('Dame la primera posicion y de tu palabra: '))
                HIPosx2=int(input('\nDame la ultima posicion x de tu palabra: '))
                HIPosy2=int(input('Dame la ultima posicion y de tu palabra: '))
                HIPI = matriz2[HIPosy][HIPosx]
                HIPF = matriz2[HIPosy2][HIPosx2]
                HIcont=HIPosx
                HIpalabra=[]
                for k in range(0,HIPosx2-HIPosx+1):
                    HIpalabra.extend(matriz2[HIPosy][HIcont])
                    HIcont-=1
                HIpalabraEnLista=''.join([str(elem3) for elem3 in HIpalabra]) 
                if HIpalabraEnLista in lista:
                     point+=1
                print('')
                CrearMatrizCompleta(matriz2)
                print('La palabra es: ', HIpalabraEnLista)
                print('PUNTOS: ', point)
                guardar3 = input("***¿Quieres guardar el juego? ('Si' o 'No')***: ")
                if guardar3 == 'Si':
                    pickle.dump(matriz2, open('JuegoGuardado.dat', 'wb'))
                    return
                else:
                    pass
                
            elif HVOI == 'vertical i':
                VIPosx=int(input('\nDame la primera posicion x de tu palabra: '))
                VIPosy=int(input('Dame la primera posicion y de tu palabra: '))
                VIPosx2=int(input('\nDame la ultima posicion x de tu palabra: '))
                VIPosy2=int(input('Dame la ultima posicion y de tu palabra: '))
                VIPI = matriz2[VIPosy][VIPosx]
                VIPF = matriz2[VIPosy2][VIPosx2]
                VIcont=VIPosy
                VIpalabra=[]
                VIpalabra2=str()
                for l in range(0,VIPosy2-VIPosy+1):
                    VIpalabra.extend(matriz2[VIcont][VIposx])
                    VIcont-=1
                VIpalabraEnLista=''.join([str(elem4) for elem4 in VIpalabra]) 
                if VIpalabraEnLista in lista:
                     point+=1
                print('')
                CrearMatrizCompleta(matriz2)
                print('La palabra es: ', VIpalabraEnLista)
                print('PUNTOS: ', point)
            print('')
        if point == 4:
            print('PUNTOS TOTALES: ', point)
            print('$$$ GANASTE $$$')
        else:
            print('Intentelo de nuevo.')
        
    def TableroCompleto(matriz):
        for i in matriz:
            lista =[]
            for dato in i:
                if dato == '-':
                    dato = random.choice(string.ascii_lowercase)
                    lista.append(dato)
                else:
                    lista.append(dato)  
            matriz2.append(lista)      
        CrearMatrizCompleta(matriz2)
    TableroCompleto(matriz)
    puntos()
    
def nivel3():
    matriz=[]
    matriz2=[]
    Horizontal=15
    Vertical=15
    n = 6
    print('')
    for i in range (Vertical):
        lista = []
        for j in range (Horizontal):
            lista.append ('-')
        matriz.append (lista)
    def CrearMatriz():
        for r in matriz:
            for d in r:
                print(d, end='   ')
            print()
    def CrearMatrizCompleta(matriz2):
        for r in matriz2:
            for d in r:
                print(d, end='   ')
            print()
    def horizontal (x):
        ubi = True
        if len(x) <= len(matriz):
            while ubi == True:
                inicioColumna = random.randint(0,Horizontal-len(x))                
                inicioFila = random.randint(0,Vertical-1) 
                a = matriz[inicioFila][inicioColumna]
                cont=0
                si = 0
                a=inicioColumna
                contador=inicioColumna
                for letra in x:
                    if matriz[inicioFila][contador]=='-':
                        si+= 1
                        contador+=1
                if si == len(x):
                    lista5=[inicioFila,inicioColumna]
                    ubi = False
            for letra in x:
                matriz[inicioFila][a+cont] = letra   
                cont+=1 
    def vertical (x):
        ubi = True
        if len(x) <= len(matriz):
            while ubi == True:
                inicioColumna = random.randint(0,Horizontal-1)           
                inicioFila = random.randint(0,Vertical-len(x)) 
                a = matriz[inicioFila][inicioColumna]
                cont=0
                si = 0
                a=inicioFila
                contador=inicioFila
                for letra in x:
                    if matriz[contador][inicioColumna]=='-':
                        si+= 1
                        contador+=1
                if si == len(x):
                    lista5=[inicioFila,inicioColumna]
                    ubi = False
            for letra in x:
                matriz[a+cont][inicioColumna] = letra   
                cont+=1  
    def VerticalInversa(x):
        a = x[::-1]
        vertical (a)
    def HorizontalInversa(x):
        a = x[::-1]
        horizontal (a)   
    lista = ['computadora', 'telefono', 'calculadora','proyecto','elefante','estuchera','carpeta']
    lista2 =[]
    lista3 = []
    while len(lista2) < n:
        b = random.randint (0,(len(lista))-1) #Como hacer que escoja al azar los elementos de una lista
        if lista[b] not in lista2:
            lista2.append(lista [b])
    if n < 6:
        for i in range (0,n):
            if i == 0:
                horizontal(lista2 [0])
                lista2.remove(lista2[0])
                #CrearMatriz()
            elif i == 1:
                vertical (lista2 [0])
                lista2.remove(lista2[0])
                #CrearMatriz()
            elif i == 2:
                HorizontalInversa(lista2 [0])
                lista2.remove(lista2[0])
                #CrearMatriz()
            elif i == 3:
                HorizontalInversa(lista2 [0])
                lista2.remove(lista2[0])
                #CrearMatriz()
            elif i == 4:
                HorizontalInversa(lista2 [0])
                lista2.remove(lista2[0])
                #CrearMatriz()    
    else:
         for i in range (0,6):
            if i == 0:
                horizontal(lista2 [0])
                lista2.remove(lista2[0])
                #CrearMatriz()
            elif i == 1:
                vertical (lista2 [0])
                lista2.remove(lista2[0])
                #CrearMatriz()
            elif i == 2:
                HorizontalInversa(lista2 [0])
                lista2.remove(lista2[0])
                #CrearMatriz()
            elif i == 3:
                VerticalInversa (lista2 [0])
                lista2.remove(lista2[0])
                #CrearMatriz()
            elif i == 4:
                VerticalInversa (lista2 [0])
                lista2.remove(lista2[0])
                #CrearMatriz()
            elif i == 5:
                VerticalInversa (lista2 [0])
                lista2.remove(lista2[0])
                #CrearMatriz()
    for i in lista2:
        a = random.randint(0,5)
        if a == 0:
            horizontal(i)
            CrearMatriz()
        elif a == 1:
            vertical (i)
            CrearMatriz()
        elif a == 2:
            HorizontalInversa (i)
            CrearMatriz()
        elif a == 3:
            VerticalInversa (i)
            CrearMatriz()
        elif a == 4:
            VerticalInversa (i)
            CrearMatriz()
        elif a == 5:
            VerticalInversa (i)
            CrearMatriz()
            
    def puntos():
        point=0
        for i in range(0,6):
            HVOI=input("\n¿En que direccion esta tu palabra (Horizontal , vertical, horizontal inversa o vertical inversa)?: ")
            if HVOI == 'horizontal':
                Posx=int(input('Dame la primera posicion x de tu palabra: '))
                Posy=int(input('Dame la primera posicion y de tu palabra: '))
                Posx2=int(input('\nDame la ultima posicion x de tu palabra: '))
                Posy2=int(input('Dame la ultima posicion y de tu palabra: '))
                PI = matriz2[Posy][Posx]
                PF = matriz2[Posy2][Posx2]
                cont=Posx
                palabra=[]
                for i in range(0,Posx2-Posx+1):
                    palabra.extend(matriz2[Posy][cont])
                    cont+=1
                palabraEnLista=''.join([str(elem) for elem in palabra]) 
                if palabraEnLista in lista:
                     point+=1
                print('')
                CrearMatrizCompleta(matriz2)
                print('La palabra es: ', palabraEnLista)
                print('PUNTOS: ', point)
                guardar = input("***¿Quieres guardar el juego? ('Si' o 'No')***: ")
                if guardar == 'Si':
                    pickle.dump(matriz2, open('JuegoGuardado.dat', 'wb'))
                    return
                else:
                    pass

            elif HVOI == 'vertical':
                VPosx=int(input('\nDame la primera posicion x de tu palabra: '))
                VPosy=int(input('Dame la primera posicion y de tu palabra: '))
                VPosx2=int(input('\nDame la ultima posicion x de tu palabra: '))
                VPosy2=int(input('Dame la ultima posicion y de tu palabra: '))
                VPI = matriz2[VPosy][VPosx]
                VPF = matriz2[VPosy2][VPosx2]
                Vcont=VPosy
                Vpalabra=[]
                for j in range(0,VPosy2-VPosy+1):
                    Vpalabra.extend(matriz2[Vcont][VPosx])
                    Vcont+=1
                VpalabraEnLista=''.join([str(elem2) for elem2 in Vpalabra]) 
                if VpalabraEnLista in lista:
                     point+=1
                print('')
                CrearMatrizCompleta(matriz2)
                print('La palabra es: ', VpalabraEnLista)
                print('PUNTOS: ', point)
                guardar2 = input("***¿Quieres guardar el juego? ('Si' o 'No')***: ")
                if guardar2 == 'Si':
                    pickle.dump(matriz2, open('JuegoGuardado.dat', 'wb'))
                    return
                else:
                    pass

            elif HVOI == 'horizontal i':
                HIPosx=int(input('\nDame la primera posicion x de tu palabra: '))
                HIPosy=int(input('Dame la primera posicion y de tu palabra: '))
                HIPosx2=int(input('\nDame la ultima posicion x de tu palabra: '))
                HIPosy2=int(input('Dame la ultima posicion y de tu palabra: '))
                HIPI = matriz2[HIPosy][HIPosx]
                HIPF = matriz2[HIPosy2][HIPosx2]
                HIcont=HIPosx
                HIpalabra=[]
                for k in range(0,HIPosx2-HIPosx+1):
                    HIpalabra.extend(matriz2[HIPosy][HIcont])
                    HIcont-=1
                HIpalabraEnLista=''.join([str(elem3) for elem3 in HIpalabra]) 
                if HIpalabraEnLista in lista:
                     point+=1
                print('')
                CrearMatrizCompleta(matriz2)
                print('La palabra es: ', HIpalabraEnLista)
                print('PUNTOS: ', point)
                guardar3 = input("***¿Quieres guardar el juego? ('Si' o 'No')***: ")
                if guardar3 == 'Si':
                    pickle.dump(matriz2, open('JuegoGuardado.dat', 'wb'))
                    return
                else:
                    pass
                
            elif HVOI == 'vertical i':
                VIPosx=int(input('\nDame la primera posicion x de tu palabra: '))
                VIPosy=int(input('Dame la primera posicion y de tu palabra: '))
                VIPosx2=int(input('\nDame la ultima posicion x de tu palabra: '))
                VIPosy2=int(input('Dame la ultima posicion y de tu palabra: '))
                VIPI = matriz2[VIPosy][VIPosx]
                VIPF = matriz2[VIPosy2][VIPosx2]
                VIcont=VIPosy
                VIpalabra=[]
                VIpalabra2=str()
                for l in range(0,VIPosy2-VIPosy+1):
                    VIpalabra.extend(matriz2[VIcont][VIposx])
                    VIcont-=1
                VIpalabraEnLista=''.join([str(elem4) for elem4 in VIpalabra]) 
                if VIpalabraEnLista in lista:
                     point+=1
                print('')
                CrearMatrizCompleta(matriz2)
                print('La palabra es: ', VIpalabraEnLista)
                print('PUNTOS: ', point)
            print('')
        if point == 6:
            print('PUNTOS TOTALES: ', point)
            print('$$$ GANASTE 5 peso $$$')
        else:
            print('Intentelo de nuevo.')
        
    def TableroCompleto(matriz):
        for i in matriz:
            lista =[]
            for dato in i:
                if dato == '-':
                    dato = random.choice(string.ascii_lowercase)
                    lista.append(dato)
                else:
                    lista.append(dato)  
            matriz2.append(lista)      
        CrearMatrizCompleta(matriz2)
    TableroCompleto(matriz)
    puntos()

def Jugar():
    print('')
    print("Dificultad 'facil': Matriz de 5x5 y palabras cortas. \nDificultad 'intermedio': Matriz de 10x10 y palabras medianas. \nDificultad 'dificil': Matriz de 15x15 y palabras largas.")
    choice2=input('\nEscoge la dificultad: ')
    if choice2 == 'facil':  
        nivel1()
    elif choice2 == 'intermedio':
        nivel2()
    elif choice2 == 'dificil':
        nivel3()
    else:
        print('\nERROR')

def cargarMatrizGuardada(x):
    for r in x:
        for d in r:
            print(d, end='   ')
        print()
        
def seguirJugando(a):
        lista = ['sol', 'pez', 'mago','cafe','pato','casa','bota', 'laptop', 'carro', 'cartera','tortuga','llave','lente','zapato','computadora', 'telefono', 'calculadora','proyecto','elefante','estuchera','carpeta']
        point=0
        if len(a)==5:
            w=3
        elif len(a)==10:
            w=4
        elif len(a)==15:
            w=6
        for i in range(0,w):
            HVOI=input("\n¿En que direccion esta tu palabra (Horizontal , vertical, horizontal inversa o vertical inversa)?: ")
            if HVOI == 'horizontal':
                Posx=int(input('Dame la primera posicion x de tu palabra: '))
                Posy=int(input('Dame la primera posicion y de tu palabra: '))
                Posx2=int(input('\nDame la ultima posicion x de tu palabra: '))
                Posy2=int(input('Dame la ultima posicion y de tu palabra: '))
                PI = a[Posy][Posx]
                PF = a[Posy2][Posx2]
                cont=Posx
                palabra=[]
                for i in range(0,Posx2-Posx+1):
                    palabra.extend(a[Posy][cont])
                    cont+=1
                palabraEnLista=''.join([str(elem) for elem in palabra]) 
                if palabraEnLista in lista:
                     point+=1
                print('')
                cargarMatrizGuardada(a)
                print('La palabra es: ', palabraEnLista)
                print('PUNTOS: ', point)

            elif HVOI == 'vertical':
                VPosx=int(input('\nDame la primera posicion x de tu palabra: '))
                VPosy=int(input('Dame la primera posicion y de tu palabra: '))
                VPosx2=int(input('\nDame la ultima posicion x de tu palabra: '))
                VPosy2=int(input('Dame la ultima posicion y de tu palabra: '))
                VPI = a[VPosy][VPosx]
                VPF = a[VPosy2][VPosx2]
                Vcont=VPosy
                Vpalabra=[]
                for j in range(0,VPosy2-VPosy+1):
                    Vpalabra.extend(a[Vcont][VPosx])
                    Vcont+=1
                VpalabraEnLista=''.join([str(elem2) for elem2 in Vpalabra]) 
                if VpalabraEnLista in lista:
                     point+=1
                print('')
                cargarMatrizGuardada(a)
                print('La palabra es: ', VpalabraEnLista)
                print('PUNTOS: ', point)

            elif HVOI == 'horizontal i':
                HIPosx=int(input('\nDame la primera posicion x de tu palabra: '))
                HIPosy=int(input('Dame la primera posicion y de tu palabra: '))
                HIPosx2=int(input('\nDame la ultima posicion x de tu palabra: '))
                HIPosy2=int(input('Dame la ultima posicion y de tu palabra: '))
                HIPI = a[HIPosy][HIPosx]
                HIPF = a[HIPosy2][HIPosx2]
                HIcont=HIPosx
                HIpalabra=[]
                for k in range(0,HIPosx2-HIPosx+1):
                    HIpalabra.extend(a[HIPosy][HIcont])
                    HIcont-=1
                HIpalabraEnLista=''.join([str(elem3) for elem3 in HIpalabra]) 
                if HIpalabraEnLista in lista:
                     point+=1
                print('')
                cargarMatrizGuardada(a)
                print('La palabra es: ', HIpalabraEnLista)
                print('PUNTOS: ', point)
                
            elif HVOI == 'vertical i':
                VIPosx=int(input('\nDame la primera posicion x de tu palabra: '))
                VIPosy=int(input('Dame la primera posicion y de tu palabra: '))
                VIPosx2=int(input('\nDame la ultima posicion x de tu palabra: '))
                VIPosy2=int(input('Dame la ultima posicion y de tu palabra: '))
                VIPI = a[VIPosy][VIPosx]
                VIPF = a[VIPosy2][VIPosx2]
                VIcont=VIPosy
                VIpalabra=[]
                VIpalabra2=str()
                for l in range(0,VIPosy2-VIPosy+1):
                    VIpalabra.extend(a[VIcont][VIposx])
                    VIcont-=1
                VIpalabraEnLista=''.join([str(elem4) for elem4 in VIpalabra]) 
                if VIpalabraEnLista in lista:
                     point+=1
                print('')
                cargarMatrizGuardada(a)
                print('La palabra es: ', VIpalabraEnLista)
                print('PUNTOS: ', point)
            print('')
        if point == w:
            print('PUNTOS TOTALES: ', point)
            print('$$$ GANASTE $$$')
        else:
            print('Intentelo de nuevo.')
       
def menu():
    print('Bienvenido al juego, \n 1. Jugar \n 2. Guardar Juego \n 3. Cargar Juego \n 4. Informacion \n 5. Salir')
    choice=input('\nEscoge un numero: ')
    
    if choice == '1':  
        print('\n***Creando tablero***')
        Jugar()  
    elif choice == '2':
        print('\n***Dentro del juego al terminar cada palabra puedes guardar la matriz actual y salir del juego***')
        Jugar() 
    elif choice == '3':
        print('\n***CARGANDO JUEGO GUARDADO***')
        cargar = pickle.load(open('JuegoGuardado.dat', 'rb'))
        print(cargarMatrizGuardada(cargar))
        seguirJugando(cargar)
        
    elif choice == '4':
        print('\n***TECNOLOGICO DE MONTERREY***\nCreadores del Juego: \n * Marco Antonio Bosquez Gonzalez - A01653247 \n * Ana Laura Flores Agredano - A01657928 \nCopyright: EstoMereceUnCien Entertainment')
    elif choice == '5':
        print('\nSaliendo del juego...')
        sys.exit

menu()