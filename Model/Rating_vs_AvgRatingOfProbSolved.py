import json
import matplotlib.pyplot as plt

with open('data.json', 'r') as file:
    data = json.load(file)

ratings = []
solve = []

def func(d):
    k = 0
    k1 = 0
    for i in d:
        k += d[i]*int(i)
        k1 += d[i]
    try:
        return k/k1
    except:
        return 0

for user in data:
    if user['SolvedCount']<100 or user['SolvedCount']>7000:
        continue
    ratings.append(user['rating'])
    solve.append(func(user['RatingDistribution']))

plt.figure(figsize=(10, 6))
plt.scatter(ratings, solve, color='blue', alpha=0.6, edgecolor='black')

plt.title("Codeforces Rating vs Average Rating of Problem", fontsize=16)
plt.xlabel("maxRating", fontsize=14)
plt.ylabel("Average Rating of Problem", fontsize=14)

plt.legend()

plt.grid(linestyle='--', alpha=0.7)
# plt.savefig("rating_vs_maxrating.png", dpi=300, bbox_inches='tight')

plt.show()


print(data[0].keys())