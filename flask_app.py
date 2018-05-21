#!/usr/bin/env python3
from flask import Flask, jsonify, request, abort

from simple_graph import graph_load, graph_save
from simple_graph import graph_create, graph_update, graph_cost
from simple_graph import graph_routes, graph_cheapest

app = Flask(__name__)

graph = graph_load()

@app.route('/', methods=['GET'])
def index():
    global graph
    return jsonify(graph)

@app.route('/', methods=['DELETE'])
def delete():
    graph = {}
    graph_save(graph)
    return jsonify({
        'result': 'success',
        'message': 'Graph deleted'
    })

@app.route('/', methods=['PUT'])
def create():
    if not request.json or not 'data' in request.json:
        abort(400)

    global graph

    try:
        graph = graph_create(request.json['data'])
        graph_save(graph)
    except Exception as e:
        return jsonify({
            'result': 'error',
            'message': str(e)
        })

    return jsonify({
        'result': 'success',
        'message': 'Graph created'
    })

@app.route('/', methods=['POST'])
def update():
    if not request.json or not 'data' in request.json:
        abort(400)

    global graph

    try:
        graph_update(graph, request.json['data'])
        graph_save(graph)
    except Exception as e:
        return jsonify({
            'result': 'error',
            'message': str(e)
        })

    return jsonify({
        'result': 'success',
        'message': 'Graph updated'
    })

@app.route('/cost/<string:route>', methods=['GET'])
def cost(route):
    res = graph_cost(graph, route)
    if res:
        return jsonify({
            'result': 'success',
            'message': res
        })
    else:
        return jsonify({
            'result': 'error',
            'message': 'No such route'
        })

@app.route('/cheapest/<string:route>', methods=['GET'])
def cheapest(route):
    res = graph_cheapest(graph, route)
    if res:
        return jsonify({
            'result': 'success',
            'message': res
        })
    else:
        return jsonify({
            'result': 'error',
            'message': 'No such route'
        })

@app.route('/count/<string:route>', methods=['GET'])
def count(route):
    try:
        res = graph_routes(graph, route,
            request.args.get('hop_limit', None, int),
            request.args.get('use_twice', False, bool),
            request.args.get('cost_limit', None, int)
        )
    except Exception as e:
        return jsonify({
            'result': 'error',
            'message': str(e)
        })

    return jsonify({
        'result': 'success',
        'message': len(res)
    })


if __name__ == '__main__':
    app.run(debug=True)
