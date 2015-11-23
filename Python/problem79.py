# This was mostly solved by hand. This code
# was used to generate a directed graph from the password
# fragments. Then I used that to create my graph, taking 0 as the
# end digit and working backwards.


def init_graph():
    graph = {}
    for i in range(10):
        graph[i] = []
    return graph

def process_keylog(graph):
    with open("keylog.txt","r") as file:
        for line in file.readlines():
            for i in range(2):
                if int(line[i+1]) not in graph[int(line[i])]:
                    graph[int(line[i])].append(int(line[i+1]))

graph = init_graph()
process_keylog(graph)

print(graph)