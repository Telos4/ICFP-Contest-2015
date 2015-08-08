import httplib
import json
import time

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

	print '\n' * 30
	print 'date of data:', parsed['time']
	print 'nr of teams:', len(parsed['data']['rankings'])
	print 'nr\trank\tscore\tpower_score\ttags'

	globalscore = [ a for a in parsed['data']['rankings'] if 'Wagner' in a['team'] ][0]
	print '-\t%s\t%s\t%s' % (globalscore['rank'],globalscore['score'],globalscore['power_score'])

	for i, a in enumerate(parsed['data']['settings']):
		localscore = [ b for b in a['rankings'] if 'Wagner' in b['team'] ][0]
		print '%s\t%s\t%s\t%s\t%s' % (i, localscore['rank'], localscore['score'], localscore['power_score'], localscore['tags'])

	time.sleep(120)