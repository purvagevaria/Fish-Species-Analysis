# Fish Species Analysis

## Overview

This project involves building and deploying a machine learning model to predict fish species based on physical measurements. The model is trained using the Fish Market dataset, and the application is deployed on Render.

## Project Structure

- `app.py`: Main Flask application file.
- `Dockerfile`: Docker configuration for containerizing the application.
- `requirements.txt`: List of Python dependencies.
- `models/`: Directory containing the saved model file.
- `templates/`: Directory containing HTML templates for the web UI.
- `notebooks/`: Jupyter notebook for training the model (if applicable).

## Deployment
Build Command: pip install -r requirements.txt
Start Command: python app.py
Port: Ensure it's set to 5000.

## Accessing the Application
Render URL: https://fish-species-analysis.onrender.com/

## Troubleshooting
TemplateNotFound Error: Ensure that index.html is in the templates/ directory and correctly named.
Port Binding Issues: Make sure your Flask app is configured to run on 0.0.0.0 and port 5000.
