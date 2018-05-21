import re

def graph_update(graph, data):
    data = data.split(',')
    for el in data:
        m = re.search(r'(\S)([\S])(\d+)', el)
        if not m:
            continue
        src = m.group(1)
        dst = m.group(2)
        cost = m.group(3)
        graph.setdefault(src, {})[dst] = int(cost)

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
            total += graph[a][b]
        else:
            return None

    return total

def graph_routes(graph, route, limit=None, twice=False, cost_limit=None):
    routes = []

    def walk(routes, path, depth=0):
        if limit is not None and depth >= limit:
            return

        if len(path) < 2:
            return

        src = path[-2]
        dst = path[-1]

        for k in graph[src].keys():
            if k == dst: 

                if cost_limit is None:
                    routes.append(path)
                    continue
                else:
                    cost = graph_cost(graph, path)
                    if cost_limit > cost:
                        routes.append(path)
                    else:
                        continue

            if not twice and str(src + k) in path:
                continue

            walk(routes, path[:-1] + k + dst, depth+1)

    walk(routes, route)
    return routes

def graph_cheapest(graph, route):
    routes = graph_routes(graph, route)
    cheapest = None
    for path in routes:
        cost = graph_cost(graph, path)
        if cheapest is None or cost < cheapest:
            cheapest = cost

    return cheapest

# Simple tests
graph = graph_create('AB1,AC4,AD10,BE3,CD4,CF2,DE1,EB3,EA2,FD1')
assert type(graph) == dict
assert len(graph)
import json
print(json.dumps(graph, indent=2))

print()
routes = [
    ('ABE', 4),
    ('AD', 10),
    ('EACF', 8),
    ('ADF', None),
]
for route in routes:
    result = graph_cost(graph, route[0])
    print(route[0], result)
    assert result == route[1]

print()
routes = [
    (('ED', 4), 4),
    (('EE', ), 5),
    (('EE', None, True, 20), 29),
    (('EE', None, True, 40), 1147),
    (('EE', None, True, 50), 7925),
]
for route in routes:
    res = graph_routes(graph, *route[0])
    print(route[0], len(res))
    assert len(res) == route[1]

print()
routes = [
    ('ED', 9),
    ('EE', 6),
    ('AA', 6),
    ('CA', 6),
]
for route in routes:
    res = graph_cheapest(graph, route[0])
    print(route[0], res)
    assert res == route[1]

