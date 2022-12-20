
from queue import PriorityQueue
class Graph:
    def __init__(self, jumlah_vertex):
        self.visited = []
        self.edges = [[-1 for x in range(jumlah_vertex)] for y in range(jumlah_vertex)]
        self.v = jumlah_vertex

    def tambah_edge(self, titik_awal, titik_target, weight):
        self.edges[titik_target][titik_awal] = weight
        self.edges[titik_awal][titik_target] = weight
def dijkstra(graph, priority):
    
    dijk = {v:float('inf') for v in range(graph.v)}
    dijk[priority] = 0

    pq = PriorityQueue()
    pq.put((0, priority))

    while not pq.empty():
        (jarak, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    baru = dijk[current_vertex] + distance
                    lama = dijk[neighbor]
                    if baru < lama:
                        pq.put((baru, neighbor))
                        dijk[neighbor] = baru
 
    return dijk


titik_awal=[0,0,0,1,1,1,2,2,2,3,3,3]
titik_target=[1,2,3,0,2,3,0,1,3,0,1,2]
weight=[2524,6344,7126,2524,4664,5578,6344,4664,943,7126,5578,943]
graph = Graph(max(titik_awal+titik_target)+1)
for i in range(len(titik_awal)):
    graph.tambah_edge(titik_awal[i],titik_target[i],weight[i])


titik_player=3
dijk = dijkstra(graph, titik_player)


for vertex in range(len(dijk)):
    print(f"Jarak terdekat dari Quest {titik_player} ke Quest", vertex, "yaitu", dijk[vertex])



