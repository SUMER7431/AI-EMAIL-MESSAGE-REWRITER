import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv(override=True)

st.set_page_config(
    page_title="Rewrite AI",
    page_icon="✦",
    layout="centered"
)

# Modern dark theme
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #08090f 0%, #111322 55%, #090a12 100%);
    color: #f5f5fa;
}
.block-container {
    max-width: 850px;
    padding-top: 2.5rem;
    padding-bottom: 3rem;
}
.hero {
    text-align: center;
    padding: 28px 10px 20px;
}
.logo {
    display: inline-block;
    color: #c4a5ff;
    background: #211936;
    border: 1px solid #49336d;
    border-radius: 16px;
    padding: 12px 18px;
    font-size: 28px;
    margin-bottom: 14px;
}
.hero h1 {
    color: #ffffff;
    font-size: 2.7rem;
    font-weight: 750;
    letter-spacing: -1.5px;
    margin-bottom: 10px;
}
.hero p {
    color: #a6a8bd;
    font-size: 1.05rem;
}
.section-label {
    color: #d4c4ff;
    font-size: 0.9rem;
    font-weight: 650;
    margin: 16px 0 8px;
}
.stTextArea textarea {
    background-color: #151722 !important;
    color: #f5f5fa !important;
    border: 1px solid #34364a !important;
    border-radius: 12px !important;
}
.stTextArea textarea:focus {
    border-color: #9870ff !important;
    box-shadow: 0 0 0 1px #9870ff !important;
}
.stSelectbox div[data-baseweb="select"] > div {
    background-color: #151722;
    border-color: #34364a;
    border-radius: 10px;
    color: white;
}
.stButton > button {
    background: linear-gradient(90deg, #8155ed, #5378f5);
    color: white;
    border: none;
    border-radius: 12px;
    min-height: 3.2rem;
    font-size: 1rem;
    font-weight: 700;
    transition: 0.2s ease;
}
.stButton > button:hover {
    border: 1px solid #c3a9ff;
    color: white;
    box-shadow: 0 0 22px #7955ed45;
}
.result-card {
    background: #151722;
    border: 1px solid #34364a;
    border-radius: 14px;
    padding: 18px;
    margin-top: 12px;
}
.footer {
    text-align: center;
    color: #777b94;
    font-size: 0.8rem;
    padding-top: 35px;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="hero">
    <div class="logo">✦</div>
    <h1>Rewrite <span style="color:#a78bfa">AI</span></h1>
    <p>Turn your thoughts into the right words.</p>
</div>
""", unsafe_allow_html=True)

# API setup
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("API key not found. Please check your .env file.")
    st.stop()

client = genai.Client(api_key=api_key)

# Message input
st.markdown('<div class="section-label">✎ &nbsp; YOUR ORIGINAL MESSAGE</div>',
            unsafe_allow_html=True)

message = st.text_area(
    "Your original message",
    placeholder="Type or paste your message here...",
    height=180,
    label_visibility="collapsed"
)

# Tone selection
st.markdown('<div class="section-label">✦ &nbsp; CHOOSE YOUR TONE</div>',
            unsafe_allow_html=True)

tone = st.selectbox(
    "Choose a tone",
    [
        "Professional",
        "Polite",
        "Friendly",
        "Casual",
        "Formal",
        "Confident",
        "Apologetic",
        "Short and clear"
    ],
    label_visibility="collapsed"
)

# Rewrite button
rewrite_clicked = st.button(
    "✦  Rewrite My Message",
    use_container_width=True,
    type="primary"
)

if rewrite_clicked:
    if not message.strip():
        st.warning("Please enter a message first.")
    else:
        with st.spinner("✨ Rewriting your message..."):
            try:
                response = client.models.generate_content(
                    model="gemini-3.1-flash-lite",
                    contents=f"""
Rewrite the following message in a {tone.lower()} tone.

Keep the original meaning.
Do not add facts that are not in the original message.
Return only the rewritten message.

Original message:
{message}
"""
                )

                rewritten = response.text or ""
                if rewritten.strip():
                    st.markdown(
                        '<div class="section-label">✦ &nbsp; YOUR REWRITTEN MESSAGE</div>',
                        unsafe_allow_html=True
                    )
                    st.text_area(
                        "Your rewritten message",
                        value=rewritten,
                        height=180
                    )
                    st.caption("Select the result text to copy it.")
                else:
                    st.warning("The AI returned an empty response. Please try again.")

            except Exception as e:
                st.error(f"Something went wrong: {e}")

st.markdown(
    '<div class="footer">✦ Made with AI · Your words, refined.</div>',
    unsafe_allow_html=True
)