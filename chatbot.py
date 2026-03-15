import streamlit as st
import time

st.set_page_config(page_title="Study Helper Bot", page_icon="🤖", layout="wide")

# ---------- Custom CSS ----------

st.markdown("""
<style>

.stApp {
background: linear-gradient(135deg,#dbeafe,#f0f9ff,#e0f7fa);
}

h1 {
text-align:center;
color:#1f2937;
}

h3 {
color:#1f2937;
}

/* User chat bubble */
.stChatMessage[data-testid="stChatMessage-user"] {
background-color:#bfdbfe;
border-radius:12px;
padding:10px;
color:#111111;
}

/* Bot chat bubble */
.stChatMessage[data-testid="stChatMessage-assistant"] {
background-color:#bbf7d0;
border-radius:12px;
padding:10px;
color:#111111;
}

/* Buttons */
.stButton>button {
background-color:#2563eb;
color:white;
border-radius:8px;
padding:8px 16px;
}

/* Sidebar text */
section[data-testid="stSidebar"] * {
color:white;
}

/* Sidebar background */
section[data-testid="stSidebar"] {
background-color:#1e293b;
}

</style>
""", unsafe_allow_html=True)
# ---------- Title ----------
st.title("🤖 Study Helper Chatbot")

# ---------- Sidebar ----------
with st.sidebar:
    st.markdown('<p class="sidebar-title">About This Bot</p>', unsafe_allow_html=True)
    st.write("This is a **rule-based chatbot** built using Python and Streamlit.")
    
    st.markdown("### Example Questions")
    st.write("• hello")
    st.write("• study tips")
    st.write("• exam preparation")
    st.write("• assignment help")
    st.write("• motivation")

# ---------- Chat history ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------- Rule-based responses ----------
def chatbot_response(user_input):

    text = user_input.lower()

    if "hello" in text or "hi" in text:
        return "👋 Hello! I'm your Study Helper Bot. Ask me anything about studying."

    elif "help" in text:
        return "😊 I'm here to help! You can ask me about study tips, exams, assignments, or motivation."

    elif "question" in text:
        return "❓ If you have a question about studying or exams, I'll try my best to guide you."

    elif "solve" in text:
        return "🧠 I can help you think through problems. Try breaking the problem into smaller steps."

    elif "answer" in text:
        return "📘 I'll try to answer your question if it's related to studies."

    elif "study tips" in text:
        return "📚 Study tip: Use the Pomodoro technique — 25 minutes of focus followed by a 5 minute break."

    elif "exam" in text:
        return "📝 For exams: revise regularly and practice previous year question papers."

    elif "assignment" in text:
        return "📂 Start assignments early and divide them into small manageable tasks."

    elif "stress" in text:
        return "🌿 Take a short break, drink water, and try some deep breathing."

    elif "motivation" in text:
        return "🔥 Keep going! Even 1 hour of focused study today makes a difference."

    elif "ai" in text:
        return "🤖 AI stands for Artificial Intelligence — machines designed to perform tasks that normally require human intelligence."

    elif "bye" in text:
        return "👋 Goodbye! Keep studying and doing your best."

    else:
        return "🤔 I'm not sure about that. Try asking about study tips, exams, assignments, or motivation."

# ---------- Quick question buttons ----------
st.markdown("### Quick Questions")

col1, col2, col3, col4 = st.columns(4)

if col1.button("Study Tips"):
    user_prompt = "study tips"
elif col2.button("Exam Help"):
    user_prompt = "exam preparation"
elif col3.button("Assignment Help"):
    user_prompt = "assignment help"
elif col4.button("Motivation"):
    user_prompt = "motivation"
else:
    user_prompt = None

# ---------- Chat input ----------
prompt = st.chat_input("Ask something about studying...")

if prompt:
    user_prompt = prompt

if user_prompt:

    st.chat_message("user").markdown(user_prompt)
    st.session_state.messages.append({"role":"user","content":user_prompt})

    response = chatbot_response(user_prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        for word in response.split():
            full_response += word + " "
            time.sleep(0.05)
            message_placeholder.markdown(full_response)

    st.session_state.messages.append({"role":"assistant","content":response})