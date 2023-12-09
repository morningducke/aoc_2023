from math import lcm

class Node:
    def __init__(self, val: str, left: str, right: str):
        self.val = val
        self.left = left
        self.right = right

class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node: Node):
        self.graph[node.val] = node

    def get_node(self, key: str) -> Node:
        return self.graph[key]

def parse_node(line: str) -> Node:
    val, children = line.split('=')
    val = val.strip()
    left, right = children.strip().replace(" ", "").strip('()').split(',')
    return Node(val=val, left=left, right=right)

def parse_network(input_name: str) -> tuple[Graph, str]:
    graph = Graph()
    with open(input_name, "r") as f:
        instructions = f.readline().strip()
        f.readline() # skip empty line
        for line in f:
            graph.add_node(parse_node(line))
    return graph, instructions

def find_target(graph: Graph, instructions: str, start: str = 'AAA', target: str = 'ZZZ') -> int:
    node = graph.get_node(start)
    i = 0
    steps = 0
    while node.val != target:
        instruction = instructions[i]
        node = graph.get_node(node.left) if instruction == 'L' else graph.get_node(node.right)
        i += 1
        i %= len(instructions)
        steps += 1
    return steps

def check_targets(nodes: list[Node]) -> bool:
    return all(node.val[-1] == 'Z' for node in nodes)

def find_path_length(graph: Graph, instructions: str, start: str) -> int:
    node = graph.get_node(start)
    steps = 0
    i = 0
    while not node.val.endswith('Z'):
        node = graph.get_node(node.left) if instructions[i] == 'L' else graph.get_node(node.right)
        steps += 1
        i += 1
        i %= len(instructions)
    return steps

def find_all_paths_lengths(graph: Graph, instructions: str) -> list[int]:
    starts = [graph.get_node(key) for key in graph.graph.keys() if key[-1] == 'A']
    return [find_path_length(graph, instructions, start.val) for start in starts]

def find_from_all_starts(graph: Graph, instructions: str) -> int:
    nodes = [graph.get_node(key) for key in graph.graph.keys() if key[-1] == 'A']
    i = 0
    steps = 0
    while not check_targets(nodes):
        instruction = instructions[i]
        nodes = [(graph.get_node(node.left) if instruction == 'L' else graph.get_node(node.right)) for node in nodes]
        i += 1
        i %= len(instructions)
        steps += 1
    return steps

input_name = "input.txt"
graph, instructions = parse_network(input_name)
print(f"part 1, steps till target: {find_target(graph, instructions)}")
print(f"part 2, steps till all = targets: {lcm(*find_all_paths_lengths(graph, instructions))}")

        