import random
import itertools

inp = { 'W' : ['p', '\'',  '!', '.', '0', '3'],
        'E' : ['b', 'c', 'e', 'f', 'y', '2'],
        'SW': ['a', 'g', 'h', 'i', 'j', '4'],
        'SE': ['l', 'm', 'n', 'o', ' ', '5'],
        'R-': ['d', 'q', 'r', 'v', 'z', '1'],
        'R+': ['k', 's', 't', 'u', 'w', 'x'],
        ' ' : ['\t', '\n', '\r', '-']} # let's also ignore '-'

inp2 = { 'W' : ['p', '\'',  '!', '.', '0', '3'],
        'E' : ['b', 'c', 'e', 'f', 'y', '2'],
        'T': ['a', 'g', 'h', 'i', 'j', '4'],
        'Q': ['l', 'm', 'n', 'o', ' ', '5'],
        'Y': ['d', 'q', 'r', 'v', 'z', '1'],
        'X': ['k', 's', 't', 'u', 'w', 'x'],
        ' ' : ['\t', '\n', '\r', '-']} # let's also ignore '-'

#all_known_phrases_of_power=['ei!', 'tsathoggua', 'yuggoth', 'necronomicon', 'ia! ia!', "r'lyeh", "in his house at r'lyeh dead cthulhu waits dreaming.",'john bigboote']


def all_known_phrases_of_power_in_class_form(pop2):
    all_known_phrases_of_power_in_class_form=[]
    for pop in pop2:
        newrep=""
        for letter in pop:
            for k in inp2.keys():
                data = inp2[k]
                if letter in data:
                    newrep += k
        all_known_phrases_of_power_in_class_form.append(newrep)
    return all_known_phrases_of_power_in_class_form


def convert_back_letter_to_classes(s):
    ret = []
    for i in s:
        for k in inp.keys():
            if i in inp[k]:
                ret.append(k)
    return ret

def all_known_phrases_of_power_direction_form(pop):
    all_known_phrases_of_power_direction_form=[]
    for item in pop:
        all_known_phrases_of_power_direction_form.append(convert_back_letter_to_classes(item))
    return all_known_phrases_of_power_direction_form

def convert_random(movement_sequence, pop):
    out = ""
    for i in movement_sequence:
        cls = inp[i]
        rep = random.choice(cls)
        out += str(rep)
    return out


def _collision(a,b):
    _,sa,ea=a
    _,sb,eb=b

    if sa <= sb:
        return sb < ea
    else:
        return sa < eb


def _collision_list(l,a,positions):
    for i in l:
        if _collision(positions[i],a) == True:
            return True
    return False


def _preprocess(movement_sequence, pop):
    movement_sequence = [ x if x != 'SE' else 'Q' for x in movement_sequence]
    movement_sequence = [ x if x != 'SW' else 'T' for x in movement_sequence]
    movement_sequence = [ x if x != 'R+' else 'X' for x in movement_sequence]
    movement_sequence = [ x if x != 'R-' else 'Y' for x in movement_sequence]
    movement_sequence = "".join(movement_sequence)

    # index of all_known_phrases_of_power_in_class_form, start in movement_sequence, end in movement_sequence
    positions=[]
    for i,rep in enumerate(all_known_phrases_of_power_in_class_form(pop)):
        start = 0
        while True:
            start = movement_sequence.find(rep, start)
            if start == -1:
                break
            positions.append((i,start,start+len(rep)))
            start = start +1

    return positions, movement_sequence


def _postprocess(retind,positions,movement_sequence, pop):
    for i in retind:
        p,s,e = positions[i]
        pp = pop[p]

        mstemp = movement_sequence[:s]
        mstemp += pp
        mstemp += movement_sequence[e:]
        movement_sequence = mstemp

    for k in ['T','Q','Y','X','W','E']:
        movement_sequence = movement_sequence.replace(k,inp2[k][0])

    return movement_sequence


def convert_ilp(movement_sequence, pop):
    positions, movement_sequence = _preprocess(movement_sequence,pop)

    try:
        import gurobipy
    except ImportError:
        raise ValueError('I cannot load gurobi')

    m = gurobipy.Model()
    m.params.OutputFlag = 0
    X,Y=[],[]
    for i in range(len(positions)):
        X.append(m.addVar(vtype=gurobipy.GRB.BINARY, obj=-2*len(pop[positions[i][0]]), name='X'+str(i)))
    for j in range(len(pop)):
        Y.append(m.addVar(vtype=gurobipy.GRB.BINARY, obj=-300, name='Y'+str(j)))
    m.update()

    for i,j in itertools.combinations(range(len(positions)), 2):
        if _collision(positions[i],positions[j]):
            m.addConstr(X[i]+X[j]<=1)
    for r in range(len(pop)):
        m.addConstr(gurobipy.quicksum( X[i] for i in range(len(positions)) if all_known_phrases_of_power_in_class_form(pop)[positions[i][0]] == all_known_phrases_of_power_in_class_form(pop)[r] ) >= Y[r])
        for i in range(len(positions)):
            if all_known_phrases_of_power_in_class_form(pop)[positions[i][0]] == all_known_phrases_of_power_in_class_form(pop)[r]:
                m.addConstr( Y[r] >= X[i] )

    m.update()
    #m.write('test.lp')
    m.optimize()

    retind = [ i for i in range(len(positions)) if X[i].x >= 0.8 ]

    return _postprocess(retind,positions,movement_sequence,pop)


def convert_greedy(movement_sequence, pop):
    positions, movement_sequence = _preprocess(movement_sequence,pop)
    retind=[]

    for i,p in enumerate(positions):
        take = True
        for j,q in enumerate(positions):
            if i!=j and p[0]==q[0]:
                take = False
                break
        if take and _collision_list(retind,p,positions) == False:
            retind.append(i)

    for p in [ p for p in positions if _collision_list(retind,p,positions)==False ]:
        if _collision_list(retind,p,positions) == False:
            retind.append(positions.index(p))

    return _postprocess(retind,positions,movement_sequence,pop)