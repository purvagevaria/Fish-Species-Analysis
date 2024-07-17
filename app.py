from flask import Flask, request, render_template, redirect, url_for
import joblib
import numpy as np

app = Flask(__name__)

# Load the model
model_path = 'models/fish_weight_model.pkl'
model = joblib.load(model_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    length1 = float(request.form['length1'])
    length2 = float(request.form['length2'])
    length3 = float(request.form['length3'])
    height = float(request.form['height'])
    width = float(request.form['width'])

    # Make prediction
    input_features = np.array([[length1, length2, length3, height, width]])
    prediction = model.predict(input_features)[0]

    return render_template('index.html', result=f'Predicted Species: {prediction}')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Ensure Flask binds to 0.0.0.0
