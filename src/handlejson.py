import json

data = '{"height":20,"width":40,"sourceSeeds":[0,18705,22828,16651,27669],"units":[{"members":[{"x":0,"y":0},{"x":2,"y":0}],"pivot":{"x":1,"y":0}},{"members":[{"x":1,"y":0},{"x":0,"y":1},{"x":0,"y":2}],"pivot":{"x":0,"y":1}},{"members":[{"x":2,"y":0},{"x":1,"y":0},{"x":0,"y":1}],"pivot":{"x":1,"y":0}},{"members":[{"x":1,"y":1},{"x":1,"y":0},{"x":0,"y":1}],"pivot":{"x":0,"y":0}},{"members":[{"x":2,"y":0},{"x":1,"y":1},{"x":1,"y":2},{"x":0,"y":3}],"pivot":{"x":1,"y":1}},{"members":[{"x":2,"y":0},{"x":1,"y":0},{"x":0,"y":1},{"x":0,"y":2}],"pivot":{"x":1,"y":1}},{"members":[{"x":1,"y":1},{"x":1,"y":0},{"x":0,"y":1},{"x":0,"y":2}],"pivot":{"x":0,"y":1}},{"members":[{"x":0,"y":0},{"x":1,"y":0},{"x":0,"y":1},{"x":0,"y":2}],"pivot":{"x":0,"y":1}},{"members":[{"x":1,"y":0},{"x":1,"y":1},{"x":1,"y":2},{"x":0,"y":3}],"pivot":{"x":0,"y":1}},{"members":[{"x":2,"y":0},{"x":1,"y":1},{"x":0,"y":1},{"x":0,"y":2}],"pivot":{"x":1,"y":1}},{"members":[{"x":2,"y":1},{"x":2,"y":0},{"x":1,"y":0},{"x":0,"y":1}],"pivot":{"x":1,"y":0}},{"members":[{"x":1,"y":1},{"x":2,"y":0},{"x":1,"y":0},{"x":0,"y":1}],"pivot":{"x":1,"y":0}},{"members":[{"x":0,"y":0},{"x":0,"y":1},{"x":1,"y":1},{"x":0,"y":2}],"pivot":{"x":0,"y":1}},{"members":[{"x":0,"y":1},{"x":1,"y":1},{"x":3,"y":0},{"x":2,"y":0}],"pivot":{"x":1,"y":0}}],"id":7,"filled":[{"x":0,"y":5},{"x":4,"y":5},{"x":30,"y":5},{"x":34,"y":5},{"x":1,"y":6},{"x":4,"y":6},{"x":30,"y":6},{"x":34,"y":6},{"x":1,"y":7},{"x":3,"y":7},{"x":30,"y":7},{"x":34,"y":7},{"x":2,"y":8},{"x":3,"y":8},{"x":29,"y":8},{"x":30,"y":8},{"x":31,"y":8},{"x":32,"y":8},{"x":34,"y":8},{"x":2,"y":9},{"x":5,"y":9},{"x":9,"y":9},{"x":12,"y":9},{"x":13,"y":9},{"x":14,"y":9},{"x":18,"y":9},{"x":19,"y":9},{"x":20,"y":9},{"x":24,"y":9},{"x":25,"y":9},{"x":26,"y":9},{"x":30,"y":9},{"x":34,"y":9},{"x":35,"y":9},{"x":36,"y":9},{"x":2,"y":10},{"x":6,"y":10},{"x":9,"y":10},{"x":12,"y":10},{"x":15,"y":10},{"x":18,"y":10},{"x":21,"y":10},{"x":24,"y":10},{"x":27,"y":10},{"x":30,"y":10},{"x":34,"y":10},{"x":37,"y":10},{"x":2,"y":11},{"x":5,"y":11},{"x":9,"y":11},{"x":11,"y":11},{"x":15,"y":11},{"x":17,"y":11},{"x":21,"y":11},{"x":23,"y":11},{"x":27,"y":11},{"x":30,"y":11},{"x":34,"y":11},{"x":37,"y":11},{"x":2,"y":12},{"x":6,"y":12},{"x":9,"y":12},{"x":12,"y":12},{"x":15,"y":12},{"x":18,"y":12},{"x":21,"y":12},{"x":24,"y":12},{"x":27,"y":12},{"x":30,"y":12},{"x":34,"y":12},{"x":37,"y":12},{"x":2,"y":13},{"x":6,"y":13},{"x":7,"y":13},{"x":8,"y":13},{"x":12,"y":13},{"x":13,"y":13},{"x":14,"y":13},{"x":15,"y":13},{"x":18,"y":13},{"x":19,"y":13},{"x":20,"y":13},{"x":21,"y":13},{"x":24,"y":13},{"x":25,"y":13},{"x":26,"y":13},{"x":30,"y":13},{"x":31,"y":13},{"x":34,"y":13},{"x":37,"y":13},{"x":15,"y":14},{"x":21,"y":14},{"x":14,"y":15},{"x":20,"y":15},{"x":12,"y":16},{"x":13,"y":16},{"x":14,"y":16},{"x":18,"y":16},{"x":19,"y":16},{"x":20,"y":16}],"sourceLength":100}'

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
