# 2. Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos necesarios para resolver las siguientes tareas:
# a) cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan; DONE!
# b) hallar el árbol de expansión minino y determinar si contiene a Yoda; DONE!
# c) determinar cuál es el número máximo de episodio que comparten dos personajes y quienes son;
# d) cargue al menos los siguientes personajes: Luke SkyWalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8. DONE! 

from grafo import Grafo
from random import randint

grafo = Grafo(dirigido=False)

grafo.insert_vertice('Luke Skywalker')
grafo.insert_vertice('Darth Vader')
grafo.insert_vertice('Yoda')
grafo.insert_vertice('Boba Fett')
grafo.insert_vertice('C3PO')
grafo.insert_vertice('Leia')
grafo.insert_vertice('Rey')
grafo.insert_vertice('Kylo Ren')
grafo.insert_vertice('Chewbacca')
grafo.insert_vertice('Han Solo')
grafo.insert_vertice('R2D2')
grafo.insert_vertice('BB8')

grafo.insert_arist('Luke Skywalker','Darh Vader',randint(1,910))
grafo.insert_arist('Darth Vader','Yoda',randint(1,120))
grafo.insert_arist('Boba Fett','C3PO',randint(1,110))
grafo.insert_arist('Leia','Rey',randint(1,10))
grafo.insert_arist('Kylo Ren','Chewbacca',randint(1,99))
grafo.insert_arist('Han Solo','R2D2',randint(1,10))
grafo.insert_arist('BB8','Darth Vader',randint(1,10))
grafo.insert_arist('BB8','R2D2',randint(1,140))
grafo.insert_arist('Han Solo','Chewbacca',randint(1,1110))
grafo.insert_arist('Leia','Luke Skywalker',randint(1,210))
grafo.insert_arist('Kylo Ren','Rey',randint(1,130))
grafo.insert_arist('Han Solo','BB8',randint(1,150))
grafo.insert_arist('BB8','Chewbacca',randint(1,610))
grafo.insert_arist('C3PO','Chewbacca',randint(1,180))



def arbol_expansion_minimo(): # Parte B.1 Arbol expansion mínimo
    bosque= grafo.kruskal()
    for arbol in bosque:
        print('arbol:')
        for nodo in arbol.split(';'):
            partes = nodo.split('-')
            print(partes)

def el_amigo_yoda(): # Parte B.2: Busqueda de Yoda
    bosque= grafo.kruskal()
    cont=0
    for arbol in bosque:
        for nodo in arbol.split(';'):
            partes = nodo.split('-')
            if ('Yoda') in partes:
                cont+=1
    if cont>=1:
        print('Encontramos a Yoda!')

#arbol_expansion_minimo()
#el_amigo_yoda()


grafo.barrido()
print(f'El número máximo de episodios es de y lo comparten: {grafo.barrido_3()}')




