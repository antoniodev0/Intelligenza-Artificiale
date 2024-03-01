from queue import PriorityQueue

# Funzione principale UCS (Uniform Cost Search)
def ucs(graph, partenza, destinazione):
    # Inizializzazione della coda prioritaria, dell'insieme degli esplorati e dei dizionari dei costi e del percorso
    frontier = PriorityQueue()
    frontier.put((0, partenza))
    explored = set()
    costs = {city: float('inf') for city in graph}
    costs[partenza] = 0
    path = {partenza: None} #path è il dizionario che tiene traccia del percorso

    # Ciclo principale dell'algoritmo UCS
    while not frontier.empty():
        cost, nodo_corrente = frontier.get() #cost rappresenta il costo accumulato fino al nodo corrente durante l'esecuzione dell'algoritmo.

        # Verifica se il nodo corrente è la destinazione
        if nodo_corrente == destinazione:
            print("Percorso trovato:")
            print_path(path, destinazione)
            print("Costo totale del percorso:", costs[destinazione])
            break

        # Se il nodo corrente non è ancora stato esplorato
        if nodo_corrente not in explored:
            explored.add(nodo_corrente)

            # Esplorazione dei vicini del nodo corrente
            for neighbor, weight in graph[nodo_corrente].items():
                new_cost = costs[nodo_corrente] + weight

                # Aggiornamento dei costi se il nuovo costo è minore
                if new_cost < costs[neighbor]:
                    costs[neighbor] = new_cost
                    frontier.put((new_cost, neighbor))
                    path[neighbor] = nodo_corrente

    else:
        print("Errore: Percorso non trovato.")

# Funzione per stampare il percorso da una città di partenza fino alla città di destinazione
def print_path(path, nodo_corrente):
    if nodo_corrente is not None:
        print_path(path, path[nodo_corrente])
        print(nodo_corrente, end=' -> ')

# Funzione per consentire all'utente di inserire le città di partenza e destinazione
def get_user_input():
    città_partenza = input("Inserisci la città di partenza: ").capitalize()
    città_destinazione = input("Inserisci la città di destinazione: ").capitalize()
    return città_partenza, città_destinazione

# Definizione del grafo delle città della Romania
mappa_romania = {
    'Arad': {'Zerind':75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Oradea': 71, 'Arad': 75},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70,'Drobeta': 75} ,
    'Drobeta':{'Craiova': 120 ,'Mehadia': 75} ,
    'Craiova':{'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Rimnicu Vilcea':{'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
    'Pitesti':{'Craiova': 138, 'Rimnicu Vilcea': 97, 'Bucarest': 101},
    'Bucarest':{'Pitesti': 101, 'Giurgiu': 90, 'Fagaras': 211, 'Urziceni': 85},
    'Giurgiu':{'Bucarest': 90},
    'Fagaras':{'Sibiu': 99, 'Bucarest': 211},
    'Urziceni':{'Bucarest': 85, 'Vaslui': 142, 'Hirsova': 98},
    'Hirsova':{'Urziceni': 98, 'Eforie': 86},
    'Eforie':{'Hirsova': 86},
    'Vaslui':{'Urziceni': 142, 'Iasi': 92},
    'Iasi':{'Vaslui': 92, 'Neamt': 87},
    'Neamt':{'Iasi': 87}
}

# Ciclo principale per permettere all'utente di eseguire più ricerche
while True:
    città_partenza, città_destinazione = get_user_input()
    ucs(mappa_romania, città_partenza, città_destinazione)

    another_op = input("Vuoi inserire un'altra meta da calcolare? (Y/N): ")
    if another_op.lower() != 'y':
        break
