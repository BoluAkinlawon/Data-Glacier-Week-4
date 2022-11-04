from flask import Flask, request, jsonify
import pickle
import json
import numpy as np

app = Flask(__name__)
model = pickle.load(open('random_forest_model.pkl', 'rb'))

@app.route('/')
def home():
    return 'Welcome to Mobile Phone price API'

@app.route("/predict", methods = ["GET"])
def predict():
    battery_power = request.args.get("battery_power")
    blue = request.args.get("blue")
    clock_speed = request.args.get("clock_speed")
    dual_sim = request.args.get("dual_sim")
    fc = request.args.get("fc")
    four_g = request.args.get("four_g")
    int_memory = request.args.get("int_memory")
    m_dep = request.args.get("m_dep")
    mobile_wt = request.args.get("mobile_wt")
    n_cores = request.args.get("n_cores")
    pc = request.args.get("pc")
    px_height = request.args.get("px_height")
    px_width = request.args.get("px_width")
    ram = request.args.get("ram")
    sc_h = request.args.get("sc_h")
    sc_w = request.args.get("sc_w")
    talk_time = request.args.get("talk_time")
    three_g = request.args.get("three_g")
    touch_screen = request.args.get("touch_screen")
    wifi = request.args.get("wifi")


    makeprediction = model.predict([[battery_power, blue, clock_speed, dual_sim, fc, four_g, int_memory, m_dep, mobile_wt, n_cores, pc, px_height, px_width, ram, sc_h, sc_w, talk_time, three_g, touch_screen, wifi]])
    output = round(makeprediction[0],0)
    return jsonify({'Price Range is':output})
    
    
if __name__ =="__main__":
    app.run(debug=True)
