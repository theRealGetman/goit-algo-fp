import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r,
                          y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, title):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(12, 8))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)
    plt.title(title)
    plt.show()


def generate_color(step, total_steps):
    # Змінюємо кольори від темних до світлих
    r = int(18 + (237 - 18) * (step / total_steps))
    g = int(40 + (230 - 40) * (step / total_steps))
    b = int(40 + (230 - 40) * (step / total_steps))
    return f"#{r:02x}{g:02x}{b:02x}"


def inorder_traversal(node, visit, step=1):
    if node is not None:
        step = inorder_traversal(node.left, visit, step)
        visit(node, step)
        step += 1
        step = inorder_traversal(node.right, visit, step)
    return step


def bfs_traversal(node, visit):
    queue = deque([node])
    step = 1
    while queue:
        current = queue.popleft()
        if current is not None:
            visit(current, step)
            step += 1
            queue.append(current.left)
            queue.append(current.right)
    return step


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def visualize_traversal(tree_root, traversal_func, title):
    total_steps = count_nodes(tree_root)

    def visit(node, step):
        node.color = generate_color(step, total_steps)

    traversal_func(tree_root, visit)
    draw_tree(tree_root, title)

# Функція для побудови бінарної купи з масиву


def build_heap(array):
    n = len(array)
    nodes = [Node(key) for key in array]

    for i in range(n):
        if 2 * i + 1 < n:
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < n:
            nodes[i].right = nodes[2 * i + 2]

    return nodes[0] if nodes else None


# Приклад масиву для побудови бінарної купи
heap_array = [10, 15, 30, 40, 50, 100, 40]

# Побудова дерева
tree_root = build_heap(heap_array)

# Візуалізація обходу в глибину
print("Обхід в глибину (Inorder Traversal):")
visualize_traversal(tree_root, inorder_traversal, "Inorder Traversal")

# Візуалізація обходу в ширину
print("Обхід в ширину (BFS Traversal):")
visualize_traversal(tree_root, bfs_traversal, "BFS Traversal")
