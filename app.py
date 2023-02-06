from flask import Flask, redirect, url_for, flash, request, jsonify
import pickle


# Para instanciar Flask
app = Flask(__name__)

# Para no tener que reiniciar si hay errores
app.config['DEBUG'] = True


@app.route('/', methods=['GET'])
def index():

    return 'Mi primera web cutre'


@app.route('/v2', methods=['GET'])
def otra():
    return 'otra pag'

# @app.route('/api/v1/predict', methods=['GET'])
# def predict():
# 
#     model = pickle.load(open('ad_model.pkl','rb'))
#     tv = float(request.args.get('tv', None))
#     radio = float(request.args.get('radio', None))
#     newspaper = float(request.args.get('newspaper', None))
# 
#     if tv is None or radio is None or newspaper is None:
#         return "Args empty, the data are not enough to predict"
#     else:
#         prediction = model.predict([[tv,radio,newspaper]])
# 
#     return jsonify({'predictions': prediction[0]})
# 
# app.run()
