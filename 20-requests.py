import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
#just print the response
#print(response.json())
#json format the response
#print(json.dumps(response.json(),indent=2))
output = response.json()
for result in output["results"]:
     print(result["trackName"])