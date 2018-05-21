import re
import json

def graph_update(graph, data):
    data = data.split(',')
    for el in data:
        m = re.search(r'(\S)([\S])(\d+)', el)
        if not m:
            continue
        src = m.group(1)
        dst = m.group(2)
        cost = m.group(3)
        graph.setdefault(src, {})[dst] = cost

def graph_create(data):
    graph = {}
    graph_update(graph, data)
    return graph

def graph_cost(graph, route):
    total = 0
    try:
        if isinstance(route, (list,tuple)):
            route = ''.join(route)
    except TypeError:
        return None

    for i in range(len(route) - 1):
        a = route[i]
        b = route[i+1]

        if graph.get(a) and graph[a].get(b):
            total += int(graph[a][b])
        else:
            return None

    return total

# Simple tests
graph = graph_create('AB1,AC4,AD10,BE3,CD4,CF2,DE1,EB3,EA2,FD1')
print(json.dumps(graph, indent=2))

routes = ['ABE', 'AD', 'EACF', 'ADF']
for route in routes:
    print(route, graph_cost(graph, route))

