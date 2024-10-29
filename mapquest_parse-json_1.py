import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Rizal, Philippines"
dest = "Makati, Philippines"
key = "arhaArR8A7wX8lxvSKao4iF2rZm5STjM" #Replace with your MapQuest key

url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

json_data = requests.get(url).json()
print(json_data)
