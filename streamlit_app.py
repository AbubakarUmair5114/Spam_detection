import streamlit as st
import joblib

# --- Load the full pipeline (vectorizer + model) ---
@st.cache_resource
def load_pipeline():
    return joblib.load("spam_classifier.pkl")

model = load_pipeline()

# --- Page Setup ---
st.set_page_config(page_title="Spam Classifier", page_icon="📧", layout="centered")

st.markdown("<h1 style='text-align: center;'>📧 Email/SMS Spam Classifier</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Paste or write your message below to check whether it's spam or not.</p>", unsafe_allow_html=True)

# --- Text Input ---
message = st.text_area("Enter your message:")

# --- Predict Button ---
if st.button("✅ Check Spam"):
    if message.strip() == "":
        st.warning("Please enter a message first.")
    else:
        prediction = model.predict([message])[0]

        if prediction == 1:
            st.error("🚫 This message is **SPAM**")
        else:
            st.success("✅ This message is **NOT SPAM**")

# --- Footer ---
st.markdown("---")
st.markdown("### 🙌 Thank You for Using the Spam Classifier App!")
st.markdown("""
- 🔍 Built with **Python + Streamlit**  
- 📦 Model trained using **Scikit-learn**  

<small>This tool helps classify messages as SPAM or NOT SPAM using machine learning.</small>
""", unsafe_allow_html=True)

