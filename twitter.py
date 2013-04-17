import json
import collections
import re
from urllib.request import urlopen
from urllib.parse import urlencode
from pprint import pprint

rpp = 100
max_results = 1500
text = ''

for i in range(int(max_results/rpp)):
    params = urlencode({'q': 'УрФУ', 'rpp': rpp, 'lang': 'ru', 'page': i+1, 'result_type': 'mixed'})
    data = urlopen('http://search.twitter.com/search.json?' + params).read()
    from_json_data = json.loads(data.decode('utf8'))
    for r in from_json_data['results']:
        text += ' ' + r['text']
pprint(collections.Counter([x for x in re.findall('\w+', text.lower()) if len(x)>2 and not re.match('урфу.*', x)]).most_common(20))

