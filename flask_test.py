import urllib.request as r
from urllib.parse import urlencode
import json

host = 'http://localhost:5000'

def test_index():
    res = r.urlopen(host + '/')
    res = json.loads(res.read().decode())
    print(res)
    assert type(res) == dict

def test_delete():
    req = r.Request(host + '/', method='DELETE')
    res = r.urlopen(req)
    res = json.loads(res.read().decode())
    print(res)
    assert res.get('result') == 'success'

def test_create(data):
    payload = { 'data': data }

    req = r.Request(host + '/create', data=json.dumps(payload).encode('utf-8'),
        headers={'content-type': 'application/json'})
    res = r.urlopen(req)
    res = json.loads(res.read().decode())
    print(res)
    assert res.get('result') == 'success'

def test_update(data):
    payload = { 'data': data }

    req = r.Request(host + '/update', data=json.dumps(payload).encode('utf-8'),
        headers={'content-type': 'application/json'})
    res = r.urlopen(req)
    res = json.loads(res.read().decode())
    print(res)
    assert res.get('result') == 'success'

def test_cost(route, exist=True):
    res = r.urlopen(host + '/cost/' + route)
    res = json.loads(res.read().decode())
    print(route, res)
    if exist:
        assert res.get('result') == 'success'
    else:
        assert res.get('result') == 'error'

def test_cost(route, result):
    res = r.urlopen(host + '/cost/' + route)
    res = json.loads(res.read().decode())
    print('cost', route, res)
    assert res.get('message') == result

def test_cheap(route, result):
    res = r.urlopen(host + '/cheapest/' + route)
    res = json.loads(res.read().decode())
    print('cheapest', route, res)
    assert res.get('message') == result

def test_count(route, result, **kwargs):
    res = r.urlopen(host + '/count/' + route + '?' + urlencode(kwargs))
    res = json.loads(res.read().decode())
    print('count', route, res)
    assert res.get('message') == result

test_index()
test_delete()
test_create('AC4,CD4,CF2,DE1,EB3,EA2,FD1')
test_update('AC4,AD10,BE3,AB1')

test_cost('ABE', 4)
test_cost('AD', 10)
test_cost('EACF', 8)
test_cost('ADF', 'No such route')

test_count('ED', 4, hop_limit=4)
test_count('EE', 5)
test_count('EE', 29, use_twice=True, cost_limit=20)

test_cheap('ED', 9)
test_cheap('EE', 6)

