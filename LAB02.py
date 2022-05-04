# Busqueda en Anchura
from Nodos import Nodo

def BPA_solucion(estado_inicial, solucion):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []

    nodo_raiz = Nodo(estado_inicial)
    nodos_frontera.append(nodo_raiz)
    while (not resuelto) and len(nodos_frontera) != 0:
        nodo_actual = nodos_frontera.pop(0)
        # extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodo_actual)
        if nodo_actual.get_estado() == solucion:
            # solucion encontrada
            resuelto = True
            return nodo_actual
        else:
            # expandir nodos hijo
            estado_nodo = nodo_actual.get_estado()

            # 1
            hijo = [estado_nodo[1], estado_nodo[0], estado_nodo[2], estado_nodo[3], estado_nodo[4], estado_nodo[5], estado_nodo[6], estado_nodo[7], estado_nodo[8], estado_nodo[9]]
            hijo_primero = Nodo(hijo)
            if not hijo_primero.en_lista(nodos_visitados) and not hijo_primero.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_primero)

            # 2
            hijo = [estado_nodo[0], estado_nodo[2], estado_nodo[1], estado_nodo[3], estado_nodo[4], estado_nodo[5], estado_nodo[6], estado_nodo[7], estado_nodo[8], estado_nodo[9]]
            hijo_segundo = Nodo(hijo)
            if not hijo_segundo.en_lista(nodos_visitados) and not hijo_segundo.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_segundo)

            # 3
            hijo = [estado_nodo[0], estado_nodo[1], estado_nodo[3], estado_nodo[2], estado_nodo[4], estado_nodo[5], estado_nodo[6], estado_nodo[7], estado_nodo[8], estado_nodo[9]]
            hijo_tercero = Nodo(hijo)
            if not hijo_tercero.en_lista(nodos_visitados) and not hijo_tercero.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_tercero)

            # 4
            hijo = [estado_nodo[0], estado_nodo[1], estado_nodo[2], estado_nodo[4], estado_nodo[3], estado_nodo[5], estado_nodo[6], estado_nodo[7], estado_nodo[8], estado_nodo[9]]
            hijo_cuarto = Nodo(hijo)
            if not hijo_cuarto.en_lista(nodos_visitados) and not hijo_cuarto.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_cuarto)

            # 5
            hijo = [estado_nodo[0], estado_nodo[1], estado_nodo[2], estado_nodo[3], estado_nodo[5], estado_nodo[4], estado_nodo[6], estado_nodo[7], estado_nodo[8], estado_nodo[9]]
            hijo_quinto = Nodo(hijo)
            if not hijo_quinto.en_lista(nodos_visitados) and not hijo_quinto.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_quinto)

            # 6
            hijo = [estado_nodo[0], estado_nodo[1], estado_nodo[2], estado_nodo[3], estado_nodo[4], estado_nodo[6], estado_nodo[5], estado_nodo[7], estado_nodo[8], estado_nodo[9]]
            hijo_sexto = Nodo(hijo)
            if not hijo_sexto.en_lista(nodos_visitados) and not hijo_sexto.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_sexto)

            # 7
            hijo = [estado_nodo[0], estado_nodo[1], estado_nodo[2], estado_nodo[3], estado_nodo[4], estado_nodo[5], estado_nodo[7], estado_nodo[6], estado_nodo[8], estado_nodo[9]]
            hijo_septimo = Nodo(hijo)
            if not hijo_septimo.en_lista(nodos_visitados) and not hijo_septimo.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_septimo)

            # 8
            hijo = [estado_nodo[0], estado_nodo[1], estado_nodo[2], estado_nodo[3], estado_nodo[4], estado_nodo[5], estado_nodo[6], estado_nodo[8], estado_nodo[7], estado_nodo[9]]
            hijo_octavo = Nodo(hijo)
            if not hijo_octavo.en_lista(nodos_visitados) and not hijo_octavo.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_octavo)

            # 9
            hijo = [estado_nodo[0], estado_nodo[1], estado_nodo[2], estado_nodo[3], estado_nodo[4], estado_nodo[5], estado_nodo[6], estado_nodo[7], estado_nodo[9], estado_nodo[8]]
            hijo_noveno = Nodo(hijo)
            if not hijo_noveno.en_lista(nodos_visitados) and not hijo_noveno.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_noveno)

            nodo_actual.set_hijo([hijo_primero, hijo_segundo, hijo_tercero, hijo_cuarto, hijo_quinto, hijo_sexto, hijo_septimo, hijo_octavo, hijo_noveno])


if __name__ == "__main__":
    estado_inicial = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]
    solucion = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    nodo_solucion = BPA_solucion(estado_inicial, solucion)
    # mostrar resultado
    resultado = []
    nodo_actual = nodo_solucion
    while nodo_actual.get_padre() is not None:
        resultado.append(nodo_actual.get_estado())
        nodo_actual = nodo_actual.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)
