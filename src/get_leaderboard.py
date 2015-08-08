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

	print 'time of site:', parsed['time']

	globalscore = [ a for a in parsed['data']['rankings'] if 'Wagner' in a['team'] ][0]
	del globalscore['teamId']
	del globalscore['team']
	del globalscore['tags']
	print 'main ranking:', globalscore

	for i, a in enumerate(parsed['data']['settings']):
		localscore = [ b for b in a['rankings'] if 'Wagner' in b['team'] ][0]
		del localscore['teamId']
		del localscore['team']
		print i, localscore

	time.sleep(300)

	print '\n\n\n\n'