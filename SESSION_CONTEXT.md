# TalktoAnyDoc - Full Session Context
## Use this to resume the project in a new Claude session

---

## Assignment Summary
Building a chatbot called "TalktoAnyDoc" for Cognizant OJT evaluation.
- User uploads a PDF or Word document
- User asks questions about the document
- AI answers based only on the uploaded document
- This is called RAG (Retrieval-Augmented Generation)

## OJT Evaluation Details
- Course: GEN AI BASED LLM APP DEVELOPMENT - AWS BEDROCK [201-INTERMEDIATE]
- Attempts Remaining: 2 (used 1 already by mistake)
- After clicking START: must upload + schedule Teams meeting within 12 hours
- Benchmark score: 60/100 to pass
- DO NOT click START until everything is 100% ready

## Deliverables Needed
1. Working application code
2. Architecture diagram
3. Video recording / demo
4. Unit test documentation
5. Presentation (PPT) with: Executive Summary, Problem Statement, Solution/Approach, Execution, Results, Conclusion

---

## Tech Stack Decided
| Purpose          | Technology             |
|------------------|------------------------|
| UI               | Streamlit              |
| PDF parsing      | PyPDF2                 |
| DOCX parsing     | python-docx            |
| AI Orchestration | LangChain              |
| Vector Database  | FAISS                  |
| LLM              | Gemini API (via HTTP)  |
| Language         | Python 3.14            |

## Why these choices
- No OpenAI API (paid) — using Gemini free tier instead
- No AWS Bedrock (no access) — Gemini works fine, assignment allows any tech
- Gemini API key is working (raw HTTP calls, SSL bypass for corporate network)
- FAISS chosen over Pinecone (local, free, no account needed)

---

## Project Location
`C:\Users\2402069\TalktoAnyDoc\`

## Project Structure
```
TalktoAnyDoc/
├── app.py               ← Main Streamlit app (entry point)
├── utils/
│   ├── doc_loader.py    ← Extract text from PDF and DOCX
│   ├── vector_store.py  ← FAISS - store and search document chunks
│   └── llm.py           ← Gemini API - generate answers
├── uploads/             ← Temporarily store uploaded files
├── tests/
│   └── test_cases.md    ← Unit test documentation
├── docs/
│   ├── architecture.png ← Architecture diagram
│   └── presentation.pptx
├── requirements.txt     ← All Python libraries needed
├── PLAN.md              ← Step by step plan
└── SESSION_CONTEXT.md   ← This file
```

---

## Step by Step Plan
### PHASE 1: Project Foundation
- [x] Step 1: Create project folder structure + Git setup ← DONE
- [ ] Step 2: Understand Streamlit - build simple Hello World UI ← NEXT

### PHASE 2: UI Development
- [ ] Step 3: Build file upload page with validation (PDF/DOCX only, max 100MB)
- [ ] Step 4: Build basic chat interface (input box + message display)

### PHASE 3: Document Processing
- [ ] Step 5: Extract text from uploaded PDF (PyPDF2)
- [ ] Step 6: Extract text from uploaded DOCX (python-docx)

### PHASE 4: AI + RAG Pipeline
- [ ] Step 7: Understand RAG concept
- [ ] Step 8: Split document text into chunks (LangChain)
- [ ] Step 9: Convert chunks to vectors and store in FAISS
- [ ] Step 10: Connect Gemini API - search FAISS + answer question

### PHASE 5: Connect Everything
- [ ] Step 11: Connect UI + document processing + AI into one working app
- [ ] Step 12: Test with a real document
- [ ] Step 13: Fix bugs and edge cases

### PHASE 6: Deliverables
- [ ] Step 14: Architecture diagram
- [ ] Step 15: Unit test documentation
- [ ] Step 16: Presentation PPT
- [ ] Step 17: Screen recording / demo video

---

## Gemini API Details
- API Key is working (stored in genAI_demo.py in Downloads)
- SSL bypass needed for corporate network:
  `ssl._create_default_https_context = ssl._create_unverified_context`
- Working model: gemini-3.5-flash
- Backup models: gemini-3.5-flash-lite, gemini-3.7-flash, gemini-3.6-flash
- API call is raw HTTP (no Google SDK) because corporate network blocks SDK

## Known Issues / Gotchas
- Corporate network (Cognizant) blocks SSL — always add SSL bypass
- API keys show as AQ. prefix in browser (DLP masking) — key still works in code
- Run Streamlit with `streamlit run app.py` NOT `python app.py`
- Unicode error when printing special chars — use `.encode("ascii", "ignore").decode()`
- gemini-2.0-flash and gemini-2.5-flash are deprecated — use gemini-3.5-flash

---

## Associate Background
- Works on Java Spring Boot + Angular (FSE)
- Python basics only
- No prior GenAI hands-on
- Explain concepts using Java/Angular comparisons where possible

---

## How to Resume in New Session
Paste this into the new Claude session:

"I am building a TalktoAnyDoc project for my Cognizant OJT evaluation.
Please read C:\Users\2402069\TalktoAnyDoc\SESSION_CONTEXT.md for full context.
We have completed Step 1 (project structure + git).
Next step is Step 2: Build a simple Streamlit Hello World UI in app.py.
Please continue from where we left off, going step by step."
