import pickle
from flask import Flask, request, jsonify
from flask_cors import CORS
import sklearn 
import numpy as np

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)
CORS(app)
@app.route('/home', methods=["POST"])
def breast_pred():
    
    content = request.get_json()
    array=[]
    array.append(int(content['radius']))
    array.append(int(content['texture']))
    array.append(int(content['peri']))
    array.append(int(content['area']))
    array.append(int(content['smooth']))
    np_array = np.array(array)

    
    ans_ar = model.predict_proba(np_array)
    ans = ans_ar[0][0]*100
    ans = jsonify(ans)
    

    return ans


if __name__ == '__main__':
    app.run(debug=True)