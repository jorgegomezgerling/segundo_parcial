# 1. Se tiene datos de los Pokémons de las 8 generaciones cargados de manera desordenada de los cuales se conoce su nombre, número, tipo/tipos para el cual debemos construir tres árboles para acceder de manera eficiente a los datos, contemplando lo siguiente:
# a) los índices de cada uno de los árboles deben ser nombre, número y tipo; DONE! 
# b) mostrar todos los datos de un Pokémon a partir de su número [DONE!] y nombre –para este último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres–; DONE! 
# c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico; DONE!
# d) realizar un listado en orden ascendente por número [DONE!] y nombre de Pokémon[DONE!], y además un listado por nivel por nombre; DONE!
# e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;
# f) Determina cuantos Pokémons hay de tipo eléctrico y acero.

from arbol_binario import BinaryTree

nombre_pokemones = BinaryTree()
tipo_pokemones = BinaryTree()
numero_pokemones = BinaryTree()

datos_pokemones = [
    {'nombre': 'Jolteon', 'numero': 1892, 'tipo': 'electrico'},
    {'nombre': 'Bulbasaur', 'numero': 4, 'tipo': 'planta'},
    {'nombre': 'Ivysaur', 'numero': 33, 'tipo': 'planta'},
    {'nombre': 'Venusaur', 'numero': 22, 'tipo': 'planta'},
    {'nombre': 'Charmander', 'numero': 11, 'tipo': 'fuego'},
    {'nombre': 'Charmeleon', 'numero':10, 'tipo': 'fuego'},
    {'nombre': 'Charizard', 'numero': 9, 'tipo': 'fuego'},
    {'nombre': 'Squirtle', 'numero': 67, 'tipo': 'agua'},
    {'nombre': 'Wartortle', 'numero': 48, 'tipo': 'agua'},
    {'nombre': 'Blastoise', 'numero': 93, 'tipo': 'agua'},
    {'nombre': 'Pikachu', 'numero': 520, 'tipo': 'electrico'},
    {'nombre': 'Raichu', 'numero': 256, 'tipo': 'electrico'},
    {'nombre': 'Eevee', 'numero': 1111, 'tipo': 'normal'},
    {'nombre': 'Steelix', 'numero': 1, 'tipo': 'acero'},
    {'nombre': 'Lucario', 'numero': 99, 'tipo': 'acero'},
    {'nombre': 'Lycanroc', 'numero': 117, 'tipo': 'roca'},
    {'nombre': 'Tyrantrum', 'numero': 999, 'tipo': 'roca'}
]

for pokemon in datos_pokemones: # parte A. 
    nombre_pokemones.insert_node(pokemon['nombre'], [pokemon['numero'], pokemon['tipo']])
    tipo_pokemones.insert_node(pokemon['tipo'], [pokemon['nombre'], pokemon['numero']])
    numero_pokemones.insert_node(pokemon['numero'], [pokemon['nombre'], pokemon['tipo']])

def punto_b():
    buscado = numero_pokemones.search(4)
    if buscado is not None:
        print('Busqueda por numero: ')
        print(buscado.value, buscado.other_values)
        print()
        print('Ahora búsqueda por coincidencia: ')
    
    nombre_pokemones.search_by_coincidence_cambiada('B')    

def punto_c():
    nombre_pokemones.inorden_probando('agua') # Recibe cualquier tipo.

def punto_d():
    print('Orden ascendente por numero:')
    numero_pokemones.inorden_datos() # Orden ascendente por numero
    print('----------')
    print('Orden ascentente por nombre:')
    nombre_pokemones.inorden_datos() # Orden ascentente por nombre
    print('----------')
    print('ByLevel por nombre:')
    nombre_pokemones.by_level() # ByLevel por nombre

def punto_e(nombre):
    buscado = nombre_pokemones.search(nombre) # Es general, sirve para todos los pokemones. Inclusive los requeridos: Jolteon, Lycanroc y Tyrantrum;
    if buscado is not None:
        print('Busqueda por nombre: ')
        print(buscado.value, buscado.other_values)
    
def punto_f():
    print('cantidad de pokemones tipo acero: ', nombre_pokemones.contar_tipos('acero'))
    print('cantidad de pokemones tipo electrico: ', nombre_pokemones.contar_tipos('electrico'))


#punto_b()
#punto_c()
#punto_d()
#punto_e('Tyrantrum')
#punto_f()