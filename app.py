import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import subprocess
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Freshness Image Route
@app.route('/run_freshness_image', methods=['POST'])
def run_freshness_image():
    os.environ['PYTHONIOENCODING'] = 'utf-8'
    # Capture the output of the script, ensure UTF-8 encoding is used to handle special characters
    result = subprocess.run(['python', 'freshness_image.py'], capture_output=True, text=True, encoding='utf-8')
    
    # Send the output back to the browser
    output_lines = result.stdout.strip().split('\n')
    
    # Get the last 3 lines of the output
    last_three_lines = '\n'.join(output_lines[-3:])
    
    # Send only the last 3 lines back to the browser
    return f"<h2>Output of Freshness Image Script:</h2><pre>{last_three_lines}</pre>"




@app.route('/run_freshness_video', methods=['POST'])
def run_freshness_video():
    subprocess.run(['python', 'freshness_video.py'])  # Replace with actual script
    return "Freshness Video Script Executed"

# Recognition routes
@app.route('/run_recognition_image', methods=['POST'])
def run_recognition_image():
    subprocess.run(['python', 'recognition_image.py'])  # Replace with actual script
    return "Recognition Image Script Executed"

@app.route('/run_recognition_video', methods=['POST'])
def run_recognition_video():
    subprocess.run(['python', 'recognition_video.py'])  # Replace with actual script
    return "Recognition Video Script Executed"

# OCR routes
@app.route('/run_ocr_image', methods=['POST'])
def run_ocr_image():
    subprocess.run(['python', 'ocr_image.py'])  # Replace with actual script
    return "OCR Image Script Executed"

@app.route('/run_ocr_video', methods=['POST'])
def run_ocr_video():
    subprocess.run(['python', 'ocr_video.py'])  # Replace with actual script
    return "OCR Video Script Executed"

if __name__ == '__main__':
    app.run(debug=True)
