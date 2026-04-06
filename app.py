import streamlit as st
import joblib
import time
st.write("🔥 UPDATED VERSION 100%")
# ---------------- LOAD MODEL ----------------
model = joblib.load("phishing_pipeline.pkl")

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Shield", page_icon="🛡", layout="centered")

# ---------------- STYLING ----------------
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #e0f2fe, #f8fafc);
}

/* Title */
.title {
    text-align: center;
    font-size: 44px;
    font-weight: 700;
    color: #0f172a;
    animation: fadeIn 1.5s ease-in-out;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 16px;
    color: #475569;
    margin-bottom: 30px;
    animation: fadeIn 2s ease-in-out;
}

/* Card */
.card {
    background: white;
    padding: 30px;
    border-radius: 18px;
    box-shadow: 0 15px 40px rgba(0,0,0,0.08);
    animation: slideUp 1s ease;
}

/* Inputs */
.stTextArea textarea {
    border-radius: 12px;
    border: 1px solid #cbd5e1;
}

/* Button */
.stButton>button {
    background: linear-gradient(45deg, #38bdf8, #0ea5e9);
    color: white;
    border-radius: 12px;
    height: 3.2em;
    width: 100%;
    font-weight: 600;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 20px rgba(14,165,233,0.6);
}

/* Result */
.result {
    padding: 16px;
    border-radius: 12px;
    text-align: center;
    font-size: 18px;
    margin-top: 20px;
    font-weight: 600;
    animation: slideUp 0.6s ease;
}

/* Footer */
.footer {
    text-align: center;
    font-size: 14px;
    color: #64748b;
    margin-top: 40px;
}

/* Animations */
@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}

@keyframes slideUp {
    from {opacity: 0; transform: translateY(25px);}
    to {opacity: 1; transform: translateY(0);}
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<div class="title">🛡 AI Shield</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered system to detect phishing and scam messages in real-time</div>', unsafe_allow_html=True)

# ---------------- MAIN CARD ----------------
st.markdown('<div class="card">', unsafe_allow_html=True)

option = st.radio("Select Content Type", ["Email", "Message"])

user_input = st.text_area(f"Enter {option} Content", height=180)

if st.button("🔍 Analyze Content"):
    if user_input.strip() == "":
        st.warning("Please enter content to analyze")
    else:
        with st.spinner("Analyzing with AI model..."):
            time.sleep(1)  # smooth UX

            prediction = model.predict([user_input])[0]

        if prediction == 1:
            st.markdown(
                '<div class="result" style="background:#fee2e2;color:#b91c1c;">⚠ Scam Detected</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                '<div class="result" style="background:#dbeafe;color:#1e3a8a;">✔ Safe Content</div>',
                unsafe_allow_html=True
            )

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- EXTRA INFO ----------------
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### ⚡ Fast")
    st.write("Instant predictions using optimized ML model")

with col2:
    st.markdown("### 🔒 Secure")
    st.write("Your data is not stored or shared")

with col3:
    st.markdown("### 🧠 AI Based")
    st.write("Trained on real-world phishing datasets")

# ---------------- FOOTER ----------------
st.markdown('<div class="footer">Made by Vivek Trivedi | Machine Learning Project</div>', unsafe_allow_html=True)