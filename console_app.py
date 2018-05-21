#!/usr/bin/env python3

import argparse

from simple_graph import graph_load, graph_save
from simple_graph import graph_create, graph_update, graph_cost, graph_routes, graph_cheapest

parser = argparse.ArgumentParser(description='Simple graph calculator.')

parser.add_argument('--create', metavar='string', type=str,
                   help='Example: "AB1,AC4,AD10,BE3,CD4,CF2,DE1,EB3,EA2,FD1". Directed graph where a node represents a town and an edge represents a route between two towns. The weighting of the edge represent the delivery cost between two towns. the towns are named using the first letters of the alphabet. a route between two town A to town B with cost of 1 is represented as AB1.')
parser.add_argument('--update', metavar='string', type=str,
                   help='Update graph')
parser.add_argument('--delete', action='store_const', const='delete',
                   help='Delete graph')
parser.add_argument('--cost', metavar='route', type=str,
                   help='Calculate the delivery cost of the given delivery route. Follow the route as given; do not count any extra stops. In case given route is not exists, output ’No Such Route’')
parser.add_argument('--count', metavar='route', type=str,
                   help='Calculates the number of possible delivery route that can be construct by the given condition. (Do not counts the route that has 0 cost).')
parser.add_argument('--hop_limit', metavar='N', type=int,
                   help='The number of maximum hops between towns.')
parser.add_argument('--cost_limit', metavar='N', type=int,
                   help='The maximum delivery cost for route.')
parser.add_argument('--use_twice', action='store_const', const=True,
                   help='The same route can be used twice in a delivery route')
parser.add_argument('--cheap', metavar='route', type=str,
                   help='Calculate the cheapest delivery route between two town.')


def main(args):
    graph = None

    if args.create:
        graph = graph_create(args.create)
        print('Graph created')
        return
    elif args.delete:
        print('Graph deleted')
        return

    graph = graph_load()

    if args.update:
        graph_update(graph, args.update)
        print('Graph updated')
    elif args.cost:
        res = graph_cost(graph, args.cost)
        print('Cost:', args.cost, '=', res or 'No such route')
    elif args.count:
        res = graph_routes(graph, args.count, args.hop_limit, args.use_twice, args.cost_limit)
        print('Count:', args.count, '=', len(res))
    elif args.cheap:
        res = graph_cheapest(graph, args.cheap)
        print('Cheapest:', args.cheap, '=', res or 'No such route')
    else:
        parser.print_help()

    graph_save(graph)

if __name__ == '__main__':
    args = parser.parse_args()
    main(args)

