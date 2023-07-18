from flask import Flask,render_template,request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))
print(model.predict(np.array([23]).reshape(-1,1)))
print(model.predict([[40]]))



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods = ['GET','POST'])
def predict():
    try :
        int_features = [float(x) for x in request.form.values()]
        features =[np.array(int_features)]
        prediction = model.predict(features)
        output = round(prediction[0], 2)
        print(output)
        return render_template('index.html', prediction =f'Estimated delivery time is {output} minutes')
    except:
        return render_template('index.html', prediction ='Try to input numbers')

if (__name__)=='__main__' :
    app.run(debug=True)
