import os
import pandas as pd
from sklearn import model_selection,svm
from sklearn.ensemble import RandomForestClassifier as rfc
from sklearn.model_selection import train_test_split as tsp
from flask import Flask, request,render_template,url_for,redirect
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
import numpy as n

df1=pd.read_csv('dataset1.txt')
y1=df1.classification
x1=df1.drop('classification',axis=1)
x_tr1,x_ts1,y_tr1,y_ts1=tsp(x1,y1,test_size=0.3)

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
    a0=float(request.form['0'])
    a1=float(request.form['1'])
    a2 =float(request.form['2'])
    a3 =float(request.form['3'])
    a4 =float(request.form['4'])
    a5=float(request.form['5'])
    a6=float(request.form['6'])
    a7 =float(request.form['7'])
    a8 =float(request.form['8'])
    a9 =float(request.form['9'])
    a10=float(request.form['10'])
    a11=float(request.form['11'])
    a12 =float(request.form['12'])
    a13 =float(request.form['13'])
    a14 =float(request.form['14'])
    a15=float(request.form['15'])
    a16=float(request.form['16'])
    a17 =float(request.form['17'])
    a18 =float(request.form['18'])
    a19 =float(request.form['19'])
    a20=float(request.form['20'])
    a21 = float(request.form['21'])
    a22 =float(request.form['22'])
    a23 =float(request.form['23'])

    algorithm1 = "Naive Bayes"
    l1=[[a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23]]
    classifier1 = GaussianNB()  
    classifier1.fit(x_tr1, y_tr1)  
    predict_test1 = classifier1.predict(x_ts1)
    final_features1 = (n.array(l1))
    prediction1 = classifier1.predict(final_features1)
    accuracy1 = round((metrics.accuracy_score(y_ts1, predict_test1)),3)

    algorithm2 ="SVM"
    l2 = [[a2,a3,a4,a5,a6,a7,a8,a11,a13,a17,a18,a19,a20,a21,a22,a23]]
    classifier2 = svm.SVC()
    classifier2.fit(x_tr2, y_tr2)  
    predict_test2 = classifier2.predict(x_ts2)
    final_features2 = (n.array(l2))
    prediction2 = classifier2.predict(final_features2)
    accuracy2 = round((metrics.accuracy_score(y_ts2, predict_test2)),3)

    algorithm3 ="Random Forest"
    l3 = [[a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23]]
    classifier3 = rfc(n_estimators=8,max_depth=4,n_jobs=-1)
    classifier3.fit(x_tr1, y_tr1)
    predict_test3 = classifier3.predict(x_ts1)
    final_features3 = (n.array(l3))
    prediction3 = classifier3.predict(final_features3)
    accuracy3 = round((metrics.accuracy_score(y_ts1, predict_test3)),3)

    if((accuracy1 > accuracy2) and (accuracy1 > accuracy3)):
        accuracy = accuracy1
        algorithm=algorithm1
        if(prediction1 == 1):
            prediction="CKD"
        else:
            prediction="Not CKD"

    elif ((accuracy2 > accuracy1) and (accuracy2 > accuracy3)):
        accuracy = accuracy2
        algorithm = algorithm2
        if(prediction2 == 1):
            prediction="CKD"
        else:
            prediction="Not CKD"
    else:
        accuracy = accuracy3
        if prediction3==1:
            prediction = "CKD"
        else:
            prediction = "Not CKD"
    
    return render_template('homepage2.html',prediction_text=prediction)

if __name__ == "__main__":
    app.run(debug=True)
