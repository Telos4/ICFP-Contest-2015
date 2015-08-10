import json
import subprocess


allseeds={0:[0],
1:[0],
2:[0, 679, 13639, 13948, 29639, 15385, 16783, 23862, 25221, 23027],
3:[0, 29060, 6876, 31960, 6094],
4:[0, 16868, 32001, 13661, 12352, 29707, 19957, 2584, 21791, 18451, 17818, 26137, 7533, 29971, 2895, 177, 8466, 17014, 23414, 23008, 15766, 6045, 13537, 31051, 12140, 26930, 28921, 8444, 29697, 8269, 12976, 28635, 16520, 22345, 22572, 12272, 6532, 2148, 23344, 19542, 22290, 2586, 19530, 11006, 8700, 30014, 21695, 26153, 13694, 20701],
5:[0, 22837, 22837, 15215, 24851, 11460, 14027, 32620, 32719, 15577],
6:[0, 13120, 18588, 31026, 7610, 25460, 23256, 19086, 24334, 22079, 9816, 8466, 3703, 13185, 26906, 16903, 24524, 9536, 11993, 21728, 2860, 13859, 21458, 15379, 10919, 7082, 26708, 8123, 18093, 26670, 16650, 1519, 15671, 24732, 16393, 5343, 28599, 29169, 8856, 23220, 25536, 629, 24513, 14118, 17013, 6839, 25499, 17114, 25267, 8780],
7:[0, 18705, 22828, 16651, 27669],
8:[0, 28581, 10596, 4491, 19012, 8000, 14104, 20240, 2629, 5696],
9:[0, 26637, 10998, 4150, 23855],
10:[0],
11:[0, 12877, 20528, 16526, 19558],
12:[0, 24762, 24103, 12700, 5864, 1155, 24803, 29992, 18660, 19102],
13:[0],
14:[0],
15:[0],
16:[0],
17:[0],
18:[0],
19:[0],
20:[0],
21:[0],
22:[0],
23:[0],
24:[18]}


def parse_to_dictionary(s):
    try:
        return json.loads(s)
    except ValueError:
        raise ValueError('your string was invalid, it cannot be parsed to python: ' + s)

def get_dictionary_of_all_solutions():
    data = subprocess.Popen(['curl','-s','--user',':hi4a3Ue84FtxUGqVQWla3aoBU9AMUphhm9KuscMIOFQ=','-X','GET','https://davar.icfpcontest.org/teams/206/solutions'], stdout=subprocess.PIPE).communicate()[0]
    return json.loads(data)    

def send_response(problemid_int, seed_array_int, solution_str, tag_str_or_none=None):
    for s in seed_array_int:
        subprocess.Popen(['curl','-s','--user',':hi4a3Ue84FtxUGqVQWla3aoBU9AMUphhm9KuscMIOFQ=','-X','POST','-H','Content-Type: application/json','-d',_create_response(problemid_int, s, solution_str, tag_str_or_none),'https://davar.icfpcontest.org/teams/206/solutions'],stdout=subprocess.PIPE).communicate()

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
    if d['seed'] not in allseeds[d['problemId']]:
        raise ValueError('your seed is not valid for this problem')
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
