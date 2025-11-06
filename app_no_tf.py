import os
import sys
import random

# Flask
from flask import Flask, request, render_template, Response, jsonify

# Some utilites
import numpy as np
from util import base64_to_pil

# Declare a flask app
app = Flask(__name__)

# Create uploads directory if it doesn't exist
os.makedirs('uploads', exist_ok=True)

print('Mock model loaded. Start serving...')

def mock_model_predict(img):
    """
    Mock prediction function for testing without TensorFlow
    Returns random prediction for demonstration
    """
    # Simulate model prediction with random result
    result = random.random()
    return [[result]]

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get the image from post request
            img = base64_to_pil(request.json)
            
            # Save image
            img.save("uploads/image.jpg")
            
            img_path = os.path.join(os.path.dirname(__file__),'uploads/image.jpg')
            
            if not os.path.isfile(img_path):
                return jsonify(error="Failed to save image"), 400
            
            # Resize image to simulate preprocessing
            img = img.resize((64, 64))
            
            # Mock prediction
            preds = mock_model_predict(img)
            result = preds[0][0]
            
            print(f"Mock prediction result: {result}")
            
            if result > 0.5:
                return jsonify(result="PNEUMONIA", confidence=f"{result:.2f}")
            else:
                return jsonify(result="NORMAL", confidence=f"{1-result:.2f}")
                
        except Exception as e:
            print(f"Error during prediction: {str(e)}")
            return jsonify(error=str(e)), 500

    return None

if __name__ == '__main__':
    print("Running in MOCK MODE - predictions are random!")
    print("This is for testing the web interface without TensorFlow")
    app.run(debug=True, host='0.0.0.0', port=5000)