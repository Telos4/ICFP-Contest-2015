import json
import subprocess


def parse_to_dictionary(s):
    try:
        return json.loads(s)
    except ValueError:
        raise ValueError('your string was invalid, it cannot be parsed to python: ' + s)

def send_response(problemid_int, seed_int, solution_str, tag_str_or_none=None):
    subprocess.call(['curl','--user',':hi4a3Ue84FtxUGqVQWla3aoBU9AMUphhm9KuscMIOFQ=','-X','POST','-H','Content-Type: application/json','-d',_create_response(problemid_int, seed_int, solution_str, tag_str_or_none),'https://davar.icfpcontest.org/teams/206/solutions'])

def _create_response(problemid_int, seed_int, solution_str, tag_str_or_none=None):
    return _create_response_from_dic({'problemId':problemid_int,'seed':seed_int,'tag':tag_str_or_none,'solution':solution_str})


def _create_response_from_dic(d):
    _check_response_is_valid(d)
    try:
        return json.dumps([d])
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
