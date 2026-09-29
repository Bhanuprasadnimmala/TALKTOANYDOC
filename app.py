import streamlit as st
import os

# Page config
st.set_page_config(
    page_title="TalktoAnyDoc",
    page_icon="📄",
    layout="centered"
)

st.title("📄 TalktoAnyDoc")
st.subheader("Chat with your PDF or Word document using AI")

st.divider()

# --- File Upload Section ---
st.header("Upload your document")

uploaded_file = st.file_uploader(
    label="Choose a PDF or Word file",
    type=["pdf", "docx"],          # Only allow PDF and DOCX
    help="Supported formats: PDF, DOCX | Max size: 100MB"
)

MAX_FILE_SIZE_MB = 100
MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024

if uploaded_file is not None:

    # Validate file size
    file_size_bytes = uploaded_file.size
    file_size_mb = file_size_bytes / (1024 * 1024)

    if file_size_bytes > MAX_FILE_SIZE_BYTES:
        st.error(f"❌ File too large: {file_size_mb:.1f} MB. Maximum allowed is {MAX_FILE_SIZE_MB} MB.")

    else:
        # Show file details
        st.success(f"✅ File uploaded successfully!")

        col1, col2, col3 = st.columns(3)
        col1.metric("File Name", uploaded_file.name)
        col2.metric("File Type", uploaded_file.type.split("/")[-1].upper())
        col3.metric("File Size", f"{file_size_mb:.2f} MB")

        # Save file to uploads/ folder
        uploads_dir = "uploads"
        os.makedirs(uploads_dir, exist_ok=True)
        save_path = os.path.join(uploads_dir, uploaded_file.name)

        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.info(f"📁 Saved to: `{save_path}`")

        # Placeholder for next steps
        st.divider()
        st.header("Ask a question")
        st.text_input("Your question about the document:", placeholder="e.g. What is the main topic of this document?", disabled=True)
        st.caption("⏳ AI answering will be connected in a later step.")

else:
    st.warning("⬆️ Please upload a PDF or DOCX file to get started.")
