import json

from simple_graph import graph_create, graph_cost, graph_routes, graph_cheapest

# Simple tests
graph = graph_create('AB1,AC4,AD10,BE3,CD4,CF2,DE1,EB3,EA2,FD1')
assert type(graph) == dict
assert len(graph)
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

