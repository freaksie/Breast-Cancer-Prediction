import pickle
from flask import Flask, request, jsonify
from flask_cors import CORS
import sklearn 
import numpy as np

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)
CORS(app)
@app.route('/', methods=["POST"])
def breast_pred():
    
    content = request.get_json()
    array=[]
    array.append(float(content['radius']))
    array.append(float(content['texture']))
    array.append(float(content['peri']))
    array.append(float(content['area']))
    array.append(float(content['smooth']))
    np_array = np.array(array)[np.newaxis]


    ans_ar = model.predict_proba(np_array)
    ans = ans_ar[0][1]*100
    #ans=0
    ans = jsonify(ans)
    

    return ans


if __name__ == '__main__':
    app.run(debug=True)