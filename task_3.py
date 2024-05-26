import heapq

class Graph:
    def __init__(self):
        self.edges = {}
        self.vertices = set()

    def add_edge(self, from_vertex, to_vertex, weight):
        if from_vertex not in self.edges:
            self.edges[from_vertex] = []
        if to_vertex not in self.edges:
            self.edges[to_vertex] = []
        self.edges[from_vertex].append((to_vertex, weight))
        self.edges[to_vertex].append((from_vertex, weight))
        self.vertices.add(from_vertex)
        self.vertices.add(to_vertex)

def dijkstra(graph, start_vertex):
    # Ініціалізація відстаней та попередників
    distances = {vertex: float('infinity') for vertex in graph.vertices}
    distances[start_vertex] = 0
    priority_queue = [(0, start_vertex)]
    heapq.heapify(priority_queue)
    shortest_path_tree = {}

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо відстань до поточної вершини більша за знайдену, пропускаємо
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph.edges[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                shortest_path_tree[neighbor] = current_vertex

    return distances, shortest_path_tree

# Створення графа та додавання ребер
graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 1)

# Визначення найкоротших шляхів від вершини 'A'
distances, shortest_path_tree = dijkstra(graph, 'A')

print("Відстані від початкової вершини:")
for vertex, distance in distances.items():
    print(f"Вершина {vertex}: {distance}")

print("\nДерево найкоротших шляхів:")
for vertex, predecessor in shortest_path_tree.items():
    print(f"Вершина {vertex}: приходить з вершини {predecessor}")
