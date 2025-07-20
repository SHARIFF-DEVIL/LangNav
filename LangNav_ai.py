import openai
import streamlit as st

# ✅ Set your OpenRouter API Key
openai.api_key = "Open_ai_key" #replace your openai key
openai.api_base = "https://openrouter.ai/api/v1"

def get_recommendation(purpose, domain, time, native):
    prompt = f"""
Suggest the best programming or spoken language to learn based on the following:

Goal: {purpose}
Domain: {domain}
Available time: {time} hours per week
Native language: {native}

Give your recommendation and also explain why in bullet points.
Limit to top 1 or 2 options. Use simple language.
"""

    try:
        response = openai.ChatCompletion.create(
            model="mistralai/mistral-7b-instruct",
            messages=[
                {"role": "system", "content": "You are a helpful AI language advisor. Recommend the best language to learn."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"❌ Error: {e}"

# ------------------ UI ------------------

st.set_page_config(page_title="LangNav - Language Recommender", page_icon="🌐")
st.title("🌐 LangNav – AI Language Recommendation System")
st.markdown("Get the best programming or spoken language recommendation based on your goals 🎯")

with st.form("langnav_form"):
    purpose = st.text_input("1️⃣ What is your main goal? (e.g., job, travel, research, startup)")
    domain = st.text_input("2️⃣ What is your field or interest area? (e.g., data science, embedded, AI)")
    time = st.text_input("3️⃣ How much time can you commit weekly? (in hours)")
    native = st.text_input("4️⃣ What is your native language? (optional)")
    submitted = st.form_submit_button("Get Recommendation 🚀")

if submitted:
    if not purpose or not domain or not time:
        st.error("Please fill in all required fields (except native language).")
    else:
        with st.spinner("Thinking..."):
            result = get_recommendation(purpose, domain, time, native)
        st.success("✅ Recommendation Ready!")
        st.markdown("### 💡 Suggested Language & Reasoning:")
        st.markdown(result)
