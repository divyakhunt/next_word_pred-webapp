# 🔮 Next Word Prediction Web App

This is a deep learning-powered web app that predicts the **next word** as you type, trained on the classic **Sherlock Holmes stories**. The app provides real-time next-word predictions and allows inserting the predicted word with the `Tab` key.


🔗 **Live Web App**: [https://next-word-predictor-rmby.onrender.com/](https://divyakhunt-next-word-predictor.hf.space/)

### 🎬 Demo Video  
📽️ [Click to watch the demo video](https://drive.google.com/file/d/1-QAO7aA3q0S0fF5Dh7zhnBMnSWn8IKgM/view?usp=sharing)

---

## 📚 Dataset

- **Source**: [The Adventures of Sherlock Holmes - Kaggle](https://www.kaggle.com/datasets/cashncarry/the-adventures-of-sherlock-holmes)
- The model is trained on the full text of Sherlock Holmes, processed and tokenized to build an LSTM-based sequence predictor.

---

## 🚀 Features

- 🔤 Predicts the next word in real-time as you type.
- 🧠 Bi-LSTM deep learning model trained on Sherlock Holmes stories.
- ⌨️ Press `Tab` to insert the predicted word directly into the text area.
- 🌐 Deployed-ready Flask web application with styled frontend.

---

## 🧠 Model Training Code

Curious about how I trained the model behind this app?

The training process — including **data preprocessing**, **tokenization**, and the **Bidirectional LSTM architecture** — is documented in detail in the Jupyter Notebook below:

📓 **Explore the Model Training Notebook:**  
[🔗 Model Training Code on GitHub](https://github.com/divyakhunt/next-word-predictor/blob/main/next_word_predictor.ipynb)

> 📁 *This is my GitHub repository link that explains how I trained the model used in this web app.*  
> 🧠 The notebook walks you through each step of the training process — from preprocessing and tokenization to building the Bidirectional LSTM model.

---

## 📁 Project Structure

```
├── static/                                    # CSS & JS files
├── templates/                                 # HTML templates (e.g., index.html)
├── app.py                                     # Flask backend
├── next_word_model.h5                         # Trained Keras model
├── tokenizer.pkl                              # Tokenizer used for input processing
├── requirements.txt                           # Required Python packages
├── Dockerfile                                 # Hugging Face build config
└── .gitattributes                             # Git LFS tracking

```

---

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/divyakhunt/next_word_pred-web.git
   cd next_word_pred-web
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   python app.py
   ```

5. Open your browser and visit:  
   `http://127.0.0.1:5000/`

---

## 🌐 Deployment

### Render / Railway

- **Build Command**:  
  `pip install -r requirements.txt`

- **Start Command**:  
  `python app.py`

- `Procfile` should contain:
  ```
  web: python app.py
  ```

---

## 📦 Notes

- This project uses **Git LFS** to track large files like `.h5` and `.pkl`.
- Before pushing or pulling:
  ```bash
  git lfs install
  git lfs pull
  ```

---

## 🙋‍♂️ Author

**Divya Khunt**  
🔗 GitHub: [@divyakhunt](https://github.com/divyakhunt)  
⭐ If you like this project, please consider starring the repo.

---

## 📜 License

This project is open-sourced under the [MIT License](LICENSE).
