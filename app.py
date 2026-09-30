import streamlit as st
import os

st.set_page_config(
    page_title="TalktoAnyDoc",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom CSS ---
st.markdown("""
<style>
    /* Hide Streamlit default header/footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* App background */
    .stApp {
        background-color: #f5f7fa;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e0e0e0;
        padding-top: 1rem;
    }

    /* App title in sidebar */
    .app-title {
        font-size: 22px;
        font-weight: 700;
        color: #1a1a2e;
        margin-bottom: 4px;
    }

    .app-subtitle {
        font-size: 13px;
        color: #6b7280;
        margin-bottom: 24px;
    }

    /* File info card */
    .file-info-card {
        background-color: #f0f4ff;
        border: 1px solid #c7d7fd;
        border-radius: 8px;
        padding: 12px 16px;
        margin-top: 12px;
        font-size: 13px;
        color: #374151;
        line-height: 1.8;
    }

    .file-info-card b {
        color: #1a1a2e;
    }

    /* Chat area */
    .chat-container {
        max-width: 760px;
        margin: 0 auto;
        padding-top: 20px;
    }

    /* User message */
    .msg-user {
        background-color: #1a1a2e;
        color: #ffffff;
        padding: 12px 16px;
        border-radius: 12px 12px 2px 12px;
        margin: 8px 0 8px 80px;
        font-size: 14px;
        line-height: 1.6;
    }

    /* Assistant message */
    .msg-assistant {
        background-color: #ffffff;
        color: #1a1a2e;
        padding: 12px 16px;
        border-radius: 12px 12px 12px 2px;
        margin: 8px 80px 8px 0;
        font-size: 14px;
        line-height: 1.6;
        border: 1px solid #e5e7eb;
    }

    /* Label above messages */
    .msg-label {
        font-size: 11px;
        color: #9ca3af;
        margin-bottom: 2px;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .msg-label-right {
        text-align: right;
        font-size: 11px;
        color: #9ca3af;
        margin-bottom: 2px;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    /* Empty state */
    .empty-state {
        text-align: center;
        color: #9ca3af;
        padding: 60px 20px;
        font-size: 15px;
    }

    .empty-state h3 {
        color: #6b7280;
        font-weight: 500;
        margin-bottom: 8px;
    }

    /* Page heading */
    .page-heading {
        font-size: 20px;
        font-weight: 600;
        color: #1a1a2e;
        margin-bottom: 4px;
    }

    .page-heading-sub {
        font-size: 13px;
        color: #6b7280;
        margin-bottom: 16px;
    }
</style>
""", unsafe_allow_html=True)

# --- Session State ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "file_ready" not in st.session_state:
    st.session_state.file_ready = False

if "file_name" not in st.session_state:
    st.session_state.file_name = ""

# =====================
# SIDEBAR — File Upload
# =====================
with st.sidebar:
    st.markdown('<div class="app-title">TalktoAnyDoc</div>', unsafe_allow_html=True)
    st.markdown('<div class="app-subtitle">Ask questions about any document</div>', unsafe_allow_html=True)

    st.markdown("**Upload Document**")

    uploaded_file = st.file_uploader(
        label="",
        type=["pdf", "docx"],
        help="PDF or DOCX — max 100 MB",
        label_visibility="collapsed"
    )

    MAX_FILE_SIZE_BYTES = 100 * 1024 * 1024

    if uploaded_file is not None:
        if uploaded_file.size > MAX_FILE_SIZE_BYTES:
            st.error(f"File exceeds 100 MB limit ({uploaded_file.size / (1024*1024):.1f} MB).")
            st.session_state.file_ready = False
        else:
            # Save to disk
            uploads_dir = "uploads"
            os.makedirs(uploads_dir, exist_ok=True)
            save_path = os.path.join(uploads_dir, uploaded_file.name)
            with open(save_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            st.session_state.file_ready = True
            st.session_state.file_name = uploaded_file.name

            file_size_mb = uploaded_file.size / (1024 * 1024)
            file_type = uploaded_file.name.rsplit(".", 1)[-1].upper()

            st.markdown(f"""
            <div class="file-info-card">
                <b>{uploaded_file.name}</b><br>
                Type: {file_type} &nbsp;|&nbsp; Size: {file_size_mb:.2f} MB<br>
                Status: Ready
            </div>
            """, unsafe_allow_html=True)

    else:
        st.session_state.file_ready = False

    # Clear chat button
    if st.session_state.chat_history:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Clear conversation", use_container_width=True):
            st.session_state.chat_history = []
            st.rerun()

# =====================
# MAIN — Chat Interface
# =====================
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

if not st.session_state.file_ready:
    st.markdown("""
    <div class="empty-state">
        <h3>No document loaded</h3>
        Upload a PDF or Word file from the sidebar to get started.
    </div>
    """, unsafe_allow_html=True)

else:
    st.markdown(f'<div class="page-heading">Document Chat</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="page-heading-sub">Asking about: {st.session_state.file_name}</div>', unsafe_allow_html=True)

    # Chat history
    if not st.session_state.chat_history:
        st.markdown("""
        <div class="empty-state">
            <h3>Ready to answer questions</h3>
            Type your question below to get started.
        </div>
        """, unsafe_allow_html=True)
    else:
        for message in st.session_state.chat_history:
            if message["role"] == "user":
                st.markdown(f'<div class="msg-label-right">You</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="msg-user">{message["content"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="msg-label">Assistant</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="msg-assistant">{message["content"]}</div>', unsafe_allow_html=True)

    # Chat input
    user_input = st.chat_input("Type your question here...")

    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        placeholder_reply = "AI answer will appear here once Gemini is connected."
        st.session_state.chat_history.append({"role": "assistant", "content": placeholder_reply})

        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
