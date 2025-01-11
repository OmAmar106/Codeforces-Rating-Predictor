import json
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

rating_list = ['1200', '1300', '1400', '1500',    '1600', '1700', '1800', '1900', '2000' , '2100', '2200', '2300', '2400', '2500', '2600', '2700', '2800', '2900', '3000']
with open('data.json', 'r') as file:
    data = json.load(file)

ratings = []
solve = []

def func(user):
    X = []
    sum = 0
    for i in rating_list[:4]:
        if i in user['RatingDistribution']:
            sum += user['RatingDistribution'][i]
    X.append(sum)
    sum = 0
    for i in rating_list[4:7]:
        if i in user['RatingDistribution']:
            sum += user['RatingDistribution'][i]
    X.append(sum)
    sum = 0
    for i in rating_list[7:9]:
        if i in user['RatingDistribution']:
            sum += user['RatingDistribution'][i]
    X.append(sum)
    sum = 0
    for i in rating_list[9:11]:
        if i in user['RatingDistribution']:
            sum += user['RatingDistribution'][i]
    X.append(sum)
    sum = 0
    for i in rating_list[11:13]:
        if i in user['RatingDistribution']:
            sum += user['RatingDistribution'][i]
    X.append(sum)
    sum = 0
    for i in rating_list[13:15]:
        if i in user['RatingDistribution']:
            sum += user['RatingDistribution'][i]
    X.append(sum)
    sum = 0
    for i in rating_list[15:17]:
        if i in user['RatingDistribution']:
            sum += user['RatingDistribution'][i]
    X.append(sum)
    sum = 0
    for i in rating_list[17:19]:
        if i in user['RatingDistribution']:
            sum += user['RatingDistribution'][i]
    X.append(sum)
    sum = 0
    return X
    

for user in data:
    if user['SolvedCount']<100:
        continue
    ratings.append(user['rating'])
    solve.append(func(user))

x = np.array(solve)

y = np.array(ratings)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=41)

model = LinearRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

mse = mean_squared_error(y_test, y_pred)

print(f"Mean Squared Error: {mse}")

plt.scatter(y_pred, y_test, color='blue', label='Predicted')
plt.plot([0, 1, 3000], [0, 1, 3000], color='red', label='Actual')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

joblib.dump(model, 'regression_model.pkl')

