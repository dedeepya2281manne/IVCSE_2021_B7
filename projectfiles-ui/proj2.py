import os
import pandas as pd
from sklearn import model_selection,svm
from sklearn.model_selection import train_test_split as tsp
from flask import Flask, request,render_template,url_for,redirect
from sklearn import metrics
import numpy as n

df2=pd.read_csv('dataset2.txt')
y2=df2.classification
x2=df2.drop('classification',axis=1)
x_tr2,x_ts2,y_tr2,y_ts2=tsp(x2,y2,test_size=0.3)

app = Flask(__name__)
@app.route("/",methods=["POST","GET"])
def home():
    return render_template('homepage2.html')

@app.route('/predictckd',methods=['POST'])
def predictckd():
    a2 =float(request.form['2'])
    a3 =float(request.form['3'])
    a4 =float(request.form['4'])
    a5=float(request.form['5'])
    a6=float(request.form['6'])
    a7 =float(request.form['7'])
    a8 =float(request.form['8'])
    a11=float(request.form['11'])
    a13 =float(request.form['13'])
    a17 =float(request.form['17'])
    a18 =float(request.form['18'])
    a19 =float(request.form['19'])
    a20=float(request.form['20'])
    a21 = float(request.form['21'])
    a22 =float(request.form['22'])
    a23 =float(request.form['23'])

    algorithm2 ="SVM"
    l2 = [[a2,a3,a4,a5,a6,a7,a8,a11,a13,a17,a18,a19,a20,a21,a22,a23]]
    classifier2 = svm.SVC()
    classifier2.fit(x_tr2, y_tr2)  
    predict_test2 = classifier2.predict(x_ts2)
    final_features2 = (n.array(l2))
    prediction2 = classifier2.predict(final_features2)
    accuracy2 = round((metrics.accuracy_score(y_ts2, predict_test2)),3)
    if(prediction2 == 1):
        prediction="CKD"
    else:
        prediction="Not CKD"

    
    return render_template('homepage2.html',prediction_text=prediction)

if __name__ == "__main__":
    app.run(debug=True)
