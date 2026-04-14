import streamlit as st
from google import genai
from config import API_KEY, MODEL_NAME

# ✅ NEW SDK (correct)
client = genai.Client(api_key=API_KEY)

from summarizer import summarize_text
from email_drafter import draft_email
from data_interpreter import interpret_data
from prompt_guide import LESSONS

# 🎨 Page settings
st.set_page_config(page_title="AI Toolkit", layout="centered")

# 🎯 Title
st.title("🤖 Generative AI Copilot Toolkit")

st.markdown("""
Your Personal AI-Powered Work Assistant  
Built with Python + Google Gemini API
""")

# 📋 MENU
st.markdown("## 📋 WHAT WOULD YOU LIKE TO DO?")

choice = st.selectbox(
    "Choose an option",
    [
        "1. 📝 Summarize a Document / Long Text",
        "2. ✉️ Draft a Professional Email",
        "3. 📊 Interpret / Explain Data",
        "4. 🧠 Learn Prompt Engineering",
        "5. 🧪 Test & Improve My Own Prompt",
        "6. 📌 View KPIs & Project Info"
    ]
)

# ================================
# 📝 SUMMARIZER
# ================================
if choice.startswith("1"):
    st.subheader("📝 Document Summarizer")

    text = st.text_area("Paste your text")

    style = st.selectbox(
        "Choose summary style",
        ["Bullet Points", "One Paragraph", "Executive Summary"]
    )

    style_map = {
        "Bullet Points": "bullet points",
        "One Paragraph": "one concise paragraph",
        "Executive Summary": "executive summary with key takeaways"
    }

    if st.button("Summarize"):
        if text.strip():
            try:
                result = summarize_text(text, style_map[style])
                st.success("✅ Summary:")
                st.write(result)
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("⚠️ Please enter some text")


# ================================
# ✉️ EMAIL
# ================================
elif choice.startswith("2"):
    st.subheader("✉️ Email Drafter")

    recipient = st.text_input("Recipient")
    purpose = st.text_input("Purpose")
    key_points = st.text_area("Key Points")

    tone = st.selectbox(
        "Choose tone",
        [
            "formal and professional",
            "friendly but professional",
            "urgent and direct",
            "apologetic and sincere"
        ]
    )

    if st.button("Generate Email"):
        if recipient and purpose:
            try:
                result = draft_email(purpose, tone, key_points, recipient)
                st.success("✅ Email Draft:")
                st.write(result)
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("⚠️ Please fill required fields")


# ================================
# 📊 DATA
# ================================
elif choice.startswith("3"):
    st.subheader("📊 Data Interpreter")

    context = st.text_input("What is this data about?")
    data = st.text_area("Paste your data")

    if st.button("Analyze Data"):
        if data.strip():
            try:
                result = interpret_data(data, context)
                st.success("✅ Interpretation:")
                st.write(result)
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("⚠️ Please enter data")


# ================================
# 🧠 PROMPT GUIDE
# ================================
elif choice.startswith("4"):
    st.subheader("🧠 Prompt Engineering Guide")

    for key, lesson in LESSONS.items():
        st.markdown(f"### 📖 Lesson {key}: {lesson['title']}")
        st.write("🔴 Bad Prompt:", lesson["bad_prompt"])
        st.write("🟢 Good Prompt:", lesson["good_prompt"])
        st.info(lesson["tip"])


# ================================
# 🧪 PROMPT TESTER (FIXED)
# ================================
elif choice.startswith("5"):
    st.subheader("🧪 Prompt Tester")

    user_prompt = st.text_area("Enter your prompt")

    if st.button("Run Prompt"):
        if user_prompt.strip():
            try:
                # ✅ FIXED (use client, not model)
                result = client.models.generate_content(
                    model=MODEL_NAME,
                    contents=user_prompt
                )

                st.write("### 📤 AI Response")
                st.write(result.text)

                critique_prompt = f"""
                You are a prompt engineering expert.
                A user wrote this prompt: "{user_prompt}"

                Give:
                1. Score out of 10
                2. What’s good
                3. Improvements
                4. Better version
                """

                critique = client.models.generate_content(
                    model=MODEL_NAME,
                    contents=critique_prompt
                )

                st.write("### 🔍 Feedback")
                st.write(critique.text)

            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("⚠️ Please enter a prompt")


# ================================
# 📌 KPIs
# ================================
elif choice.startswith("6"):
    st.subheader("📌 Project KPIs & Success Metrics")

    kpis = [
        "70% users complete at least 2 modules",
        "15–30 mins saved per task",
        "AI output rated 4/5 or above",
        "Prompt score improvement by 2+ points",
        "80% email acceptance rate",
        "90% summary accuracy"
    ]

    for k in kpis:
        st.write("✅", k)

    st.markdown("### 🗺️ Learning Modules")

    modules = [
        "Module 1: Use-case Identification",
        "Module 2: Responsible AI",
        "Module 3: Prompt Engineering",
        "Module 4: AI Workflows",
        "Module 5: Measuring Impact"
    ]

    for m in modules:
        st.write("📚", m)
