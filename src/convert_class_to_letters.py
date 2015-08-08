import random

inp = { 'W' : ['p', '\'',  '!', '.', '0', '3'],
        'E' : ['b', 'c', 'e', 'f', 'y', '2'],
        'SW': ['a', 'g', 'h', 'i', 'j', '4'],
        'SE': ['l', 'm', 'n', 'o', ' ', '5'],
        'R-': ['d', 'q', 'r', 'v', 'z', '1'],
        'R+': ['k', 's', 't', 'u', 'w', 'x'],
        ' ' : ['\t', '\n', '\r', '-']} # let's also ignore '-'


movement_sequence = ['SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SE','SW','SW','SW','SW','SW','SW','SE','SE','SW','W','SW','SW','SW','SW','SW','SW','SW','SE','SE','SE','SW','SW','SW','SW','SW','SW','SE','SE','SE','SW','SE','SE','SE','SW','SW','SW','SW','SW','SE','W','SW','SW','SW','SW','SW','SW','SE','SE','SE','SE','W','SE','SE','SE','SE','SE','SE','SW','SW','SW','SW','SE','SW','SW','SW','SW','SE','SE','SE','SW','SE','SE','SE','SW','SW','SW','SW','SW','SW','SW','SE','SE','SE','SW','SW','SE','SE','SE','SW','SW','SW','SW','SW','SE','SW','SW','W','SW','SW','SW','SW','SW','SE','SE','SE','SE','SE','SW','W','SW','SW','SW','SW','SW','SW','SE','SE','SE','SE','SW','SW','W','SW','SW','SW','SW','SW','SW','SE','SE','SE','SE','SE','SE','SE','SW','SW','SW','SW','SW','SE','SE','SE','SE','SW','SW','SE','SE','SW','SW','SW','SW','SW','SW','SE','SE','SE','SE','SE','SW','SW','SE','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SE','SE','SE','W','SW','SW','SW','SW','SW','SW','SW','SW','SW','SE','SE','SE','SE','W','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SE','SE','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SE','SE','SW','SE','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SW','SE','SE','SE','SE','SE','SE','SE','SW','SW','SW','SW','SW','SW','SW','SW','SW','SE','SE','SE','SE','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','W','W','W']



out = ""
for i in movement_sequence:
	cls = inp[i]
	rep = random.choice(cls)
	out += str(rep)
print out

#agajaha4j4j4ajihoigh4j4 m40gjhha4al oaaaaiim lilolj4jaim3jghigio5n !olnmooggh4oggh4  oal5o44aihai 5ogg55 4iijj5j4.4i4ha5lnmo4!aa444jlmlmaj.4aihigmlmlmmlggg44momogg5 ih4jgan l ogjl4jjaja44j4om 3gia4ijia4l5 m!hjhjjjaiajggln4ihjaajgiiloalhj4hhgi4ijin5ooll iighijga45nlo....p.p0p'3p330!0'p0!..'!.''03..3efyceybyyfyefy2bcyccb2ef2b2eb2yfffc0..

#for problem 19