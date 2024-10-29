import sys
import requests

if len(sys.argv) != 3:
    sys.exit("Please only give 2 arguments")

elif len(sys.argv) == 3:
    response = requests.get(f"https://itunes.apple.com/search?entity=song&limit={sys.argv[2]}&term={sys.argv[1]}")
    o = response.json()
    for result in o['results']:
        print(result['trackName'])