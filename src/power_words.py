#!/usr/bin/python

inp = { 'W' : ['p', '\'',  '.', '0', '3'],
        'E' : ['b', 'c', 'e', 'f', 'y', '2'],
        'SW': ['a', 'g', 'h', 'i', 'j', '4'],
        'SE': ['l', 'm', 'n', 'o', ' ', '5'],
        'R-': ['d', 'q', 'r', 'v', 'z', '1'],
        'R+': ['k', 's', 't', 'u', 'w', 'x'],
        ' ' : ['\t', '\n', '\r']}

inv_map = {e: k for k, v in inp.items() for e in v}

words_for_sure = ["ei!", "ia! ia!", "r'lyeh", "yuggoth"]

words_probable = ["cthulhu", "dagon", "nyarlathotep",
                  "shub-niggurath", "huitloxopetl", 
                  "ph'nglui mglw'nafh cthulhu r'lyeh wgah'nagl fhtagn"]

words = words_for_sure + words_probable

def reverse_matching(word):
    r = []
    for c in word:
        if c in inv_map:
            r.append(inv_map[c])
        else:
            print c,"not in map for word",word
            return ""
    return r

        
def main():
    for w in words:
        print "word", w
        print reverse_matching(w)

if __name__ == "__main__":
    main()
