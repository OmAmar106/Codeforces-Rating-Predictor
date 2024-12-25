import matplotlib.pyplot as plt
import json

with open("sample_users.json", "r") as file:
    user_data = json.load(file)

ratings = [(user['rating']) for user in user_data]

plt.figure(figsize=(10, 6))
plt.hist(ratings, bins=20, color='skyblue', edgecolor='black', alpha=0.7)

plt.title("Distribution of Codeforces Ratings", fontsize=16)
plt.xlabel("Rating", fontsize=14)
plt.ylabel("Number of Users", fontsize=14)

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig("sample_rating_distribution.png", dpi=300, bbox_inches='tight')

plt.show()
