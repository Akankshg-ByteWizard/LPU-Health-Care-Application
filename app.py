from flask import Flask, render_template, url_for, flash, redirect
import joblib
from flask import request
import numpy as np

app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/cancer")
def cancer():
    return render_template('cancer.html')

def ValuePredictor1(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==5):
        loaded_model = joblib.load(r"cancer_model.pkl")
        result = loaded_model.predict(to_predict)
    return result[0]

@app.route("/diabetes")
def diabetes():
    return render_template("diabetes.html")

def ValuePredictor2(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==6):
        loaded_model = joblib.load(r'diabetes_model.pkl')
        result = loaded_model.predict(to_predict)
    return result[0]

@app.route("/heart")
def heart():
    return render_template("heart.html")

def ValuePredictor3(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==7):
        loaded_model = joblib.load(r'heart_model.pkl')
        result = loaded_model.predict(to_predict)
    return result[0]

@app.route("/kidney")
def kidney():
    return render_template("kidney.html")

def ValuePredictor3(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==7):
        loaded_model = joblib.load(r'kidney_model.pkl')
        result = loaded_model.predict(to_predict)
    return result[0]

@app.route("/liver")
def liver():
    return render_template("liver.html")

def ValuePredictor3(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==7):
        loaded_model = joblib.load(r'liver_model.pkl')
        result = loaded_model.predict(to_predict)
    return result[0]

@app.route('/predict', methods = ["POST"])
def predict():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
         #diabetes
        if(len(to_predict_list)==5):
            result = ValuePredictor1(to_predict_list,5)
        elif(len(to_predict_list)==6):
            result = ValuePredictor2(to_predict_list,6)
        elif(len(to_predict_list)==7):
            result = ValuePredictor3(to_predict_list,7)
    if(int(result)==1):
        prediction = "Sorry you are likely to have the disease. Please consult the doctor immediately"
    else:
        prediction = "You are absoultrly fine. You have no symptoms of the  disease"
    return(render_template("result.html", prediction_text=prediction))      

@app.route("/BreastAnalysis")
def BreastAnalysis():
    return render_template('WPbreastcancer.html')

@app.route("/DiabetesAnalysis")
def DiabetesAnalysis():
    return render_template('WPdiabetes.html')

@app.route("/HeartAnalysis")
def HeartAnalysis():
    return render_template('WPheartdisease.html')

@app.route("/LiverAnalysis")
def LiverAnalysis():
    return render_template('WPliverdisease.html')

@app.route("/KidneyAnalysis")
def KidneyAnalysis():
    return render_template('WPchronickidney.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
