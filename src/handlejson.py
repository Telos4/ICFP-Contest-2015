import json

data = '{"height":20,"width":15,"sourceSeeds":[0,24762,24103,12700,5864,1155,24803,29992,18660,19102],"units":[{"members":[{"x":0,"y":0}],"pivot":{"x":4,"y":0}},{"members":[{"x":0,"y":0}],"pivot":{"x":4,"y":0}},{"members":[{"x":0,"y":0}],"pivot":{"x":4,"y":0}},{"members":[{"x":0,"y":0}],"pivot":{"x":4,"y":0}},{"members":[{"x":0,"y":0}],"pivot":{"x":4,"y":0}},{"members":[{"x":0,"y":0}],"pivot":{"x":4,"y":0}},{"members":[{"x":0,"y":0}],"pivot":{"x":4,"y":0}},{"members":[{"x":0,"y":0}],"pivot":{"x":4,"y":0}},{"members":[{"x":1,"y":0},{"x":2,"y":0},{"x":0,"y":1},{"x":2,"y":1},{"x":1,"y":2},{"x":2,"y":2}],"pivot":{"x":3,"y":5}},{"members":[{"x":1,"y":0},{"x":2,"y":0},{"x":0,"y":1},{"x":2,"y":1},{"x":1,"y":2},{"x":2,"y":2}],"pivot":{"x":3,"y":5}},{"members":[{"x":1,"y":0},{"x":2,"y":0},{"x":3,"y":0},{"x":0,"y":1},{"x":3,"y":1},{"x":0,"y":2},{"x":4,"y":2},{"x":0,"y":3},{"x":3,"y":3},{"x":1,"y":4},{"x":2,"y":4},{"x":3,"y":4}],"pivot":{"x":8,"y":6}}],"id":12,"filled":[],"sourceLength":100}'

def parse_to_dictionary(s):
    try:
        return json.loads(s)
    except ValueError:
        raise ValueError('your string was invalid, it cannot be parsed to python: ' + s)


def create_response_string(d):
    _check_response_is_valide(d)
    try:
        return json.dumps(d)
    except ValueError:
        raise ValueError('your dictionary cannot be parsed to a json string')

def _check_response_is_valid(d):
    valid_keys={'problemId','seed','tag','solution'}
    if set(d.keys()) != valid_keys:
        raise ValueError('your dictionary contains wrong keys. You have: ' + str(d.keys()) + ', but it should contain: ' + str(valid_keys))
    if type(d['problemId']) is not int:
        raise ValueError('your problemId has to be an integer, you have: ' + str(d['problemId']) + ' of type: ' + str(type(d['problemId'])))
    if type(d['seed']) is not int:
        raise ValueError('your seed has to be an integer, you have: ' + str(d['seed']) + ' of type: ' + str(type(d['seed'])))
    if (type(d['tag']) is not str) and (type(d['tag']) is not type(None)):
        raise ValueError('your tag has to be a string or None, you have: ' + str(d['tag']) + ' of type: ' + str(type(d['tag'])))
    if type(d['solution']) is not str:
        raise ValueError('your solution has to be a string, you have: ' + str(d['solution']) + ' of type: ' + str(type(d['solution'])))
    valid_solution_letters=['p','\'','!','.','0','3',
                            'b','c','e','f','y','2',
                            'a','g','h','i','j','4',
                            'l','m','n','o',' ','5',
                            'd','q','r','v','z','1',
                            'k','s','t','u','w','x',
                            '\t','\n','\r']
    for i in d['solution']:
        if i not in valid_solution_letters:
            raise ValueError('your solution contains an invalid character: ' + i)
