from cola import Cola
import linecache

def get_value_from_file(file_name, index):
    line = linecache.getline(file_name, index)
    line_split = line.split(';')
    line_split.pop()
    return line_split

class NodeTree(): # Definicion del nodo para el árbol

    def __init__(self, value, other_values=None): # other_values parece no ser totalmente relevante.
        self.value = value # valor del nodo
        self.other_values = other_values
        self.left = None 
        self.right = None
        self.height = 0


class BinaryTree:

    def __init__(self): # clasico init
        self.root = None 

    def height(self, root): # retorna la altura -1 si no tiene si quiera un nodo. Sino, la altura root.height
        if root is None:
            return -1
        else:
            return root.height

    def update_height(self, root): # actualizar la altura
        if root is not None: # Si el nodo no está vacío       
            left_height = self.height(root.left) # altura nodo izquierdo
            right_height = self.height(root.right) # altura nodo derecho
            root.height = (left_height if left_height > right_height else right_height) + 1 # retorna la altura mayor.

    def simple_rotation(self, root, control): # rotacion
        if control: # variable control
            aux = root.left
            root.left = aux.right
            aux.right = root
        else:
            aux = root.right
            root.right = aux.left
            aux.left = root
        self.update_height(root)
        self.update_height(aux)
        root = aux
        return root

    def double_rotation(self, root, control):
        if control:
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else:
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        return root

    def balancing(self, root):
        if root is not None:
            if self.height(root.left) - self.height(root.right) == 2:
                if self.height(root.left.left) >= self.height(root.left.right):
                    root = self.simple_rotation(root, True)
                else:
                    root = self.double_rotation(root, True)
            elif self.height(root.right) - self.height(root.left) == 2:
                if self.height(root.right.right) >= self.height(root.right.left):
                    root = self.simple_rotation(root, False)
                else:
                    root = self.double_rotation(root, False)
        return root

    def insert_node(self, value, other_values=None):

        def __insertar(root, value, other_values):
            if root is None:
                return NodeTree(value, other_values)
            elif value < root.value:
                root.left = __insertar(root.left, value, other_values)
            else:
                root.right = __insertar(root.right, value, other_values)
            root = self.balancing(root)
            self.update_height(root)
            return root

        self.root = __insertar(self.root, value, other_values)

    def by_level(self):
        if self.root is not None:
            cola_tree = Cola()
            cola_tree.arrive(self.root)
            while cola_tree.size() > 0:
                node = cola_tree.atention()
                print(node.value)
                # a = input()
                if node.left is not None:
                    cola_tree.arrive(node.left)
                if node.right is not None:
                    cola_tree.arrive(node.right)

    def inorden(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(root.value)
                __inorden(root.right)

        __inorden(self.root)

    
    # acá empiezan cosas para ejercicios... 

    def inorden_datos(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(root.value, root.other_values)
                __inorden(root.right)

        __inorden(self.root)

    def inorden_criatura(self, criatura):
        def __inorden(root, criatura):
            if root is not None:
                __inorden(root.left, criatura)
                if root.value is criatura:
                    print(root.value, root.other_values)
                __inorden(root.right, criatura)

        __inorden(self.root, criatura)
    
    def inorden_super_or_villano(self, is_hero):
        def __inorden_s_v(root, is_hero):
            if root is not None:
                __inorden_s_v(root.left, is_hero)
                if root.other_values is is_hero:
                    print(root.value)
                __inorden_s_v(root.right, is_hero)

        __inorden_s_v(self.root, is_hero)
    

    def inorden_cuantos_hay(self, tipo):
        contador = 0
        def __inorden_s_v(root, tipo):
            if root is not None:
                __inorden_s_v(root.left, tipo)
                if tipo in root.other_values:
                    contador += 1
                __inorden_s_v(root.right, tipo)

        __inorden_s_v(self.root, tipo)
        return contador



    def hacer_bosque(self, arbHeroes, arbVillanos):
        def __inorden(root, arbHeroes, arbVillanos):
            if root is not None:
                if root.other_values is True:
                    arbHeroes.insert_node(root.value, root.other_values)
                else:
                    arbVillanos.insert_node(root.value, root.other_values)
                __inorden(root.right, arbHeroes, arbVillanos)
                __inorden(root.left, arbHeroes, arbVillanos)
        
        __inorden(self.root, arbHeroes, arbVillanos)

    def inorden_sov(self, is_hero):
        def __inorden(root, is_hero):
            if root is not None:
                __inorden(root.left, is_hero)
                if root.other_values is is_hero:
                    print(root.value)
                __inorden(root.right, is_hero)

        __inorden(self.root, is_hero)

    def inorden_probando(self, tipo):
        def __inorden(root, tipo):
            if root is not None:
                __inorden(root.left, tipo)
                if tipo in root.other_values:
                    print(root.value)
                __inorden(root.right, tipo)

        __inorden(self.root, tipo)

    def inorden_derrotadas_por(self, vencedor):
        def __inorden(root, vencedor):
            if root is not None:
                __inorden(root.left, vencedor)
                if root.other_values['derrotado'] is vencedor:
                    print(root.value)
                __inorden(root.right, vencedor)

        __inorden(self.root, vencedor)

    def inorden_letra(self, letra):
        def __inorden(root, letra):
            if root is not None:
                __inorden(root.left, letra)
                if root.value[0] == letra:
                    print(root.value)
                __inorden(root.right, letra)

        __inorden(self.root, letra)
    
    def contar(self, value):
        def __contar(root, value):
            count = 0
            if root is not None:
                if root.value == value:
                    count = 1
                count += __contar(root.left, value)
                count += __contar(root.right, value)
            return count

        return __contar(self.root, value)
    
    def contar_heroes(self):
        def __contar_heroes(root):
            count = 0
            if root is not None:
                if root.other_values is True:
                    count = 1
                count += __contar_heroes(root.left)
                count += __contar_heroes(root.right)
            return count

        return __contar_heroes(self.root)
    
    def contar_tipos(self, tipo):
        def __contar_heroes(root, tipo):
            count = 0
            if root is not None:
                if tipo in root.other_values:
                    count = 1
                count += __contar_heroes(root.left, tipo)
                count += __contar_heroes(root.right, tipo)
            return count

        return __contar_heroes(self.root, tipo)
    
    def contar_en_general(self):
        def __contar_en_general(root):
            count = 0
            if root is not None:
                count = 1
                count += __contar_en_general(root.left)
                count += __contar_en_general(root.right)
            return count
        

        return __contar_en_general(self.root)

    def inorden_ranking(self, ranking):
        def __inorden_ranking(root, ranking):
            if root is not None:
                __inorden_ranking(root.left, ranking)
                if root.other_values['derrotado'] is not None:
                    if root.other_values['derrotado'] not in ranking:
                        ranking[root.other_values['derrotado']] = 1
                    else:
                        ranking[root.other_values['derrotado']] += 1
                __inorden_ranking(root.right, ranking)

        __inorden_ranking(self.root, ranking)

    def inorden_add_field(self):
        def __inorden_add_field(root):
            if root is not None:
                __inorden_add_field(root.left)
                root.other_values['capturado'] = None
                __inorden_add_field(root.right)

        __inorden_add_field(self.root)
    
    def inorden_soy_invencible(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                if root.other_values['derrotado'] is None:
                    print(root.value)
                __inorden(root.right)

        __inorden(self.root)
    
    def inorden_derrotado_por_heracles(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                if root.other_values['derrotado'] == 'Heracles':
                    print(root.value)
                __inorden(root.right)

        __inorden(self.root)
    
    def inorden_add_newfield(self, field):
        def __inorden_add_field(root, field):
            if root is not None:
                __inorden_add_field(root.left, field)
                root.other_values[field] = None
                __inorden_add_field(root.right, field)

        __inorden_add_field(self.root, field)

    def inorden_file(self, file_name):
        def __inorden_file(root, file_name):
            if root is not None:
                __inorden_file(root.left, file_name)
                value = get_value_from_file(file_name, root.other_values)
                print(root.value, value[0])
                __inorden_file(root.right, file_name)

        __inorden_file(self.root, file_name)

    def inorden_file_lightsaber(self, file_name, lightsaber_color):
        def __inorden_file_lightsaber(root, file_name, lightsaber_color):
            if root is not None:
                __inorden_file_lightsaber(root.left, file_name, lightsaber_color)
                value = get_value_from_file(file_name, root.other_values)
                if lightsaber_color in value[4].split('/'):
                    print(root.value, value[4].split('/'))
                __inorden_file_lightsaber(root.right, file_name, lightsaber_color)

        __inorden_file_lightsaber(self.root, file_name, lightsaber_color)

    def inorden_maestro(self, file_name):
        def __inorden_file_lightsaber(root, file_name):
            if root is not None:
                __inorden_file_lightsaber(root.left, file_name)
                value = get_value_from_file(file_name, root.other_values)
                if not '-' in value[3].split('/'):
                    print(root.value, value[3].split('/'))
                __inorden_file_lightsaber(root.right, file_name)

        __inorden_file_lightsaber(self.root, file_name)

    def inorden_proveniente(self, file_name):
        def __inorden_p(root, file_name):
            if root is not None:
                __inorden_p(root.left, file_name)
                value = get_value_from_file(file_name, root.other_values)
                if 'togruta' in value[2].split('/') or 'cerean' in value[2].split('/'):
                    print(root.value, value[2].split('/'))
                __inorden_p(root.right, file_name)

        __inorden_p(self.root, file_name)
    
    def inorden_aves_en_peligro(self):
        def __inorden_p(root):
            if root is not None:
                __inorden_p(root.left)
                if 'Aves de Esinfalo' == root.value:
                    root.other_values['Descripcion'] = 'Heracles derrotó a varias'
                __inorden_p(root.right)

        __inorden_p(self.root) 

    def inorden_start_with(self, cadena):
        def __inorden_start_with(root, cadena):
            if root is not None:
                __inorden_start_with(root.left, cadena)
                if root.other_values is True and root.value.upper().startswith(cadena):
                    print(root.value)
                __inorden_start_with(root.right, cadena)
    
    def inorden_start_with_jedi(self, cadena):
        def __inorden_start_with_jedi(root, cadena):
            if root is not None:
                __inorden_start_with_jedi(root.left, cadena)
                if root.value.upper().startswith(cadena):
                    print(root.value)
                __inorden_start_with_jedi(root.right, cadena)

        __inorden_start_with_jedi(self.root, cadena)

    def inorden_caracter(self, caracter):
        def __inorden_start_with_jedi(root, caracter):
            if root is not None:
                __inorden_start_with_jedi(root.left, caracter)
                if caracter in root.value:
                    print(root.value)
                __inorden_start_with_jedi(root.right, caracter)

        __inorden_start_with_jedi(self.root, caracter)

    def postorden(self):
        def __postorden(root):
            if root is not None:
                __postorden(root.right)
                print(root.value)
                __postorden(root.left)

        __postorden(self.root)

    def postorden_listadoD(self, is_heroe):
        def __postorden(root, is_heroe):
            if root is not None:
                __postorden(root.right, is_heroe)
                if root.other_values == is_heroe:
                    print(root.value)
                __postorden(root.left, is_heroe)
        
        __postorden(self.root, is_heroe)


    def preorden(self):
        def __preorden(root):
            if root is not None:
                print(root.value, root.height)
                __preorden(root.left)
                __preorden(root.right)

        __preorden(self.root)

    def search_by_coincidence(self, value):
        def __search_by_coincidence(root, value):
            if root is not None:
                if root.value.startswith(value):
                    print(root.value)
                __search_by_coincidence(root.left, value)
                __search_by_coincidence(root.right, value)

        __search_by_coincidence(self.root, value)

    def search_by_coincidence_cambiada(self, value):
        def __search_by_coincidence(root, value):
            if root is not None:
                if root.value.startswith(value):
                    print(root.value, root.other_values)
                __search_by_coincidence(root.left, value)
                __search_by_coincidence(root.right, value)

        __search_by_coincidence(self.root, value)


    def search(self, key):
        def __search(root, key):
            if root is not None:
                if root.value == key:
                    return root
                elif key < root.value:
                    return __search(root.left, key)
                else:
                    return __search(root.right, key)

        return __search(self.root, key)
    

    def search_modificada(self, key):
        def __search(root, key):
            if root is not None:
                if root.value == key:
                    return root
                elif key < root.value:
                    return __search(root.left, key)
                else:
                    return __search(root.right, key)

        return __search(self.root, key)
    
    def inorden_rank(self, file_name, rank):
        def __inorden_rank(root, file_name, rank):
            if root is not None:
                __inorden_rank(root.left, file_name,rank)
                value = get_value_from_file(file_name, root.other_values)
                if rank in value[1].split('/'):
                    print(root.value, value[0].split('/'))
                __inorden_rank(root.right, file_name,rank)

        __inorden_rank(self.root, file_name,rank)

    def delete_node(self, key):
        def __replace(root):
            if root.right is None:
                return root.left, root
            else:
                root.right, replace_node = __replace(root.right)
            return root, replace_node

        def __delete(root, key):
            value = None
            if root is not None:
                if key < root.value:
                    root.left, value = __delete(root.left, key)
                elif key > root.value:
                    root.right, value = __delete(root.right, key)
                else:
                    value = root.value
                    if root.left is None and root.right is not None:
                        return root.right, value
                    elif root.right is None and root.left is not None:
                        return root.left, value
                    elif root.left is None and root.right is None:
                        return None, value
                    else:
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value
                    root = self.balancing(root)
                    self.update_height(root)
            return root, value

        delete_value = None
        if self.root is not None:
            self.root, delete_value = __delete(self.root, key)
        return delete_value

    

arbol = BinaryTree()

# for i in range(15):
#     arbol.insert_node(name, {'derrotado_por': derrotado})


# pos.other_values['capurado_por'] = 'asdas'
# arbol.preorden()

# arbol.root = arbol.balancing(arbol.root)



# print(arbol.root)
# arbol.insert_node('F')
# arbol.insert_node('B')
# # arbol.insert_node('E')
# arbol.insert_node('K')
# arbol.insert_node('H')
# arbol.insert_node('J')
# arbol.insert_node('I')
# arbol.insert_node('R')

# arbol.preorden()

# print()
# deleted = arbol.delete_node('F')
# # if deleted:
# #     print('el valor fue eliminado', deleted)
# # print()
# arbol.preorden()
# deleted = arbol.delete_node('Z')
# print()
# arbol.preorden()
# deleted = arbol.delete_node('K')
# print()
# arbol.preorden()


# print()
# pos = arbol.search('Z')
# print(pos)
# if pos:
#     print('valor encontrado', pos.value)
