import random
import json

with open("all_user.json", "r") as file:
    user_data = json.load(file)

all_users = [{'handle':user['handle'],'maxRating':user['maxRating'],'rating':user['rating'],'registrationTimeSeconds':user['registrationTimeSeconds']} for user in user_data if (user['rating']>=800 and (user['maxRating']-user['rating']<=300))]
sample_users = random.sample(all_users,4000)

for j in all_users:
    if j['maxRating']>=2400:
        sample_users.append(j)

with open("sample_users.json", "w") as file:
    json.dump(sample_users, file)

print(len(sample_users))

print("Part 2 Done :)")
