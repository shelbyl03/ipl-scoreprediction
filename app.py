#crating server

from flask import Flask, render_template, request
import pickle 
import numpy as np

#1 creating object
app=Flask(__name__)

#6 loding the model
with open("ipl.pkl","rb")as f:
    model=pickle.load(f)

#7  for prediction

def predict_score(batting_team = 'Chennai Super kings',bowling_team = 'Mumbai Indians',overs=5.1, runs=50, wickets=0,runs_in_prev_5=50,wickets_in_prev_5=50):
    temp_array=list()
    if batting_team=='Chennai Super kings':
        temp_array= temp_array+[1,0,0,0,0,0,0,0]
    elif batting_team=='Delhi Daredevils':
        temp_array= temp_array+[0,1,0,0,0,0,0,0]
    elif batting_team=='Kings XI Punjab':
        temp_array= temp_array+[0,0,1,0,0,0,0,0]
    elif batting_team=='Kolkata Knight Riders':
        temp_array= temp_array+[0,0,0,1,0,0,0,0]
    elif batting_team=='Mumbai Indians':
        temp_array= temp_array+[0,0,0,0,1,0,0,0]
    elif batting_team=='Rajastan Royals':
        temp_array= temp_array+[0,0,0,0,0,1,0,0]
    elif batting_team=='Royal Challengers Bangalore':
        temp_array= temp_array+[0,0,0,0,0,0,1,0]
    elif batting_team=='Sunrisers Hydrabad':
        temp_array= temp_array+[0,0,0,0,0,0,0,1]
    
#bowling team
    if bowling_team=='Chennai Super kings':
        temp_array= temp_array+[1,0,0,0,0,0,0,0]
    elif bowling_team=='Delhi Daredevils':
        temp_array= temp_array+[0,1,0,0,0,0,0,0]
    elif bowling_team=='Kings XI Punjab':
        temp_array= temp_array+[0,0,1,0,0,0,0,0]
    elif bowling_team=='Kolkata Knight Riders':
        temp_array= temp_array+[0,0,0,1,0,0,0,0]
    elif bowling_team=='Mumbai Indians':
        temp_array= temp_array+[0,0,0,0,1,0,0,0]
    elif bowling_team=='Rajastan Royals':
        temp_array= temp_array+[0,0,0,0,0,1,0,0]
    elif bowling_team=='Royal Challengers Bangalore':
        temp_array= temp_array+[0,0,0,0,0,0,1,0]
    elif bowling_team=='Sunrisers Hydrabad':
        temp_array= temp_array+[0,0,0,0,0,0,0,1]

    
#overs,runs,wickets,runs_in_prev_5,wickets_in_prev_5

    temp_array=temp_array+[overs,runs,wickets,runs_in_prev_5,wickets_in_prev_5]
# converting into numpy arrays

    temp_array=np.array([temp_array])
    print(temp_array)

#prediction
    return int(model.predict(temp_array))


#3routing 
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

#4predict for post method

@app.route("/predict",methods=['GET','POST'])
def predict():


    # 5 for taking front end data
    if request.method=='POST':
        batting_team=request.form.get('batting_team')
        bowling_team=request.form.get('bowling_team')
        overs=float(request.form.get('overs'))
        runs=int(request.form.get('runs'))
        wickets=int(request.form.get('wickets'))
        runs_in_prev_5=int(request.form.get('runs_in_prev_5'))
        wickets_in_prev_5=int(request.form.get('wickets_in_prev_5'))
        print(bowling_team)
        print(type(runs))
        score=predict_score(batting_team=batting_team,bowling_team=bowling_team,overs=overs,runs=runs,wickets=wickets,runs_in_prev_5=runs_in_prev_5,wickets_in_prev_5=wickets_in_prev_5)
        print(score)
        return render_template('result.html',
                               Prediction=score)
    return render_template('predict.html')
    

if __name__=='__main__':
# 2running server
    app.run(debug=True)
