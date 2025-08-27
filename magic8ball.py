
import random
import streamlit as st

# ----- Page setup -----
st.set_page_config(page_title="Mystic 8-Ball", page_icon="🔮", layout="centered")

# Subtle purple theme & a glowing orb
st.markdown("""
<style>
/* Page background */
.stApp {
  background: radial-gradient(1200px 600px at 50% -10%, #6e3bc7 0%, #2c184e 35%, #140a26 70%, #0c0716 100%);
  color: #EEE;
  font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, "Helvetica Neue", Arial;
}

/* Cards and boxes */
.block-container { padding-top: 3.2rem; }
.css-1dp5vir, .css-1r6slb0, .stTextInput>div>div>input, .stNumberInput>div>div>input, .stTextArea>div>div>textarea {
  color: #EEE !important;
}

/* Inputs & buttons */
.stTextInput input, .stTextArea textarea {
  background: rgba(255,255,255,0.06);
  border: 1px solid rgba(255,255,255,0.18);
}
.stButton>button {
  background: linear-gradient(135deg, #9b59ff, #6c3bff);
  border: 1px solid rgba(255,255,255,0.25);
  color: white;
  font-weight: 600;
  border-radius: 12px;
  padding: 0.6rem 1rem;
}
.stButton>button:hover {
  filter: brightness(1.08);
  transform: translateY(-1px);
}

/* The orb */
.orb {
  width: 200px; height: 200px; margin: 0 auto 1rem auto; border-radius: 50%;
  background: radial-gradient(circle at 30% 30%, #b98bff 0%, #7c4dff 40%, #3b1d78 70%, #1a0e3a 100%);
  box-shadow: 0 0 40px rgba(155, 89, 255, 0.65), inset 0 0 60px rgba(255,255,255,0.10);
  position: relative;
}
.orb::after {
  content: "";
  position: absolute; top: 20px; left: 40px; width: 60px; height: 60px; border-radius: 50%;
  background: radial-gradient(circle, rgba(255,255,255,0.9) 0%, rgba(255,255,255,0.2) 40%, rgba(255,255,255,0) 70%);
  filter: blur(2px);
}

/* Answer card */
.answer {
  background: rgba(255,255,255,0.06);
  border: 1px solid rgba(255,255,255,0.18);
  padding: 1rem 1.1rem;
  border-radius: 14px;
  backdrop-filter: blur(6px);
}
.small {
  opacity: 0.85; font-size: 0.92rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="orb"></div>', unsafe_allow_html=True)
st.markdown("<h1 style='text-align:center;'>🔮 Mystic 8-Ball</h1>", unsafe_allow_html=True)
st.markdown("<p class='small' style='text-align:center;'>Ask a yes-or-no question, then consult the orb.</p>", unsafe_allow_html=True)

# ----- Inputs -----
col1, col2 = st.columns([2,1])
with col1:
  name = st.text_input("Your name", "")
with col2:
  st.write("")  # spacer
  st.write("")

question = st.text_input("Ask the Magic 8-Ball a yes-or-no question:")

# Keep answers in session so they persist after reruns
if "answer" not in st.session_state:
    st.session_state.answer = None
if "answer2" not in st.session_state:
    st.session_state.answer2 = None

# ----- Core answering logic -----
main_answers = [
    'Yes — definitely!',
    'It is decidedly so.',
    'Without a doubt.',
    'Reply hazy, try again.',
    'Ask again later.',
    'Better not tell you now.',
    'My sources say no.',
    'Outlook not so good.',
    'Very doubtful.'
]

followup_answers = [
    "I just know things.",
    "The universe whispers it.",
    "Logic and reason guide me.",
    "It is a mystery even to me.",
    "Because I can see the bigger picture.",
    "Experience tells me so.",
    "Some things cannot be explained.",
    "I read between the lines.",
    "Because patterns repeat themselves."
]

def get_main_answer(q: str) -> str:
    if not q.strip():
        return "The orb is silent. (Ask something first.)"
    roll = random.randint(1, 10)
    if roll == 10:
        # Your custom special line (references the question)
        return f"It remains to be seen if the answer is yes or no to: {q}"
    else:
        return main_answers[(roll - 1) % len(main_answers)]

def get_followup(name: str) -> str:
    # Random reply to "Don't you wonder how I know that?"
    return random.choice(followup_answers)

# ----- Button to consult the orb -----
if st.button("Consult the Orb"):
    st.session_state.answer = get_main_answer(question)
    st.session_state.answer2 = get_followup(name)

# ----- Display answers -----
if st.session_state.answer:
    st.markdown("<div class='answer'>", unsafe_allow_html=True)
    if question.strip():
        st.markdown(f"**You asked:** {question}")
    st.markdown(f"**Magic 8-Ball says:** {st.session_state.answer}")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br/>", unsafe_allow_html=True)
    st.markdown("<div class='answer small'>", unsafe_allow_html=True)
    st.markdown(f"*Don’t you wonder how I know that, {name or 'seeker'}?*")
    st.markdown(f"**Answer:** {st.session_state.answer2}")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br/><div class='small' style='text-align:center; opacity:0.75;'>For fun only ✨</div>", unsafe_allow_html=True)
