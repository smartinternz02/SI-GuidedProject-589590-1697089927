from flask import Flask, render_template, request
import pickle
import joblib
app = Flask(__name__)
model = pickle. load(open(r"C:/Users/katta/Desktop/srujana.flask/srujana/Flask/crab1.pkl", "rb"))
#model = pickle.load(open("crab.pkl","rb"))
#ct = joblib. load('col.pkl')
@app.route('/')
@app.route('/home',methods= ["GET", "POST"])
def homepage():
            return render_template("home.html")

@app.route('/predict', methods = ["GET", "POST"])
def predict():
            return render_template("predict.html")

@app.route('/submit',methods = ["GET", "POST"])
def submit():
    if request.method=="POST":        
            sw = (request.form["sw"])
            l = (request.form["l"])
            d = (request.form["d"])
            h = (request.form["h"])
            w = (request.form["w"])
            ww=(request.form["ww"])
            vw = (request.form["vw"])
            Sex = (request.form["Sex"])
            if Sex == "M":
                    Sex = 2
            elif Sex == "F":
                  Sex = 0
            elif Sex == "0":
                  Sex = 1
            data = [[float(sw), float(l),float( d), float( h), float(w),float(ww), float(vw), float(Sex)]]
            print(data)
            output = model.predict(data)
            print(output)
            return render_template("submit.html", output = output)

if __name__=='__main__':
    app.run(debug = False)
