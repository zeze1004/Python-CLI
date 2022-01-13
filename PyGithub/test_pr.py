import requests

import json
from pprint import pprint


#Get only closed PR
# URL = 'https://api.github.com/repos/zeze1004/AWS_K8s/pulls?&state=closed'
# headers = {'Authorization': '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'} #Obtained access token
# r = requests.get(URL.format("AWS_K8s"), headers=headers)
# pprint(r.json())

#Create PR
URL = 'https://api.github.com/repos/zeze1004/AWS_K8s/pulls?&state=closed'

curl -H "Authorization: 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" https://api.github.com