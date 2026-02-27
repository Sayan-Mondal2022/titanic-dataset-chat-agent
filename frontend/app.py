import streamlit as st
import requests
import time

# ==============================
# CONFIGURATION
# ==============================

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Titanic Chat Agent",
    page_icon="🚢",
    layout="wide"
)

# ==============================
# CUSTOM CSS
# ==============================

st.markdown("""
<style>
    /* ── Top toolbar buttons ── */
    .top-bar {
        display: flex;
        gap: 10px;
        justify-content: flex-end;
        margin-bottom: 10px;
    }

    /* ── Backend offline card ── */
    .offline-card {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        border: 1px solid #e94560;
        border-radius: 16px;
        padding: 40px;
        text-align: center;
        max-width: 600px;
        margin: 80px auto;
        box-shadow: 0 8px 32px rgba(233, 69, 96, 0.2);
    }
    .offline-icon {
        font-size: 72px;
        margin-bottom: 16px;
    }
    .offline-title {
        color: #e94560;
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 8px;
    }
    .offline-subtitle {
        color: #a0aec0;
        font-size: 1rem;
        margin-bottom: 28px;
    }
    .step-box {
        background: rgba(255,255,255,0.05);
        border-left: 3px solid #e94560;
        border-radius: 8px;
        padding: 12px 16px;
        margin: 8px 0;
        text-align: left;
        color: #e2e8f0;
        font-size: 0.9rem;
    }
    .code-block {
        background: #0d1117;
        border: 1px solid #30363d;
        border-radius: 8px;
        padding: 10px 14px;
        font-family: 'Courier New', monospace;
        color: #79c0ff;
        font-size: 0.85rem;
        margin-top: 6px;
    }
    .pulse-dot {
        display: inline-block;
        width: 12px;
        height: 12px;
        background: #e94560;
        border-radius: 50%;
        margin-right: 8px;
        animation: pulse 1.5s infinite;
    }
    @keyframes pulse {
        0%   { box-shadow: 0 0 0 0 rgba(233,69,96,0.6); }
        70%  { box-shadow: 0 0 0 10px rgba(233,69,96,0); }
        100% { box-shadow: 0 0 0 0 rgba(233,69,96,0); }
    }
</style>
""", unsafe_allow_html=True)


# ==============================
# BACKEND HEALTH CHECK
# ==============================

def is_backend_alive():
    try:
        response = requests.get(f"{BACKEND_URL}/docs", timeout=2)
        return response.status_code == 200
    except:
        return False


# ==============================
# BACKEND OFFLINE PAGE  (improved)
# ==============================

def show_backend_error():

    st.markdown("""
    <div class="offline-card">
        <div class="offline-icon">🔌</div>
        <div class="offline-title">Backend Not Connected</div>
        <div class="offline-subtitle">
            <span class="pulse-dot"></span>
            Unable to reach the FastAPI backend at <code>http://127.0.0.1:8000</code>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("#### 🔎 Possible Reasons")
        st.markdown("""
        <div class="step-box">⚠️ The backend server is <strong>not running</strong></div>
        <div class="step-box">🌐 Wrong backend URL configured in <code>app.py</code></div>
        <div class="step-box">🔒 A firewall or network issue is blocking port <strong>8000</strong></div>
        """, unsafe_allow_html=True)

        st.markdown("#### 🛠️ How to Fix")
        st.markdown("""
        <div class="step-box">
            <strong>Step 1 —</strong> Open a terminal and navigate to your project folder
        </div>
        <div class="step-box">
            <strong>Step 2 —</strong> Start the backend server:
            <div class="code-block">uvicorn backend:app --reload</div>
        </div>
        <div class="step-box">
            <strong>Step 3 —</strong> Wait until you see:<br>
            <div class="code-block">✅  Uvicorn running on http://127.0.0.1:8000</div>
        </div>
        <div class="step-box">
            <strong>Step 4 —</strong> Come back here and click <strong>Retry Connection</strong> below
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("🔄 Retry Connection", use_container_width=True, type="primary"):
            st.rerun()

    st.stop()


# Check backend before loading UI
if not is_backend_alive():
    show_backend_error()


# ==============================
# SESSION STATE INIT
# ==============================

if "messages" not in st.session_state:
    st.session_state.messages = []


# ==============================
# DIALOG — DOCUMENTATION
# ==============================

@st.dialog("📘 Documentation", width="large")
def show_docs_dialog():
    st.markdown("""
    ## 🚢 How to Use the Titanic Chat Agent

    Ask any natural language question about the Titanic passenger dataset —
    the AI agent will analyze the data and respond with insights or visualizations.

    ---

    ### 🔍 Analysis Questions
    These return text-based statistics and summaries:

    | Example Question | What It Does |
    |---|---|
    | *What is the average fare?* | Returns mean ticket price |
    | *How many passengers survived?* | Counts survivors |
    | *What percentage were male?* | Gender distribution |
    | *What was the median age?* | Age statistics |
    | *How many were in 1st class?* | Class breakdown |

    ---

    ### 📊 Visualization Questions
    These generate and display charts inline:

    | Example Question | Chart Type |
    |---|---|
    | *Show histogram of Age* | Histogram |
    | *Plot survival rate by gender* | Bar chart |
    | *Show bar chart of Embarked distribution* | Bar chart |
    | *Visualize fare distribution* | Histogram |

    ---

    ### 💡 Tips
    - You can combine filters: *"What is the average age of female survivors in 1st class?"*
    - Charts are saved per session and viewable via **Show Old Plots**
    - Chat history is preserved within the session; use **Clear Chat** to reset
    - The agent understands synonyms: *"ticket price"* = *"fare"*, *"passed away"* = *"died"*, etc.

    ---

    ### ⚙️ Backend Info
    The app connects to a **FastAPI** backend running locally at `http://127.0.0.1:8000`.
    Make sure it is running before sending queries.
    """)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("✅ Got it, Close", use_container_width=True, type="primary"):
        st.rerun()


# ==============================
# DIALOG — SHOW OLD PLOTS
# ==============================

@st.dialog("🖼️ Previously Generated Plots", width="large")
def show_old_plots_dialog():
    plot_messages = [
        msg for msg in st.session_state.messages
        if msg.get("role") == "assistant" and msg.get("plot") is not None
    ]

    if not plot_messages:
        st.info("📭 No plots have been generated yet in this session. Ask a visualization question to get started!")
    else:
        st.markdown(f"**{len(plot_messages)} plot(s) generated this session:**")
        st.divider()

        for idx, msg in enumerate(reversed(plot_messages), 1):
            with st.expander(f"📊 Plot #{len(plot_messages) - idx + 1}", expanded=(idx == 1)):
                st.image(msg["plot"], use_column_width=True)
                st.caption(f"**Query:** {_find_user_query_for(msg)}")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Close", use_container_width=True):
        st.rerun()


def _find_user_query_for(assistant_msg):
    """Walk backwards through messages to find the user query before this assistant reply."""
    msgs = st.session_state.messages
    try:
        idx = msgs.index(assistant_msg)
        for i in range(idx - 1, -1, -1):
            if msgs[i]["role"] == "user":
                return msgs[i]["content"]
    except ValueError:
        pass
    return "Unknown query"


# ==============================
# MAIN TITLE + TOP ACTION BAR
# ==============================

title_col, btn_col = st.columns([4, 1])

with title_col:
    st.title("🚢 Titanic Dataset Chatbot")
    st.caption("Powered by FastAPI + Groq + LangChain")

with btn_col:
    st.markdown("<br>", unsafe_allow_html=True)
    col_a, col_b, col_c = st.columns(3)

    with col_a:
        if st.button("📘", help="Open Documentation", use_container_width=True):
            show_docs_dialog()

    with col_b:
        plot_count = sum(
            1 for m in st.session_state.messages
            if m.get("role") == "assistant" and m.get("plot") is not None
        )
        label = f"🖼️" if plot_count == 0 else f"🖼️ {plot_count}"
        if st.button(label, help="View previously generated plots", use_container_width=True):
            show_old_plots_dialog()

    with col_c:
        if st.button("🧹", help="Clear chat history", use_container_width=True):
            st.session_state.messages = []
            st.rerun()

st.divider()


# ==============================
# DISPLAY CHAT HISTORY
# ==============================

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg.get("plot"):
            st.image(msg["plot"], width=650)


# ==============================
# USER INPUT
# ==============================

user_input = st.chat_input("Ask a question about the Titanic dataset...")

if user_input:

    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Call backend
    with st.spinner("Analyzing..."):

        answer = "🚨 Unknown error occurred."
        plot_image = None
        is_visualization = False

        try:
            response = requests.post(
                f"{BACKEND_URL}/ask",
                json={"question": user_input},
                timeout=20
            )

            # Bug fix 2: Check HTTP status BEFORE parsing JSON
            if response.status_code != 200:
                answer = f"❌ Backend returned HTTP {response.status_code}: {response.text}"
            else:
                data = response.json()

                if data.get("success"):
                    answer = data["answer"]
                    # Bug fix 1: Only fetch plot if backend signals a plot was generated
                    is_visualization = data.get("has_plot", False)
                else:
                    answer = f"❌ Error: {data.get('error', 'Unknown error')}"

        except requests.exceptions.Timeout:
            answer = "⏱️ Request timed out. The backend took too long to respond."
        except requests.exceptions.ConnectionError:
            answer = "🔌 Could not connect to the backend. Is it still running?"
        except ValueError:
            # Bug fix 3: .json() failed — backend returned non-JSON (e.g. HTML crash page)
            answer = "⚠️ Backend returned an unexpected response format. Check the server logs."
        except Exception as e:
            answer = f"🚨 Unexpected error: {str(e)}"

        # Bug fix 1: Only call /plot when backend confirmed a visualization was made
        if is_visualization:
            try:
                plot_response = requests.get(
                    f"{BACKEND_URL}/plot",
                    timeout=10
                )
                if plot_response.status_code == 200:
                    plot_image = plot_response.content
            except:
                pass

    # Save assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer,
        "plot": plot_image
    })

    st.rerun()


# ==============================
# AUTO SCROLL SCRIPT
# ==============================

st.markdown(
    """
    <script>
        window.scrollTo(0, document.body.scrollHeight);
    </script>
    """,
    unsafe_allow_html=True
)