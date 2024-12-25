import json
import time
import requests
from collections import Counter

with open('sample_users.json', 'r') as file:
    data = json.load(file)

count = 0

findata = []
failed = 0
for user in data:
    try:
        start_time = time.time()
        set1 = set()
        url = "https://codeforces.com/api/user.status?handle="+user['handle']+"&from=1&count=25000"

        response = requests.get(url)
        # print(response)
        # exit()
        
        data = response.json()
        count2 = Counter()
        if data['status']=='OK':
            data = data['result']
            for i in data:
                if i['verdict']=='OK' and i['id'] not in set1:
                    set1.add(i['id'])
                    if 'rating' in i['problem']:
                        count2[i['problem']['rating']] += 1
        else:
            raise Exception(":/")
        count += 1
        user1 = user
        user1['SolvedCount'] = len(set1)
        user1['RatingDistribution'] = count2
        findata.append(user1)
        
        with open('data.json', 'w') as file:
            json.dump(findata, file, indent=4)

        print(f"Users Fetched: {count} , Users Failed: {failed}", end="\r")

        while time.time()-start_time<=2:
            pass
    except:
        failed += 1

print(failed)


print("Data written to data.json")
print(":)")