import requests
import json

url = "https://codeforces.com/api/user.ratedList?activeOnly=false&includeRetired=false"

response = requests.get(url)

data = response.json()['result']

file = open("all_user.json","w")

json.dump(data,file)

print("User Data Written :)")