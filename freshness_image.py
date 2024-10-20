import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def get_shelf_life(predicted_class, T, H):
    # Define the shelf life for each class based on temperature and humidity conditions
    if predicted_class == 'Orange_orange':
        if T > 25 and H < 60:
            return "1-3 days - Spoils quickly due to very high temperature and low humidity."
        elif T > 20 and H < 60:
            return "2-3 days - Spoils faster due to high temperature and low humidity."
        elif T > 20 and H >= 90:
            return "4-7 days - Better shelf life with higher humidity, but risk of mold."
        elif 0 < T <= 4 and 90 <= H <= 95:
            return "2-4 weeks - Optimal storage conditions for extended shelf life."
        elif 5 <= T <= 10 and 60 <= H < 85:
            return "5-10 days - Stable shelf life under moderate conditions."
        elif T <= 0:
            return "1-2 days - Chilling injury may occur due to freezing temperatures."
        elif T < 5 and H > 95:
            return "3-5 days - High risk of mold growth due to very high humidity."
        elif 0 < T <= 5 and H < 60:
            return "7-14 days - Moisture loss may cause drying or shriveling."
        else:
            return "1-2 days - Unsuitable conditions for extended storage."
    
    elif predicted_class == 'black_purple_grapes':
        if T > 20 and H < 60:
            return "1-3 days - High temperature and low humidity cause rapid dehydration."
        elif 15 <= T <= 20 and 60 <= H < 80:
            return "3-5 days - Shelf life is reduced at room temperature."
        elif 0 <= T <= 2 and 90 <= H <= 95:
            return "2 weeks - Optimal storage conditions for maximum freshness."
        elif T < 0:
            return "Several months - Can be frozen, but texture may degrade when thawed."
        elif 5 <= T <= 10 and 60 <= H <= 85:
            return "5-7 days - Moderate conditions provide stable shelf life."
        else:
            return "1-2 days - Suboptimal conditions for grape storage."

    elif predicted_class == 'brown_banana':
        if T > 20:
            return "1-2 days - Spoils rapidly at high temperatures."
        elif 13 <= T <= 15 and 90 <= H <= 95:
            return "3-5 days - Optimal conditions for maintaining quality."
        elif T < 12:
            return "1-3 days - Chilling injury likely below 12°C."
        elif T <= 0:
            return "Several months - Can be frozen, but texture may be affected."
        else:
            return "1-2 days - Suboptimal conditions for banana storage."

    elif predicted_class == 'green_karela':
        if 5 <= T <= 10 and 90 <= H <= 95:
            return "2-3 weeks - Optimal storage conditions for extended shelf life."
        elif T >= 30 and 60 <= H <= 70:
            return "3-4 days - Rapid spoilage in warm ambient conditions."
        elif T < 0:
            return "Not recommended - Freezing can degrade quality."
        elif T == 20:
            return "6-8 days - UV-C treatment can help extend shelf life."
        else:
            return "1-2 weeks - Suboptimal conditions for storage."

    elif predicted_class == 'green_apple':
        if 0 <= T <= 4 and H == 90:
            return "Up to 3 weeks - Optimal storage in the refrigerator crisper drawer."
        elif 18 <= T <= 21:
            return "5-7 days - Will ripen quickly at room temperature."
        elif T < 0:
            return "6-12 months - Freezing can preserve, but may affect texture."
        else:
            return "1-2 weeks - Suboptimal conditions may shorten shelf life."

    elif predicted_class == 'green_banana':
        if 13 <= T <= 14 and 90 <= H <= 95:
            return "2-4 weeks - Optimal storage for extending shelf life."
        elif 20 <= T <= 25:
            return "5-7 days - Ripens naturally at room temperature."
        elif T < 13:
            return "1-3 days - Risk of chilling injury at lower temperatures."
        else:
            return "1 week - Suboptimal conditions may lead to uneven ripening."

    elif predicted_class == 'green_capsicum':
        if 7 <= T <= 13 and 90 <= H <= 95:
            return "2-3 weeks - Optimal storage conditions for prolonged shelf life."
        elif T < 7:
            return "1-2 weeks - Risk of chilling injury at lower temperatures."
        elif 20 <= T <= 25:
            return "3-5 days - Rapid spoilage at room temperature."
        else:
            return "1 week - Suboptimal conditions for storage."

    elif predicted_class == 'green_grapes':
        if 0 <= T <= 2 and 90 <= H <= 95:
            return "2-3 weeks - Optimal refrigeration conditions for extended shelf life."
        elif T < 0:
            return "6-12 months - Can be frozen for long-term storage, but texture may be affected."
        elif 20 <= T <= 25:
            return "3-5 days - Spoils quickly at room temperature."
        else:
            return "1-2 weeks - Suboptimal conditions may reduce shelf life."

    elif predicted_class == 'green_yelloe_orange':
        if 1 <= T <= 10 and 90 <= H <= 95:
            return "2-4 weeks - Optimal refrigeration conditions for extended shelf life."
        elif 20 <= T <= 25:
            return "1-2 weeks - Suitable for room temperature storage, but ripening will be faster."
        elif T < 0:
            return "Up to 12 months - Can be frozen for long-term storage."
        else:
            return "1-2 weeks - Suboptimal conditions may lead to faster spoilage."

    elif predicted_class == 'orange_capsicum':
        if 7 <= T <= 10 and 90 <= H <= 95:
            return "2-3 weeks - Optimal conditions for extended shelf life."
        elif 20 <= T <= 25:
            return "3-5 days - Spoils quickly at room temperature."
        elif T < 0:
            return "6-8 months - Can be frozen for long-term storage."
        else:
            return "1-2 weeks - Suboptimal conditions may reduce quality."

    elif predicted_class == 'red_apple':
        if 0 <= T <= 4 and 90 <= H <= 95:
            return "1-2 months - Optimal conditions in the refrigerator."
        elif 18 <= T <= 21:
            return "1-2 weeks - Suitable for room temperature storage."
        elif T < 0:
            return "6-12 months - Can be frozen for long-term preservation."
        else:
            return "1-3 weeks - Suboptimal conditions may affect quality."

    elif predicted_class == 'red_capsicum':
        if 7 <= T <= 10 and 90 <= H <= 95:
            return "2-3 weeks - Optimal refrigeration conditions for red capsicum."
        elif T < 7:
            return "1-2 weeks - Risk of chilling injury below recommended temperatures."
        elif 20 <= T <= 25:
            return "3-5 days - Rapid spoilage at room temperature."
        else:
            return "1-2 weeks - Suboptimal storage conditions may affect quality."

    elif predicted_class == 'red_grapes':
        if 0 <= T <= 2 and 90 <= H <= 95:
            return "2-3 weeks - Optimal storage conditions in the refrigerator."
        elif 20 <= T <= 25:
            return "5-7 days - Short-term storage at room temperature."
        elif T < 0:
            return "Up to 1 year - Can be frozen for long-term storage."
        else:
            return "1-2 weeks - Suboptimal conditions may reduce shelf life."

    elif predicted_class == 'red_yellow_apple':
        if 0 <= T <= 4 and 90 <= H <= 95:
            return "1-2 months - Optimal storage in the refrigerator."
        elif 18 <= T <= 21:
            return "1-2 weeks - Suitable for room temperature storage."
        elif T < 0:
            return "6-12 months - Can be frozen for long-term preservation."
        else:
            return "1-3 weeks - Suboptimal conditions may shorten shelf life."

    elif predicted_class == 'yellow_bitter_gourd':
        if 5 <= T <= 10 and 90 <= H <= 95:
            return "2-3 weeks - Optimal storage in cold conditions."
        elif T >= 30 and 60 <= H <= 70:
            return "3-4 days - Short shelf life at room temperature."
        elif T == 20:
            return "6-8 days - UV-C treatment can extend shelf life."
        else:
            return "1-2 weeks - Suboptimal conditions for storage."

    elif predicted_class == 'yellow_banana':
        if 20 <= T <= 25:
            return "2-7 days - Typical shelf life at room temperature."
        elif 1 <= T <= 7:
            return "1-2 weeks - Extended freshness in the refrigerator, though peel may darken."
        elif T < 0:
            return "6-12 months - Suitable for freezing."
        elif 12 <= T <= 14 and 90 <= H <= 95:
            return "3-4 weeks - Commercial storage conditions for long-term freshness."
        else:
            return "1 week - Suboptimal storage conditions may reduce quality."

    else:
        return "Unknown class."
# Hide the main tkinter window
Tk().withdraw()

# Ask the user to select an image file
image_path = askopenfilename(title="Select an image", filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])

# Check if the user selected an image
if not image_path:
    print("No image selected.")
    exit()

# Load the model and add a diagnostic print
try:
    model = load_model('Image_classify.keras')
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")

# Define categories
data_cat = ['Orange_orange',
 'black_purple_grapes',
 'brown_banana',
 'green karela',
 'green_apple',
 'green_banana',
 'green_capsicum',
 'green_grapes',
 'green_yelloe_orange',
 'orange_capsicum',
 'red_apple',
 'red_capsicum',
 'red_grapes',
 'red_yellow_apple',
 'yellow karela',
 'yellow_banana']

img_height = 180
img_width = 180

if not os.path.exists(image_path):
    print(f"Image not found: {image_path}")
    exit()

# Load and preprocess the image
try:
    print(f"Selected image: {image_path}")
    image_load = tf.keras.utils.load_img(image_path, target_size=(img_height, img_width))
    img_arr = tf.keras.preprocessing.image.img_to_array(image_load)
    img_bat = np.expand_dims(img_arr, axis=0)

    # Make prediction
    print("Making prediction...")
    predict = model.predict(img_bat)
    print(f"Raw prediction output: {predict}")
    
    # Apply softmax to get probabilities
    score = tf.nn.softmax(predict)
    print(f"Softmax probabilities: {score}")

    # Print the prediction results
    predicted_class = data_cat[np.argmax(score)]
    confidence = np.max(score) * 100
    print(get_shelf_life(predicted_class, 34, 50))
    print(f'Predicted class: {predicted_class} with accuracy: {confidence:.2f}%')
    print(predicted_class)
except Exception as e:
    print(f"Error processing image: {e}")