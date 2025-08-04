import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# load the dataset
df = pd.read_csv(r"D:\spam_ham_dataset.csv")

# Getting the first few rows. 
print(df.head())

# Don't need to Convert Labels: 'ham' into 'spam' 
# If needed the following code would have done it.
# df['label'] =  df['label'].map({'ham':0, 'spam':1})

# Split data
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label_num'], test_size = 0.2, random_state=4)

# Create pipelines: vectorizer plus Naive Bayes classifier
model  = make_pipeline(CountVectorizer(), MultinomialNB())

# Train model
model.fit(X_train, y_train)

# Save the trained model in the joblib

joblib.dump(model, "spam_classifier.pkl")

#Print the model

print("Model Trained and saved successfully")