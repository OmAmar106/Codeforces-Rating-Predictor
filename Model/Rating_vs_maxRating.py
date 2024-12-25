import matplotlib.pyplot as plt
import json

with open("sample_users.json", "r") as file:
    user_data = json.load(file)

ratings = []
max_ratings = []
for user in user_data:
    ratings.append(user['rating'])
    max_ratings.append(user['maxRating'])

plt.figure(figsize=(10, 6))
plt.scatter(ratings, max_ratings, color='blue', alpha=0.6, edgecolor='black')

plt.title("Codeforces Rating vs Max Rating", fontsize=16)
plt.xlabel("Current Rating", fontsize=14)
plt.ylabel("Max Rating", fontsize=14)

plt.legend()

plt.grid(linestyle='--', alpha=0.7)
plt.savefig("rating_vs_maxrating.png", dpi=300, bbox_inches='tight')

plt.show()
