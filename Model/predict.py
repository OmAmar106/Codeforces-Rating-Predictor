import numpy as np
import requests
from collections import Counter

coefficients = [1.23343836e+00, -1.18708102e-06, 1.02432872e-01]
intercept = 1897.8176387573285

def func(handle):
    # handle = input("Enter Username : ")

    def func(d):
        k = 0
        k1 = 0
        for i in d:
            k += d[i]*int(i)
            k1 += d[i]
        try:
            return (k/k1,k1)
        except:
            return 0
        
    url = "https://codeforces.com/api/user.status?handle="+handle+"&from=1&count=25000"
    response = requests.get(url)
    data1 = response.json()
    if data1['status'] == 'OK':
        data1 = data1['result']
        set1 = set()
        count2 = Counter()
        for i in data1:
            if i['verdict'] == 'OK' and i['id'] not in set1:
                set1.add(i['id'])
                if 'rating' in i['problem']:
                    count2[i['problem']['rating']] += 1
    else:
        return (False, 0)

    url = "https://codeforces.com/api/user.info?handles="+handle
    response = requests.get(url)
    data = response.json()

    if data['status'] == 'OK':
        try:
            data = response.json()['result'][0]
            L = func(count2)

            x_test = np.array([[L[0], data['registrationTimeSeconds'], L[1]]])
            prediction = np.dot(x_test, coefficients) + intercept

            return (True, [prediction[0], data])
        except Exception as e:
            return (False, f"Error: {str(e)}")
    else:
        return (False, 'Server Down')