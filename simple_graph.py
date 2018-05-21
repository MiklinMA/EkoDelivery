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

def graph_routes(graph, route, limit=None, twice=False):
    routes = []

    def walk(routes, path, depth=0):
        if limit is not None and depth>= limit:
            return

        if len(path) < 2:
            return

        src = path[-2]
        dst = path[-1]

        for k in graph[src].keys():
            if k == dst: 
                routes.append(path)
                continue
            if not twice and str(src + k) in path:
                continue

            result = walk(routes, path[:-1] + k + dst, depth+1)

    walk(routes, route)
    return routes

# Simple tests
graph = graph_create('AB1,AC4,AD10,BE3,CD4,CF2,DE1,EB3,EA2,FD1')
print(json.dumps(graph, indent=2))

print()
routes = ['ABE', 'AD', 'EACF', 'ADF']
for route in routes:
    print(route, graph_cost(graph, route))

print()
routes = [
    ('ED', 4),
    ('EE', ),
    ('EE', 20, True),
]
for route in routes:
    res = graph_routes(graph, *route)
    print()
    print(route)
    for path in res:
        print('route', path, graph_cost(graph, path))

