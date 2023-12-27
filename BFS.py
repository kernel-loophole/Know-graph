from queue import Queue

class GraphProcessor:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        self.graph = self.build_graph()

    def build_graph(self):
        graph = {}

        # Add nodes to the graph
        for node in self.nodes:
            node_id = node.get('id')
            graph[node_id] = []

        # Add edges to the graph
        for edge in self.edges:
            from_node = edge.get('from')
            to_node = edge.get('to')
            if from_node is not None and to_node is not None:
                if from_node not in graph:
                    graph[from_node] = []
                graph[from_node].append(to_node)

        return graph

    def bfs_related_nodes(self, keyword):
        related_nodes = []

        for node in self.nodes:
            if keyword.lower() in node.get('label', '').lower():
                start_node = node['id']
                visited = set()
                result = []

                queue = Queue()
                queue.put(start_node)
                visited.add(start_node)

                while not queue.empty():
                    current_node = queue.get()
                    result.append(current_node)

                    for neighbor in self.graph.get(current_node, []):
                        if neighbor not in visited:
                            queue.put(neighbor)
                            visited.add(neighbor)

                # Include only those nodes that were visited during BFS
                related_nodes.extend([n for n in self.nodes if n['id'] in result])

        return related_nodes

# # Example usage:
# Nodes,edges=
# processor = GraphProcessor(nodes, edges)
# keyword = 'appoint'  # Change this to the desired keyword
# result = processor.bfs_related_nodes(keyword)

# print(result)
