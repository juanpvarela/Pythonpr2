nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 'David',
'Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 'Francsica', 
'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 'Joaquina', 'Jorge',
'JOSE', 'Javier', 'Joaquín'  , 'Julian', 'Julieta', 'Luciana','LAUTARO', 'Leonel', 'Luisa', 
'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 'Nicolás',  'Nancy', 'Noelia', 'Pablo', 
'Priscila', 'Sabrina', 'Tomás', 'Ulises', 'Yanina' '''
notas_1 = [81,  60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69, 12, 77, 
           13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44, 85, 73, 37, 42, 95, 18, 7, 
           74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37, 64, 13, 8,
           87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73, 95, 19, 47, 15, 31,
           39, 15, 74, 33, 57, 10]

alumn= nombres.replace("\n","").replace(" " ,"").split(",")
alumnos = {}

for i in range(len(alumn)):
    alumnos[alumn[i]]= [notas_1[i],notas_2[i]]


print("La lista de alumnos con sus notas es:")



#Hago un print para cada uno de los elementos del diccionario así los escribe  verticalmente

for i in range(len(alumn)):
    
    print(alumn[i],":",alumnos[alumn[i]])


    
#Calculo el promedio de cada uno de los estudiantes usando sus dos notas
proms = [(val[0]+val[1])/2 for key, val in alumnos.items()]

#Este espacio es para que haya mas espacio entre las escrituras
print("\n \n \n")      


#Agrego la columna con los promedios
for i in range(len(alumnos)):
    alumnos[alumn[i]].append(proms[i])


print("La lista de los alumnos con sus notas y promedios es:")      

for i in range(len(alumn)):
    
    print(alumn[i],":",alumnos[alumn[i]])

print("\n \n \n") 



promgen = sum([(val[0]+val[1])/2 for key, val in alumnos.items()])/len(alumnos)


print("El promedio general es:")      
print(promgen)



print("\n \n \n")      
maxprom = 0

#Utilizo un sorted para ordenar la lista del mayor promedio al menor, y luego escribo el nombre y el
#promedio máximo.

print("La persona con mayor promedio y su promedio es:")

x = sorted(alumnos.items(), key=lambda prom: prom[1][2], reverse = True)
print(x[0][0],x[0][1][2])


print("\n \n \n")



#Hago una sentencia for que vaya comparando las notas,  se quede con la nota mínima, y a su vez
#guarde el  nombre de la persona con la menor nota.
nota_min = min(alumnos[alumn[0]])
nombre = "Agustin"
for i in range(len(alumnos)):
    if min(alumnos[alumn[i]]) < nota_min:
        nombre = alumn[i]
        nota_min = min(alumnos[alumn[i]])
    else:
        nombre = nombre
        nota_min = nota_min

print("La persona con nota minima y su nota es")      
print(nombre,nota_min)
