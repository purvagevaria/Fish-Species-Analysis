from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)

# Load the model
model_path = os.path.join('models', 'fish_weight_model.pkl')
model = joblib.load(model_path)

@app.route('/')
def index():
    return "Welcome to the Fish Species Analysis API!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    features = [data['features']]
    prediction = model.predict(features)
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))