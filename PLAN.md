# TalktoAnyDoc - Project Plan

## What we are building
A chatbot web app where user uploads a PDF/Word document and asks questions about it.
The AI answers based only on the uploaded document content.

---

## Step-by-Step Plan

### PHASE 1: Project Foundation (Current)
- [x] Step 1: Create project folder structure + Git setup
- [ ] Step 2: Understand Streamlit - build a simple Hello World UI

### PHASE 2: UI Development
- [ ] Step 3: Build file upload page with validation (PDF/DOCX only, max 100MB)
- [ ] Step 4: Build basic chat interface (input box + message display)

### PHASE 3: Document Processing
- [ ] Step 5: Extract text from uploaded PDF file (using PyPDF2)
- [ ] Step 6: Extract text from uploaded DOCX file (using python-docx)

### PHASE 4: AI + RAG Pipeline
- [ ] Step 7: Understand what RAG is (concept + diagram)
- [ ] Step 8: Split document text into chunks (using LangChain)
- [ ] Step 9: Convert chunks to vectors and store in FAISS
- [ ] Step 10: Connect Gemini API - search FAISS + answer question

### PHASE 5: Connect Everything
- [ ] Step 11: Connect UI + document processing + AI into one working app
- [ ] Step 12: Test with a real PDF (insurance doc, any document)
- [ ] Step 13: Fix bugs and edge cases

### PHASE 6: Deliverables
- [ ] Step 14: Architecture diagram
- [ ] Step 15: Unit test documentation
- [ ] Step 16: Presentation (PPT) - Executive Summary, Problem, Solution, Results
- [ ] Step 17: Screen recording / demo video

---

## Project Folder Structure
```
TalktoAnyDoc/
├── app.py               # Main Streamlit app (entry point)
├── utils/
│   ├── doc_loader.py    # Extract text from PDF and DOCX
│   ├── vector_store.py  # FAISS - store and search document chunks
│   └── llm.py           # Gemini API - generate answers
├── uploads/             # Temporarily store uploaded files
├── tests/
│   └── test_cases.md    # Unit test documentation
├── docs/
│   ├── architecture.png # Architecture diagram
│   └── presentation.pptx
├── requirements.txt     # All Python libraries needed
└── PLAN.md              # This file
```

---

## Tech Stack
| Purpose         | Technology              |
|-----------------|------------------------|
| UI              | Streamlit              |
| PDF parsing     | PyPDF2                 |
| DOCX parsing    | python-docx            |
| AI Orchestration| LangChain              |
| Vector Database | FAISS                  |
| LLM             | Gemini API (via HTTP)  |
| Language        | Python                 |

---

## Current Step: Step 1 DONE - Move to Step 2
