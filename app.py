import flask
from flask import Flask, request, jsonify
import pickle
import json
import numpy as np


app = Flask(__name__)
model = pickle.load(open('random_forest_model.pkl','rb'))

@app.route('/')

def home():
    return render_template('Templates/index.html')

@app.route('/predict', methods =['POST'])
def predict():
    """

    For rendering results on HTML GUI
    -------
    None.

    """
    
    int_features =[int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    
    output = round(prediction[0], 2)
    
    return render_template('Templates/index.html', prediction_text = 'Price range should be'.format(output))


if __name__ =="__main__":
    app.run(debug = True)
