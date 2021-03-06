# Eko Delivery Service

Eko decide to introduce a new delivery services to the market in order to support growth of E-commerce business in Thailand. Due to innovative nature of the company, the ways to use their service is very innovative one.

To use Eko Delivery Service, their customers have to define the delivery route by themselves. They can construct it by choosing multiple routes between two towns that Eko provided.

The delivery cost is equal to the summation of these routes that they choosed. Each routes in the list is only ‘one-way’, That is, a route from town A to town B does not imply the existence of a route from town B to town A. Even if both of these routes do exist, they are distinct and are not necessarily have the same cost.

The purpose of this assignments is to help Eko building the system that provide their customers with information about delivery route. you will compute the delivery cost of a certain route, the number of possible delivery route between two towns, and the cost of cheapest delivery route between two towns.

## Simple graph library

Simple graph is a pyhon module
```
graph_cheapest(graph, route)
    Find cheapest path by given source-destination route.

graph_cost(graph, route)
    Calculate cost of given route in graph

graph_create(data)
    Return new graph (dict)

graph_routes(graph, route, limit=None, twice=False, cost_limit=None)
    Return all posible routes for graph by given source and destination route

    Keyword arguments:
    limit -- hop limit (int)
    twice -- using same route twice (bool)
    cost_limit -- route cost limit (int)

    Be careful! Using same route twice may cause of system hangs!
    In this case use another kind of limit or be sure what you do.

graph_update(graph, data)
    Update given graph with data
```

## Console application

Console application uses the simple graph library and could be used to calculate routes
```
Simple graph calculator.

optional arguments:
  -h, --help       show this help message and exit
  --create string  Example: "AB1,AC4,AD10,BE3,CD4,CF2,DE1,EB3,EA2,FD1".
                   Directed graph where a node represents a town and an edge
                   represents a route between two towns. The weighting of the
                   edge represent the delivery cost between two towns. the
                   towns are named using the first letters of the alphabet. a
                   route between two town A to town B with cost of 1 is
                   represented as AB1.
  --update string  Update graph
  --delete         Delete graph
  --cost route     Calculate the delivery cost of the given delivery route.
                   Follow the route as given; do not count any extra stops. In
                   case given route is not exists, output ’No Such Route’
  --count route    Calculates the number of possible delivery route that can
                   be construct by the given condition. (Do not counts the
                   route that has 0 cost).
  --hop_limit N    The number of maximum hops between towns.
  --cost_limit N   The maximum delivery cost for route.
  --use_twice      The same route can be used twice in a delivery route
  --cheap route    Calculate the cheapest delivery route between two town.
```

## Flask REST application

Simple REST API for library. 

Limit: Only one graph for all users!

### Methods:
```
GET /
    Returns graph as JSON dict
    
PUT /
    Create graph
    
    Content-Type: application/json
    JSON: {"data": "AB1,..."}

POST /
    Update graph
    
    Content-Type: application/json
    JSON: {"data": "AB1,..."}

DELETE /
    Delete graph

GET /cost/<route>
    Return cost of given route if exist or 'No such route'

GET /cheapest/<route>
    Return cheapest cost of given route if exist or 'No such route'
    
GET /count/route
    Return count of posible routes for graph by given source and destination route (and limits)

    Arguments:
    hop limit - maximum stops (int)
    use_twice -- using same route twice (bool)
    cost_limit -- route cost limit (int)
```
