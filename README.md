🧠 Description:
LangNav is an interactive web application that intelligently recommends the most suitable programming or spoken language to learn based on a user's personal and professional goals. Whether your aim is to get a job, travel abroad, conduct research, or start a business, LangNav analyzes your inputs using a fine-tuned AI model and provides a personalized language suggestion with clear reasons.

The system leverages OpenRouter’s AI models (like Mistral) via the OpenAI-compatible API and is built using Streamlit for a fast and simple user interface.

🎯 Key Features:
✅ User-friendly web form (built in Streamlit)
🤖 GPT-powered personalized language recommendations
🧭 Input parameters: goal, field of interest, available study time, native language
💬 Output: 1-2 recommended languages with bullet-point explanations
🌐 Supports both spoken and programming languages

🔧 Tech Stack:
Frontend/UI: Streamlit (Python-based web framework)
Backend: Python
AI Model: OpenRouter (e.g., Mistral-7B-Instruct)
API: OpenAI-compatible endpoint via OpenRouter
Deployment: Localhost or Streamlit Cloud

📥 User Input:
Main Goal (Job / Travel / Research / Startup)
Domain or Interest Area (AI / Data Science / Linguistics / etc.)
Available Time per Week (in hours)
Native Language (Optional)

📤 AI Output:
One or two language recommendations (e.g., Python, Spanish)
Reasoning in bullet points
Beginner-friendly explanation

💡 Use Case Examples:
A user interested in data science with 5 hours/week is suggested Python and SQL.
A user who wants to travel across Europe is recommended Spanish or French.

🧩 Possible Future Enhancements:
User authentication and history tracking
Language learning roadmap and resources
Integration with Duolingo or GitHub APIs
Downloadable recommendations as PDF
