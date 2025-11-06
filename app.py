import os
import sys

# Flask
from flask import Flask, request, render_template, Response, jsonify
#from werkzeug.utils import secure_filename

# Optional gevent import for production
try:
    from gevent.pywsgi import WSGIServer
    GEVENT_AVAILABLE = True
except ImportError:
    GEVENT_AVAILABLE = False
    print("Warning: gevent not installed. Using Flask development server.")

# TensorFlow and tf.keras
#import tensorflow as tf
#from tensorflow import keras

from tensorflow.keras.applications.imagenet_utils import preprocess_input
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Some utilites
import numpy as np
from util import base64_to_pil


# Declare a flask app
app = Flask(__name__)

# Create uploads directory if it doesn't exist
os.makedirs('uploads', exist_ok=True)

MODEL_PATH = 'models/oldModel.h5'

# Check if model exists before loading
if not os.path.exists(MODEL_PATH):
    print(f"Error: Model file not found at {MODEL_PATH}")
    print("Please place your trained model file in the models/ directory")
    sys.exit(1)

model = load_model(MODEL_PATH)
print('Model loaded. Start serving...')


def model_predict(img, model):
    
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x, mode='tf')
    
    preds = model.predict(x)
    
    return preds


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        
        # Get the image from post request
        img = base64_to_pil(request.json)
       
                
        img.save("uploads/image.jpg")
        
        img_path = os.path.join(os.path.dirname(__file__),'uploads/image.jpg')
        
        os.path.isfile(img_path)
        
        img = image.load_img(img_path, target_size=(64,64))

        preds = model_predict(img, model)
        
        
        result = preds[0,0]
        
        print(result)
        
        if result >0.5:
            return jsonify(result="PNEUMONIA")
        else:
            return jsonify(result="NORMAL")

    return None


if __name__ == '__main__':
    # For development
    app.run(debug=True, host='0.0.0.0', port=5000)
    
    # For production with gevent (only if available)
    # if GEVENT_AVAILABLE:
    #     http_server = WSGIServer(('0.0.0.0', 5000), app)
    #     http_server.serve_forever()
    # else:
    #     app.run(host='0.0.0.0', port=5000)
