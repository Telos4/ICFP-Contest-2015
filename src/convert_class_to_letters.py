import random
import itertools

inp = { 'W' : ['p', '\'',  '!', '.', '0', '3'],
        'E' : ['b', 'c', 'e', 'f', 'y', '2'],
        'SW': ['a', 'g', 'h', 'i', 'j', '4'],
        'SE': ['l', 'm', 'n', 'o', ' ', '5'],
        'R-': ['d', 'q', 'r', 'v', 'z', '1'],
        'R+': ['k', 's', 't', 'u', 'w', 'x'],
        }#' ' : ['\t', '\n', '\r', '-']} # let's also ignore '-'


all_known_phrases_of_power=['ei!','ia! ia!','necronomicon','yuggoth','house','dead',"cthulhu r'lyeh","wgah'nagl fhtagn"]

#map19
# movement_sequence = ['SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SE','SW','SW','SW','SW','SW','SW','SE','SE','SW','W','SW','SW','SW','SW','SW','SW','SW','SE','SE','SE','SW','SW','SW','SW','SW','SW','SE','SE','SE','SW','SE','SE','SE','SW','SW','SW','SW','SW','SE','W','SW','SW','SW','SW','SW','SW','SE','SE','SE','SE','W','SE','SE','SE','SE','SE','SE','SW','SW','SW','SW','SE','SW','SW','SW','SW','SE','SE','SE','SW','SE','SE','SE','SW','SW','SW','SW','SW','SW','SW','SE','SE','SE','SW','SW','SE','SE','SE','SW','SW','SW','SW','SW','SE','SW','SW','W','SW','SW','SW','SW','SW','SE','SE','SE','SE','SE','SW','W','SW','SW','SW','SW','SW','SW','SE','SE','SE','SE','SW','SW','W','SW','SW','SW','SW','SW','SW','SE','SE','SE','SE','SE','SE','SE','SW','SW','SW','SW','SW','SE','SE','SE','SE','SW','SW','SE','SE','SW','SW','SW','SW','SW','SW','SE','SE','SE','SE','SE','SW','SW','SE','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SE','SE','SE','W','SW','SW','SW','SW','SW','SW','SW','SW','SW','SE','SE','SE','SE','W','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SE','SE','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SE','SE','SW','SE','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SE','SE','SE','SE','SE','SE','SE','SW','SW','SW','SW','SW','SW','SW','SW','SW','SE','SE','SE','SE','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','W','W','W']

#map0
#movement_sequence = ['SW','SW','SW','SW','SW','R-','R-','R-','W','W','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SE','SW','SW','SW','SW','SW','SE','SE','SW','SW','SW','SE','SW','SW','SE','SE','SE','R-','R-','R-','SE','SE','SE','SE','SE','E','SE','SE','SE','SE','SE','SE','SE','SE','SW','SE','SE','SE','SE','SE','SE','SE','SE','SW','SE','SE','SE','SE','SE','SW','SE','SE','SW','SE','SE','SE','SW','SW','SW','SE','SE','SE','SE','SE','SE','SE','R-','R-','R-','E','E','E','SE','SE','R-','SE','SE','SE','SE','SE','SE','SE','R-','SE','SE','SE','SW','SW','SE','SE','E','E','SE','SE','SE','SE','SE','SE','SW','SW','SW','R-','SW','SW','SE','SE','SE','SW','SW','SW','SW','SW','SW','W','W','SE','SE','R-','R-','R-','SE','SE','SW','SW','SE','SE','SW','SW','SE','SE','SW','SE','SE','SE','SW','SW','SW','SE','SW','SE','SE','SE','SW','SW','SW','R+','SW','SW','SE','SW','SW','W','W','SE','SE','SE','SE','SE','SE','E','SE','SE','SW','SW','SW','SW','W','SW','SW','SE','SE','SE','R-','SE','SE','E','E','E','E','SW','SW','SW','SW','SE','SE','SW','SW','SE','SE','SE','SE','SE','R-','R-','SW','SW','SW','SW','SW','SE','SE','SE','SE','E','E','E','SW','SW','SW','SW','W','W','W','SW','SW','SW','SW','SW','SW','SW','SE','SE','E','E','E','SE','SE','SE','SE','R+','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SE','SE','SE','SE','SE','SE','SE','SW','SE','SE','SE','SE','SE','SE','SW','SW','SE','SE','SE','SE','SW','SW','SW','SW','SW','SE','SW','SW','SW','SW','SE','SE','SW','R-','R-','R-','SE','SW','SE','SE','SW','SW','SW','SE','SE','SW','SE','SE','SE','SE','SE','SE','SE','SE','SW','SE','SE','SW','SW','SW','SW','SW','SE','SW','SE','SE','SE','SE','SW','SW','SW','SW','SE','SE','SW','SW','SW','SW','SW','SW','SE','SE','SE','SE','R-','R-','R-','E','E','E','E','SE','SE','SE','R-','R-','R-','SE','SE','SE','SE','SE','R-','R-','R-','SW','SE','SE','SE','SW','SW','SW','SW','SW','SW','SE','SE','SE','SW','SE','SE','SW','SW','SE','SE','SE','SE','SW','SW','SW','SW','SW','R-','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SE','SW','SW','SE','SW','R-','SW','SW','SW','SE','SE','SE','SW','SW','SW','SW','W','W','SW','SW','SW','SW','SW','SE','SE','SW','SW','SW','SW','SE','SW','SE','SE','SE','E','E','SE','SE','SE','SE','SE','SE','SE','R-','SE','SW','SW','SE','SE','SE','SE','SE','SE','E','E','SE','SE','SW','SE','SW','SW','SW','SE','SE','E','SE','E','E','SW','SW','R+','SW','SW','SW','SW','SW','SE','SE','SE','SW','SE','SW','SW','SW','SW','SE','SE','E','E','SE','SE','SE','SW','SW','SE','SW','SW','SE','SE','R-','SE','SW','SE','SE','E','E','E','R-','E','SE','SE','SE','SE','SE','SE','SE','SE','SE','SE','SE','SW','SW','SW','W','W','R-','SW','SW','SW','SW','SW','SE','E','E','E','R-','E','SE','SE','SW','SW','SE','SW','SW','SW','SW','SW','SW','SE','SW','SW','SE','SE','R-','E','SE','SE','SE','SW','SW','SW','SW','W','W','SW','SE','SE','SE','SW','SW','SW','SW','W','SW','SW','SW','SE','SE','W','SW','SW','SE','SE','SW','W','W','W','SW','SW','W','W','W','SW','SW','SW','SE','SE','SE','E','SE','SE','SE','SE','SE','E','SE','R-','SW','R-','SW','R-','SW','SW','SW','SW','SE','SW','R-','SW','SW','SW','E','E','SE','R-','SE','SW','SW']

def convert_random(movement_sequence):
    out = ""
    for i in movement_sequence:
        cls = inp[i]
        rep = random.choice(cls)
        out += str(rep)
    return out

#for problem 19
#agajaha4j4j4ajihoigh4j4 m40gjhha4al oaaaaiim lilolj4jaim3jghigio5n !olnmooggh4oggh4  oal5o44aihai 5ogg55 4iijj5j4.4i4ha5lnmo4!aa444jlmlmaj.4aihigmlmlmmlggg44momogg5 ih4jgan l ogjl4jjaja44j4om 3gia4ijia4l5 m!hjhjjjaiajggln4ihjaajgiiloalhj4hhgi4ijin5ooll iighijga45nlo....p.p0p'3p330!0'p0!..'!.''03..3efyceybyyfyefy2bcyccb2ef2b2eb2yfffc0..


#for map0
#a4gji1rvp0gih4jg44jg4laaj4h 5hajlginnoqdd nm552nnnn5 m jooonnl5nhoo o am g lmhh4l nonllvz1ycc5 r5ooo5  ql5 ga55eenomolnah4r445mmhajahi0'mlqzq ojanogao i mmaijlhnomgigkaim4hpp mm  mcomiiij0i4oomd55y2bfaghjnlagmloo5rqhjgiimmmmybfjgja00!jhg4jihm cyb5lm5uhhgigjaahgg4ll n555immo loghmnnl4j4gh5g4a4mng1drnil5hhjol4ollo 55lammg4hgjn4 mn5hg4gmlgh4ij45lnnrddccbfonov115 nonr1rjo 5ajjhiglmmj5ni4no5m4iiagdajghggjghja44aghigilha5ivjghllngjaa''g44gj5 iigjohn5nbbll nn5odo4hmnlooocb5o4ojgj  y5224at4iiii  ogoaghglmyb mlgjmh4 lznhnlb2ere5ooon lmo nagh.pvagjailc2fqc5nggn4a4igg aao5vc5lnhhih'!g olgjhjpj4am pii55j0.'i43.'h445 oy5n5 52ld4q4qghhini1a4hby5r h4


def convert_ilp(movement_sequence):
    all_known_phrases_of_power_in_class_form=[]

    for pop in all_known_phrases_of_power:
        newrep=""
        for letter in pop:
            for k in inp.keys():
                data = inp[k]
                if letter in data:
                    newrep += k
        all_known_phrases_of_power_in_class_form.append(newrep)

    print all_known_phrases_of_power_in_class_form


    # index of all_known_phrases_of_power_in_class_form, start in movement_sequence, end in movement_sequence
    positions=[]
    for i,rep in enumerate(all_known_phrases_of_power_in_class_form):
        start = 0
        while True:
            start = movement_sequence.find(rep, start)
            if start == -1:
                break
            positions.append((i,start,start+len(rep)))
            start = start +1

    print positions

    try:
        import gurobipy
    except ImportError:
        raise ValueError('I cannot load gurobi')


    def collision(a,b):
        _,sa,ea=a
        _,sb,eb=b
        
        if sa <= sb:
            return sb < ea
        else:
            return sa < eb



    m = gurobipy.Model()
    #m.params.OutputFlag = 0
    X=[]
    Y=[]
    for i in range(len(positions)):
        X.append(m.addVar(vtype=gurobipy.GRB.BINARY, obj=-2*len(all_known_phrases_of_power[positions[i][0]]), name='X'+str(i)))
    for j in range(len(all_known_phrases_of_power)):
        Y.append(m.addVar(vtype=gurobipy.GRB.BINARY, obj=-300, name='Y'+str(j)))
    m.update()

    for i,j in itertools.combinations(range(len(positions)), 2):
        if collision(positions[i],positions[j]):
            m.addConstr(X[i]+X[j]<=1)
    for r in range(len(all_known_phrases_of_power)):
        m.addConstr(gurobipy.quicksum( X[i] for i in range(len(positions)) if all_known_phrases_of_power_in_class_form[positions[i][0]] == all_known_phrases_of_power_in_class_form[r] ) >= Y[r])
        for i in range(len(positions)):
            if all_known_phrases_of_power_in_class_form[positions[i][0]] == all_known_phrases_of_power_in_class_form[r]:
                m.addConstr( Y[r] >= X[i] )

    m.update()
    m.write('test.lp')
    m.optimize()
    

    retind=[]
    for i in range(len(positions)):
        if X[i].x >= 0.8:
            retind.append(i)

    for i in retind:
        p,s,e = positions[i]
        pp = all_known_phrases_of_power[p]
        
        mstemp = movement_sequence[:s]
        mstemp += pp
        mstemp += movement_sequence[e:]
        movement_sequence = mstemp

    print movement_sequence

    for k in inp.keys():
        movement_sequence = movement_sequence.replace(k,inp[k][0])
    return movement_sequence






