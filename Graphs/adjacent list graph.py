class Graph:
    def __init__(self, no_of_nodes=0, adjacent_list={}):
        self.no_of_nodes = no_of_nodes
        self.adjacent_list = adjacent_list

    def add_vertex(self, node):
        if not self.adjacent_list.get(node):
            self.adjacent_list[node] = []
            self.no_of_nodes += 1
        return "Node already exists"

    def add_edge(self, node1, node2):
        try:
            if not (node1 and node2):
                return "Please enter correct node"
            if node1 not in self.adjacent_list.keys() or node2 not in self.adjacent_list.keys():
                return "1 of the Nodes does not exist"
            if node2 in self.adjacent_list.get(node1):
                return "Edge already exists"
            else:
                self.adjacent_list.get(node1).append(node2)
                self.adjacent_list.get(node2).append(node1)
                return "Edge successfully added"
        except Exception as exp:
            print(exp)

    def show_connections(self):
        try:
            for item in self.adjacent_list.items():
                print(f'{item[0]} -> {item[1]}')
        except Exception as exp:
            print(exp)


if __name__ == "__main__":
    myGraph = Graph()
    myGraph.add_vertex('0')
    myGraph.add_vertex('1')
    myGraph.add_vertex('2')
    myGraph.add_vertex('3')
    myGraph.add_vertex('4')
    myGraph.add_vertex('5')
    myGraph.add_vertex('6')
    myGraph.add_edge('3', '1')
    myGraph.add_edge('3', '4')
    myGraph.add_edge('4', '2')
    myGraph.add_edge('4', '5')
    myGraph.add_edge('1', '2')
    myGraph.add_edge('1', '0')
    myGraph.add_edge('0', '2')
    myGraph.add_edge('6', '5')
    myGraph.show_connections()
