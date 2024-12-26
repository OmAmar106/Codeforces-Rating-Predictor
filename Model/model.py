import json
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib


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

def func2(d):
    k = 0
    k1 = 0
    for i in d:
        k += d[i]*int(i)
        k1 += d[i]
    return k1

for user in data:
    if user['SolvedCount']<100:
        continue
    ratings.append(user['rating'])
    solve.append([func(user['RatingDistribution']),user['registrationTimeSeconds'],func2(user['RatingDistribution'])])

x = np.array(solve)

y = np.array(ratings)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=41)

model = LinearRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

mse = mean_squared_error(y_test, y_pred)

print(f"Mean Squared Error: {mse}")

plt.scatter(y_pred, y_test, color='blue', label='Actual')
# plt.plot(y_test, y_pred, color='red', label='Predicted')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

joblib.dump(model, 'regression_model.pkl')

