import streamlit as st

# Page config — like setting the browser tab title and layout
st.set_page_config(
    page_title="TalktoAnyDoc",
    page_icon="📄",
    layout="centered"
)

# Title and subtitle
st.title("📄 TalktoAnyDoc")
st.subheader("Chat with your PDF or Word document using AI")

st.divider()

# Simple status message to confirm app is running
st.success("✅ App is running! Streamlit is working correctly.")

st.markdown("""
### What this app will do:
1. **Upload** a PDF or DOCX file
2. **Ask** any question about the document
3. **Get** an AI-powered answer based only on your document

---
*Step 2 complete — Hello World UI is working.*
""")
