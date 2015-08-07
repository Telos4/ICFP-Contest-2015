import handlejson

pop_sure = ["necronomicon"]

words_probable = ["cthulhu", "dagon", 
                  "rhan-tegoth-cthulhu fthagn-ei! ei! ei! ei!-rhan-teogth.",
                  "rhan-tegoth rhan-tegoth!",
                  "ph'nglui mglw'nafh cthulhu r'lyeh wgah'nagl fhtagn",
                  "h. p. lovecraft", "azathoth", "chaugnar faugn",
                  "shoggoths"]

s = sorted(words_probable,key=len)

for i,a in enumerate(s):
	print 'sending',(i+1)%len(s),a.replace('-',' ')
	handlejson.send_response(i, 0, a.replace('-',' '))
	print ''
