import json
import httplib


#conn = httplib.HTTPConnection("icfpcontest.org")
#conn.request("GET", "/problems/problem_0.json")
#data = conn.getresponse().read()
#conn.close()

#print data

data = '{"height":10,"width":10,"sourceSeeds":[0],"units":[{"members":[{"x":0,"y":0}],"pivot":{"x":0,"y":0}},{"members":[{"x":0,"y":0},{"x":2,"y":0}],"pivot":{"x":1,"y":0}},{"members":[{"x":0,"y":0},{"x":0,"y":2}],"pivot":{"x":0,"y":1}},{"members":[{"x":2,"y":0},{"x":0,"y":1},{"x":2,"y":2}],"pivot":{"x":1,"y":1}},{"members":[{"x":0,"y":0},{"x":1,"y":1},{"x":0,"y":2}],"pivot":{"x":0,"y":1}},{"members":[{"x":0,"y":0},{"x":1,"y":0}],"pivot":{"x":0,"y":0}},{"members":[{"x":0,"y":0},{"x":1,"y":0}],"pivot":{"x":1,"y":0}},{"members":[{"x":0,"y":0},{"x":0,"y":1}],"pivot":{"x":0,"y":0}},{"members":[{"x":0,"y":0},{"x":0,"y":1}],"pivot":{"x":0,"y":1}},{"members":[{"x":0,"y":0},{"x":1,"y":0},{"x":2,"y":0}],"pivot":{"x":0,"y":0}},{"members":[{"x":0,"y":0},{"x":1,"y":0},{"x":2,"y":0}],"pivot":{"x":1,"y":0}},{"members":[{"x":0,"y":0},{"x":1,"y":0},{"x":2,"y":0}],"pivot":{"x":2,"y":0}},{"members":[{"x":0,"y":0},{"x":0,"y":1},{"x":0,"y":2}],"pivot":{"x":0,"y":0}},{"members":[{"x":0,"y":0},{"x":0,"y":1},{"x":0,"y":2}],"pivot":{"x":0,"y":1}},{"members":[{"x":0,"y":0},{"x":0,"y":1},{"x":0,"y":2}],"pivot":{"x":0,"y":2}},{"members":[{"x":1,"y":0},{"x":0,"y":1},{"x":1,"y":2}],"pivot":{"x":1,"y":0}},{"members":[{"x":1,"y":0},{"x":0,"y":1},{"x":1,"y":2}],"pivot":{"x":1,"y":1}},{"members":[{"x":1,"y":0},{"x":0,"y":1},{"x":1,"y":2}],"pivot":{"x":1,"y":2}}],"id":0,"filled":[],"sourceLength":100}'


def parse_to_dictionary(s):
    try:
        return json.loads(s)
    except ValueError:
        raise ValueError('your string was invalid, it cannot be parsed to python: ' + s)


def create_response_string(d):
    check_response_is_valide(d)
    try:
        return json.dumps(d)
    except ValueError:
        raise ValueError('your dictionary cannot be parsed to a json string')

def check_response_is_valid(d):
    valid_keys={'problemId','seed','tag','solution'}
    if set(d.keys()) != valid_keys:
        raise ValueError('your dictionary contains wrong keys. You have: ' + str(d.keys()) + ', but it should contain: ' + str(valid_keys))
    if type(d['problemId']) is not int:
        raise ValueError('your problemId has to be an integer, you have: ' + str(d['problemId'] + ' of type: ' + str(type(d['problemId']))))
    if type(d['seed']) is not int:
        raise ValueError('your seed has to be an integer, you have: ' + str(d['seed'] + ' of type: ' + str(type(d['seed']))))
    if (type(d['tag']) is not str) and (type(d['tag']) is not None):
        raise ValueError('your tag has to be a string, you have: ' + str(d['tag'] + ' of type: ' + str(type(d['tag']))))


print parse_to_dictionary(data)
print parse_to_dictionary(data)['sourceLength']


check_response_is_valid({'problemId':'a','seed':100,'tag':'a','solution':'abc'})
