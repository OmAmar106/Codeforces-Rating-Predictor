from flask import Flask, redirect, render_template, request, jsonify,url_for,session
from flask_caching import Cache
from Model.predict import func

app = Flask(__name__)
app.config['CACHE_TYPE'] = 'simple'
cache = Cache(app)
app.app_context().push()
app.secret_key = "APtlnuRu04uv"

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='GET':
        return render_template('index.html')
    elem = request.form.get('profile_name')
    tup = (func(elem))
    if not tup[0]:
        return render_template('index.html',flag=True)

    d = {
        "Newbie": "#A9A9A9",  # Gray
        "Pupil": "#32CD32",  # Deep Sky Blue
        "Specialist": "#00ffcc",  # Lime Green
        "Expert": "#1E90FF",  # Dodger Blue
        "Candidate Master": "#800080",  # Purple
        "Master": "#FFD700",  # Gold
        "International Master": "#DAA520",  # Goldenrod
        "Grandmaster": "#DAA520",  # Medium Violet Red
        "International Grandmaster": "#DC143C",  # Crimson
        "Legendary Grandmaster": "#FF0000",  # Red
        "Tourist": "#FFFFFF"
    }
    try:
        tup[1][1]['rank_color'] = d[(tup[1][1]['rank']).title()]
    except:
        tup[1][1]['rank_color'] = '#A9A9A9'
    try:
        if tup[1][0]>tup[1][1]['rating']:
            msg = "Hopefully, you wil reach your expected rating soon :)"
        else:
            msg = "You are above your Expected Rating, Bravo!!!"
    except:
        msg = "Hopefully, you wil reach your expected rating soon :)"
    if 'rating' not in tup[1][1]:
        tup[1][1]['rating'] = 0
    return render_template('result.html',user_data=tup[1][1],prediction=tup[1][0],msg=msg)

@app.template_filter('abs')
def abs(value):
    return abs(value)

@app.route('/get/<string:s>',methods=['GET'])
def get(s):
    elem = s
    tup = (func(elem))
    if not tup[0]:
        return jsonify({'':''}),404

    d = {
        "Newbie": "#A9A9A9",  # Gray
        "Pupil": "#32CD32",  # Deep Sky Blue
        "Specialist": "#00ffcc",  # Lime Green
        "Expert": "#1E90FF",  # Dodger Blue
        "Candidate Master": "#800080",  # Purple
        "Master": "#FFD700",  # Gold
        "International Master": "#DAA520",  # Goldenrod
        "Grandmaster": "#DAA520",  # Medium Violet Red
        "International Grandmaster": "#DC143C",  # Crimson
        "Legendary Grandmaster": "#FF0000",  # Red
        "Tourist": "#FFFFFF"
    }
    try:
        tup[1][1]['rank_color'] = d[(tup[1][1]['rank']).title()]
    except:
        tup[1][1]['rank_color'] = '#A9A9A9'
    try:
        if tup[1][0]>tup[1][1]['rating']:
            msg = "Hopefully, you wil reach your expected rating soon :)"
        else:
            msg = "You are above your Expected Rating, Bravo!!!"
    except:
        msg = "Hopefully, you wil reach your expected rating soon :)"
    if 'rating' not in tup[1][1]:
        tup[1][1]['rating'] = 0
    return jsonify({'user_data':tup[1][1],'prediction':tup[1][0]}),200

if __name__ == '__main__':
    app.run(debug=True)
