from flask import Flask, request, render_template, jsonify
import tensorflow as tf
import numpy as np
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

# Load model
print("Loading model...")
model = tf.keras.models.load_model("next_word_model.h5")
print("Model loaded successfully.")

# Load tokenizer
print("Loading tokenizer...")
with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)
print("Tokenizer loaded successfully.")

# Match this with your training
MAX_LEN = 20
print(f"MAX_LEN set to {MAX_LEN}")

def predict_next_word(text):
    token_seq = tokenizer.texts_to_sequences([text])[0]
    padded_seq = pad_sequences([token_seq], maxlen=MAX_LEN-1, padding='pre')
    prediction = model.predict(padded_seq, verbose=0)
    next_index = np.argmax(prediction)
    next_word = tokenizer.index_word.get(next_index, "")
    return next_word

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_text = request.json['input_text']
    next_word = predict_next_word(input_text.strip())
    return jsonify({'next_word': next_word})

if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(debug=True)
