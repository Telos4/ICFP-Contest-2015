import httplib
import json
import time

class color:
	PURPLE = '\033[95m'
	CYAN = '\033[96m'
	DARKCYAN = '\033[36m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	END = '\033[0m'

oldtime = None

while True:
	c = httplib.HTTPSConnection('davar.icfpcontest.org')
	c.request('GET','/rankings.js')
	r = c.getresponse()
	d = r.read()
	c.close()

	capped = d[11:]
	parsed = json.loads(capped)

	# tags of all people
	# sorted([ a['tags'] for a in parsed['data']['rankings'] ])


	if oldtime != parsed['time']:
		print '\n'*5 + 'NEW DATA '*200 +'\n'*5
		time.sleep(2)
		oldtime = parsed['time']

	globalscore = [ a for a in parsed['data']['rankings'] if 'Wagner' in a['team'] ][0]

	print '\n' * 30
	print color.BOLD + 'date of data:' + color.END, parsed['time']
	print color.BOLD + 'place in total:' + color.END, parsed['data']['rankings'].index(globalscore), 'of', len(parsed['data']['rankings'])
	mxrk = max( [ x['rank'] for x in parsed['data']['rankings'] ] )
	mxscr = max( [ x['score'] for x in parsed['data']['rankings'] ] )
	mxpwr = max( [ x['power_score'] for x in parsed['data']['rankings'] ] )
	print color.BOLD + 'max' + color.END +'\t%s\t%s\t%s' % (mxrk,mxscr,mxpwr)
	mn = lambda l: "%.1f" % (float(sum(l))/len(l)) if len(l) > 0 else float('nan')
	mnrk = mn( [ x['rank'] for x in parsed['data']['rankings'] ] )
	mnscr = mn( [ x['score'] for x in parsed['data']['rankings'] ] )
	mnpwr = mn( [ x['power_score'] for x in parsed['data']['rankings'] ] )
	print color.BOLD + 'mean'+color.END+'\t%s\t%s\t%s' % (mnrk,mnscr,mnpwr)
	print color.BOLD + 'nr\trank\tscore\tpower_score\ttags' + color.END
	print '-\t%s\t%s\t%s\t-' % (globalscore['rank'],globalscore['score'],globalscore['power_score'])

	for i, a in enumerate(parsed['data']['settings']):
		localscore = [ b for b in a['rankings'] if 'Wagner' in b['team'] ][0]
		print '%s\t%s\t%s\t%s\t%s' % (i, localscore['rank'], localscore['score'], localscore['power_score'], localscore['tags'])

	time.sleep(120)