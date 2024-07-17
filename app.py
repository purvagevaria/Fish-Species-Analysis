from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the model and scaler
model = joblib.load('models/fish_weight_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    species = request.form['species']
    length1 = float(request.form['length1'])
    length2 = float(request.form['length2'])
    length3 = float(request.form['length3'])
    height = float(request.form['height'])
    width = float(request.form['width'])

    # Create input array
    input_data = [length1, length2, length3, height, width]
    input_data += [1 if species == s else 0 for s in ['Bream', 'Roach', 'Whitefish', 'Parkki', 'Smelt']]

    # Scale the input data
    input_data = scaler.transform([input_data])

    # Predict the weight
    prediction = model.predict(input_data)

    return f'The predicted weight of the fish is {prediction[0]:.2f} grams'

if __name__ == '__main__':
    app.run(debug=True)
