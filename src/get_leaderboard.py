import httplib
import json
import time

while True:
	c = httplib.HTTPSConnection('davar.icfpcontest.org')
	c.request('GET','/rankings.js')
	r = c.getresponse()
	d = r.read()
	c.close()

	capped = d[11:]
	parsed = json.loads(capped)

	print '\n' * 30
	print parsed['time']
	print 'nr\trank\tscore\tpower_score\ttags'

	globalscore = [ a for a in parsed['data']['rankings'] if 'Wagner' in a['team'] ][0]
	print '-\t%s\t%s\t%s' % (globalscore['rank'],globalscore['score'],globalscore['power_score'])


	for i, a in enumerate(parsed['data']['settings']):
		localscore = [ b for b in a['rankings'] if 'Wagner' in b['team'] ][0]
		print '%s\t%s\t%s\t%s\t%s' % (i, localscore['rank'], localscore['score'], localscore['power_score'], localscore['tags'])

	time.sleep(300)