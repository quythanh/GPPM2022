from flask import render_template, request
from mysite import app
from mysite.readDB import getUser

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/profile', methods=["GET", "POST"])
def profile():
    user = getUser(str(1))
    return render_template('profile.html', user=user)

@app.route('/health-care', methods=["GET", "POST"])
def healthCare():
    if request.method == "POST":
        symptoms = [0, 0, 0, 0, 0, 0, 0]
        dsymptoms = [0, 0, 0, 0]
        for i in request.form.getlist('symptom'):
            symptoms[int(i) - 1] = 1
        for i in request.form.getlist('dsymptom'):
            dsymptoms[int(i) - 1] = 1

    return render_template('healthCare.html')

@app.route('/chart', methods=["GET"])
def graph():
    return render_template('chart.html')

@app.route('/get/user/<string:id>', methods=["GET"])
def api_user(id):
    data = getUser(id)
    return data