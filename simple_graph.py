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

