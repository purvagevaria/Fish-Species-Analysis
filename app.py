from flask import Flask, request, render_template
import joblib
import os

app = Flask(__name__)

# Load the model
model_path = os.path.join(os.path.dirname(__file__), 'models', 'fish_weight_model.pkl')
model = joblib.load(model_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            length1 = float(request.form['length1'])
            length2 = float(request.form['length2'])
            length3 = float(request.form['length3'])
            height = float(request.form['height'])
            width = float(request.form['width'])

            features = [[length1, length2, length3, height, width]]
            prediction = model.predict(features)
            result = f"Predicted Weight: {prediction[0]:.2f} g"
        except ValueError as e:
            result = "Invalid input. Please enter numeric values."

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
