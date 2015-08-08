import httplib
import json
import time

while True:
	c = httplib.HTTPSConnection('davar.icfpcontest.org')
	c.request('GET','/rankings.js')
	r = c.getresponse()
	d = r.read()
	c.close()
	#print type(d)
	#print d

	capped = d[11:]
	parsed = json.loads(capped)

	#print parsed

	print 'time of site:', parsed['time']

	print 'main ranking:'

	print [ a for a in parsed['data']['rankings'] if 'Wagner' in a['team'] ][0]

	for i, a in enumerate(parsed['data']['settings']):
		print i, [ b for b in a['rankings'] if 'Wagner' in b['team'] ][0]

	time.sleep(300)

	print '\n\n\n\n'