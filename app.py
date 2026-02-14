import streamlit as st
import joblib

# Load model
model = joblib.load("phishing_pipeline.pkl")

st.set_page_config(
    page_title="Scam Detection System",
    layout="centered"
)

# -------- CLEAN WHITE PROFESSIONAL THEME -------- #
st.markdown("""
<style>
.stApp {
    background-color: #F7F9FC;
}

/* Title */
h1 {
    color: #1A1A1A;
    text-align: center;
    font-size: 40px;
    font-weight: 600;
}

/* Divider */
hr {
    border: 1px solid #E0E6ED;
}

/* Labels */
label {
    color: #333333 !important;
    font-weight: 500;
}

/* Text Area */
.stTextArea textarea {
    background-color: #FFFFFF;
    color: #000000;
    border-radius: 8px;
    border: 1px solid #D1D9E6;
}

/* Buttons */
.stButton>button {
    background-color: #2563EB;
    color: white;
    border-radius: 8px;
    height: 3em;
    width: 100%;
    font-weight: 600;
    border: none;
}

.stButton>button:hover {
    background-color: #1E4DB7;
}

/* Result Box */
.result-box {
    padding: 16px;
    border-radius: 8px;
    text-align: center;
    font-size: 18px;
    margin-top: 20px;
    font-weight: 500;
}
</style>
""", unsafe_allow_html=True)

# -------- TITLE -------- #
st.title("Scam Detection System")

st.markdown("---")

# -------- OPTION SELECT -------- #
option = st.radio(
    "Choose Content Type",
    ("Email", "Message")
)

st.markdown("---")

# -------- INPUT -------- #
user_input = st.text_area(
    f"Enter {option} Content Below:",
    height=200
)

# -------- ANALYZE BUTTON -------- #
if st.button("Analyze Content"):
    if user_input.strip() == "":
        st.warning("Please enter content to analyze.")
    else:
        prediction = model.predict([user_input])[0]

        if prediction == 1:
            st.markdown(
                '<div class="result-box" style="background-color:#FFE5E5;color:#C62828;">⚠ Scam Detected</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                '<div class="result-box" style="background-color:#E6F4EA;color:#1B5E20;">✔ Safe Content</div>',
                unsafe_allow_html=True
            )

st.markdown("---")
st.caption("Machine Learning Based Scam Classification System")
