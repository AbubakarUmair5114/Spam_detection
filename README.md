# 📧 Spam Classifier Web App

This is a simple machine learning web app built using **Streamlit** that classifies messages as **Spam** or **Not Spam**. It uses a **Naive Bayes** model trained on a public SMS dataset.

---

## 🚀 Features

- Predicts whether a message is **SPAM** or **NOT SPAM**
- Easy-to-use web interface powered by **Streamlit**
- Trained using real-world SMS data from UCI
- Model built with `scikit-learn` and saved with `joblib`

---

## 🔧 Tools & Libraries Used

| Tool         | Description                                      |
|--------------|--------------------------------------------------|
| Python       | Core language used for development               |
| scikit-learn | Machine learning library for model training      |
| Streamlit    | Web-based GUI framework                          |
| Joblib       | For saving and loading the trained model         |
| UCI Dataset  | Public dataset with labeled spam/ham messages    |

---

## 🧠 How It Works

1. Loads the SMS Spam dataset from UCI.
2. Preprocesses the messages using `CountVectorizer`.
3. Trains a **Multinomial Naive Bayes** classifier.
4. Saves the model using `joblib`.
5. The Streamlit app loads the trained model and predicts the label of any input message.

---

## 🧪 Sample Message Predictions

| Message                                                | Prediction   |
|--------------------------------------------------------|--------------|
| "Congratulations! You’ve won a free cruise!"           | 🚨 SPAM      |
| "Hi, are you free this weekend to catch up?"           | ✅ NOT SPAM  |
| "Urgent! Your account is at risk. Click the link now"  | 🚨 SPAM      |
| "Reminder: Your appointment is at 4:30 PM tomorrow."   | ✅ NOT SPAM  |

---

## ▶️ How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/spam-classifier
   cd spam-classifier

