# 🛡️ Spam Shield

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![NLTK](https://img.shields.io/badge/NLTK-154f3c?style=for-the-badge)](https://www.nltk.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Deployed on Streamlit Cloud](https://img.shields.io/badge/Deployed-Streamlit%20Cloud-FF4B4B?style=for-the-badge&logo=streamlit)](https://spam-shield-app.streamlit.app/)
[![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)](https://spam-shield-app.streamlit.app/)

### *One message, one click — spam or not, decided instantly.*

A binary text classification project that detects spam SMS/Email messages using NLP preprocessing
(tokenization, stopword removal, stemming) and TF-IDF vectorization. Eleven classifiers were
benchmarked end-to-end, and **Bernoulli Naive Bayes** was selected as the final model for its
perfect precision — meaning zero real messages were ever misclassified as spam.

🌐 **[Open Live Demo →](https://sms-spam-shield.streamlit.app/)**


---

## Live demo

🌐 **[spam-shield-app.streamlit.app](https://sms-spam-shield.streamlit.app/)**

Paste in any SMS or email text and hit **Predict** — no login, no setup, works instantly in the browser.

## How to run this project locally

### Prerequisites

- Python 3.10+
- pip

### Steps

```
# Clone the repository
git clone https://github.com/Rushit004/spam-shield.git
cd spam-shield

# Create a virtual environment & install dependencies
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux
pip install -r requirements.txt

# Download required NLTK corpora (one-time)
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"

# Run the app
streamlit run main.py
```

> Want to retrain on a different dataset or try a different model? Open `SMS-spam-detector.ipynb`,
> run all cells, and it will regenerate `model.pkl` + `vectorizer.pkl`.

---

## ✨ Features

- 🎯 **Real-time spam detection** — type or paste a message and get an instant Spam / Not Spam verdict
- 🧹 **Full NLP preprocessing pipeline** — lowercasing, tokenization, alphanumeric filtering, stopword/punctuation removal, and stemming via `PorterStemmer`
- 📊 **TF-IDF vectorization** (`TfidfVectorizer`) to turn cleaned text into model-ready feature vectors
- 🏆 **Benchmarked across 11 classifiers** — the best-performing model on precision was selected for deployment
- 🛡️ **Zero false positives** — the chosen model (BernoulliNB) never flags a genuine message as spam on the test set
- ⚡ **Train-once, serve-via-pickle** — `model.pkl` and `vectorizer.pkl` are precomputed offline, so the app does zero training at request time

---

## 🎮 How to Use

### Step 1 — Enter a Message

Paste or type any SMS / email text into the input box.

### Step 2 — Hit Predict

Click **`Predict`**. The app preprocesses your text, converts it to a TF-IDF vector, and runs it through the trained model.

### Step 3 — Read the Result

The app displays **Spam** or **Not Spam** based on the model's prediction.

---

## 🧠 Behind the Scenes: Classification Pipeline

```
SMS / Email message
        │  lowercase
        ▼
nltk.word_tokenize
        │  keep alphanumeric tokens only
        ▼
remove stopwords + punctuation
        │  PorterStemmer
        ▼
cleaned, stemmed token string
        │  TfidfVectorizer.transform
        ▼
TF-IDF feature vector
        │  BernoulliNB.predict
        ▼
Spam / Not Spam
```

---

## 🧪 ML Concepts Demonstrated

This project covers concepts typically taught in an intro Data Science / NLP course:

- Binary text classification
- Bag-of-Words / TF-IDF text vectorization
- NLP preprocessing: tokenization, stopword removal, punctuation filtering, stemming (`PorterStemmer`, NLTK)
- Multi-model benchmarking across 11 classifiers (SVC, KNN, Multinomial/Bernoulli/Gaussian Naive Bayes, Decision Tree, Logistic Regression, Random Forest, AdaBoost, Bagging, Extra Trees, Gradient Boosting, XGBoost)
- Precision-first model selection — optimizing to minimize false positives, since misclassifying a real message as spam is costlier than missing an actual spam message
- Train-once, serve-via-pickle architecture

### Model Comparison

| Model | Accuracy | Precision |
| --- | --- | --- |
| SVC | 0.9758 | 0.9748 |
| KNN | 0.9052 | 1.0000 |
| **BernoulliNB (selected)** | **0.9710** | **1.0000** |
| Decision Tree | 0.9294 | 0.8283 |
| Logistic Regression | 0.9565 | 0.9697 |
| Random Forest | 0.9768 | 0.9750 |
| AdaBoost | 0.9236 | 0.8391 |
| Bagging Classifier | 0.9594 | 0.8692 |
| Extra Trees | 0.9778 | 0.9675 |
| Gradient Boosting | 0.9507 | 0.9307 |
| XGBoost | 0.9710 | 0.9500 |

BernoulliNB was chosen over models with marginally higher accuracy (like Extra Trees or Random Forest)
because of its perfect precision score — in a spam filter, a false positive (a real message wrongly
blocked as spam) is far more disruptive than a false negative (a spam message that slips through).

---

## 📊 Dataset

`spam.csv` — a labeled collection of SMS messages tagged as **spam** or **ham** (legitimate), used to
train and evaluate all eleven classifiers above.

---

## 🗂️ Project Structure

```
spam-shield/
│
├── SMS-spam-detector.ipynb   # EDA, preprocessing, model benchmarking & selection notebook
├── main.py                   # Streamlit app — UI, preprocessing, prediction
├── model.pkl                 # Trained BernoulliNB classifier
├── vectorizer.pkl            # Fitted TfidfVectorizer
├── spam.csv                  # Labeled SMS spam/ham dataset
├── requirements.txt          # Python dependencies
├── .gitignore
└── README.md
```

---

## 🛠️ Tech Stack

| Technology | Role |
| --- | --- |
| Python 3 | Core language |
| Pandas / NumPy | Data loading & cleaning |
| scikit-learn | TF-IDF vectorization, model training & evaluation |
| NLTK (`word_tokenize`, `stopwords`, `PorterStemmer`) | Text preprocessing & normalization |
| Streamlit | Web app UI, deployed on Streamlit Community Cloud |
| Pickle | Model & vectorizer serialization |

---

## About the Author

**Rushit Tholiya**
[LinkedIn Profile](https://www.linkedin.com/in/rushit-tholiya-605341311/)

[GitHub Profile](https://github.com/Rushit004)
