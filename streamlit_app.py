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
st.set_page_config(page_title="Spam or Not?", page_icon="🎯", layout="centered")

st.markdown("""
    <h1 style='color: #FF4B4B; text-align: center;'>🚨 Spam Detector 3000 🚨</h1>
    <p style='text-align:center; font-size:18px;'>Find out if your message is a scam in disguise!</p>
""", unsafe_allow_html=True)

st.markdown("#### 📝 Your Message")
message = st.text_area("", height=120, placeholder="Write your message here...")

if st.button("🔍 Check Now"):
    st.error("⚠️ Spam Detected!")  # Replace with real prediction

st.markdown("---")
st.info("🎉 Try out various messages to test our spam detector!")


