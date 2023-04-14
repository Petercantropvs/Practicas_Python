'''
10. Dada una lista de nombres de estudiantes y dos listas con sus notas en un curso, 
escriba un programa que manipule dichas estructuras de datos para poder resolver los siguientes puntos:
   
A. Generar una estructura con todas las notas relacionando el nombre del estudiante 
   con las notas. Utilizar esta estructura para la resolución de los siguientes items.
B. Calcular el promedio de notas de cada estudiante.
C. Calcular el promedio general del curso.
D. Identificar al estudiante con la nota promedio más alta.
E. Identificar al estudiante con la nota más baja.

Nota:
- Las 3 estructuras están ordenadas de forma que los elementos en la misma posición corresponden a un mismo alumno.
- Realizar funciones con cada item'''

def prom(nums):
    '''Esta función calcula el promedio de una lista o tupla independientemente de la cantidad de elementos de la misma.'''
    if len(nums):
        p = sum(i for i in nums)/len(nums)
    else: p = 0
    return p

nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín'  , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 
'Nicolás',  'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''
notas_1 = [81,  60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69, 
           12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44, 
           85, 73, 37, 42, 95, 18, 7,     74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
           64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
           95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

calificaciones = {}
promedio = {}
nota_min = {}
nombres = nombres.split(',')
nombres1 = []

for nombre, nota1, nota2 in zip(nombres, notas_1, notas_2):
    nombre = nombre.strip(' \'\n').title()
    nombres1.append(nombre)

    calificaciones[nombre] = (nota1, nota2)
    promedio[nombre] = prom(calificaciones[nombre])  
    nota_min[nombre] = min(nota1,nota2)
    
prom_gral = prom(promedio.values())
nota_min = min(nota_min.items(), key = lambda nota: nota[1])

print('{:<12}{:^12}{:>12}\n{}'.format('Nombre','Calificaciones','Promedio','-'*40))

for nombre, nota1, nota2, prom in zip(nombres1, notas_1, notas_2, promedio.values()):
    print(f'{nombre:<15}{nota1:<4}{nota2:>4}{prom:>15}')
print('-'*40)
print(f'''\nPromedio más alto: {max(promedio.items(), key = lambda nota: nota[1])}
\nNota más baja: {nota_min}
\nPromedio general: {prom_gral:.4f}''')