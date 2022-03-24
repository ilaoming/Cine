#Librerias
from statistics import mode

# Declaracion de variables
nombrePeliculas = ['Lagrimas del Sol','IT','Spiderman','Laberinto del Fauno','Tom and Jerry','Guerra de los Mundos','2012']
nombreSalas = ['Sala A','Sala B','Sala C','Sala D','Sala E','Sala F']
opcionesPeli = ['1','2','3','4','5','6','7']
opcionesSala = ['1','2','3','4','5','6']
opcionesNueva = ['1','2']
contadorPeli = [0,0,0,0,0,0,0]
contadorSala = [0,0,0,0,0,0]
combinacion = []
opcionNueva = ""
opcion = ""
opcionSala = ""
pelicula = []
sala = []
mayorAsistencia = ""
menorAsistencia = ""
i = 0

#cambio despues de el enlace con SourceTree

#Funciones

# Retorna true si encuentra una opcion valida
def validOpcionPeli(opcion):
    return opcion in opcionesPeli

# Retorna true si encuentra una opcion valida
def validOpcionSala(opcion):
    return opcion in opcionesSala

# Retorna true si encuentra una opcion valida
def validOpcionNueva(opcion):
    return opcion in opcionesNueva    

# Imprime la lista con los nombres de las peliculas 
def menuPeliText():
    for x in range(len(nombrePeliculas)):
        print(x+1,".",nombrePeliculas[x])
   

# Imprime la lista con los nombres de las salas 
def menuSalaText():
    for x in range(len(nombreSalas)):
        print(x+1,".",nombreSalas[x])

# Imprime el mensaje del ultimo menu.
def menuNuevaText():
    print("Desea elejir una nueva pelicula. 1.SI  2.NO")    


# Valida que opcion seleccionaron y en base a la opcion realiza un incremento "+=1" en la lista "contadorSala = []" y agrega un elemento a la lista "sala = []"
def logicaMenuSala(opcionSala):
    while not validOpcionSala(opcionSala):
        print("Opcion invalida")
        opcionSala = input("Elije tu Sala: ")
    else:
        if (opcionSala == opcionesSala[0]):
            contadorSala[0] +=1
            sala.append("Sala A")

        elif (opcionSala == opcionesSala[1]):
            contadorSala[1] +=1
            sala.append("Sala B")

        elif (opcionSala == opcionesSala[2]):
            contadorSala[2] +=1
            sala.append("Sala C")

        elif (opcionSala == opcionesPeli[3]):
            contadorSala[3] +=1
            sala.append("Sala D")

        elif (opcionSala == opcionesSala[4]):
            contadorSala[4] +=1
            sala.append("Sala E")

        elif (opcionSala == opcionesSala[5]):
            contadorSala[5] +=1
            sala.append("Sala F")



# Recive un contador global "i" como parametro
# Valida que opcion seleccionaron y en base a la opcion realiza un incremento "+=1" en la lista "contadorPeli = []" y agrega un elemento a la lista "pelicula = []"
# Llama la funcion "menuSalaText()" --> Ya se indico previamente su uso
# Llama la funcion "logicaMenuSala()" --> Ya se indico previamente su uso
# Agrega un elemento a la lista "combinacion = []"
def main(i):
    menuPeliText()
    opcion = input("Elije tu Pelicula: ")
    while not validOpcionPeli(opcion):
        print("Opcion invalida")
        opcion = input("Elije tu Pelicula: ")
    else:
        if (opcion == opcionesPeli[0]):
            contadorPeli[0] +=1
            pelicula.append("Lagrimas del Sol")
            menuSalaText()
            opcionSala = input("Elije tu Sala: ")
            logicaMenuSala(opcionSala)
            combinacion.append(pelicula[i] +"-"+ sala[i])

        elif (opcion == opcionesPeli[1]):
            contadorPeli[1] +=1
            pelicula.append("IT")
            menuSalaText()
            opcionSala = input("Elije tu Sala: ")
            logicaMenuSala(opcionSala)
            combinacion.append(pelicula[i] +"-"+ sala[i])

        elif (opcion == opcionesPeli[2]):
            contadorPeli[2] +=1
            pelicula.append("Spiderma")
            menuSalaText()
            opcionSala = input("Elije tu Sala: ")
            logicaMenuSala(opcionSala)
            combinacion.append(pelicula[i] +"-"+ sala[i])

        elif (opcion == opcionesPeli[3]):
            contadorPeli[3] +=1
            pelicula.append("Laberinto del Fauno")
            menuSalaText()
            opcionSala = input("Elije tu Sala: ")
            logicaMenuSala(opcionSala)
            combinacion.append(pelicula[i] +"-"+ sala[i])

        elif (opcion == opcionesPeli[4]):
            contadorPeli[4] +=1
            pelicula.append("Tom and Jerry")
            menuSalaText()
            opcionSala = input("Elije tu Sala: ")
            logicaMenuSala(opcionSala)
            combinacion.append(pelicula[i] +"-"+ sala[i])

        elif (opcion == opcionesPeli[5]):
            contadorPeli[5] +=1
            pelicula.append("Guerra de los Mundos")
            menuSalaText()
            opcionSala = input("Elije tu Sala: ")
            logicaMenuSala(opcionSala)
            combinacion.append(pelicula[i] +"-"+ sala[i])

        elif (opcion == opcionesPeli[6]):
            contadorPeli[6] +=1
            pelicula.append("2012")
            menuSalaText()
            opcionSala = input("Elije tu Sala: ")
            logicaMenuSala(opcionSala)
            combinacion.append(pelicula[i] +"-"+ sala[i])

        else:
            print("Error")
  
    # Imprime el valor actual de las listas , para ir observando los cambios
    print(contadorPeli)
    print(contadorSala)
    print(pelicula)
    print(sala)
    print(combinacion)

    # Llama la funcion "menuNuevaText()" --> Ya se indico previamente su uso
    menuNuevaText()
    # Devuelve True si la opcion selecciona es "encontrada"
    opcionNueva = input("Elija una Opcion: ")
    while not validOpcionNueva(opcionNueva):
        print("Opcion invalida")
        opcionNueva = input("Elija una Opcion: ")
    else:
        if (opcionNueva == opcionesNueva[0]):
            i+=1
            main(i)
        else:
            # Buscamos la sala con menor asistencia
            salaMenor = min(contadorSala, key=int)

            # Buscamos la sala con mayor asistecia y la pelicula mas vista
            salaMayor = max(contadorSala, key=int)
            mayorAsistencia = max(contadorPeli, key=int)

            # Obtenemos el indice ("la posicion") de la pelicula mas vista, la sala mas asistida y la sala menos asistida
            indexPeli = contadorPeli.index(mayorAsistencia)
            indexSalaMayor = contadorSala.index(salaMayor)
            indexSalaMenor = contadorSala.index(salaMenor)

            # Obtenemos la combinacion mas repetida
            print("Combinacion mas vista",mode(combinacion))

            # Ya que sabemos en que posicion esta la pelicula mas vista, la sala mas asistida y la menos asistida. Lo imprimimos.
            print("Pelicula mas vista:",nombrePeliculas[indexPeli],"vista:",mayorAsistencia,"veces")
            print("Sala mas asistida:",nombreSalas[indexSalaMayor],"asistida:",salaMayor,"veces")
            print("Sala menos asistida:",nombreSalas[indexSalaMenor],"asistida:",salaMenor,"veces")
            print("Adios ☺")   

#Llama la funcion principal "main()"    
main(i)












