# 🤖 ColdEmailGenerator – AI-Powered Cold Email Automation

ColdEmailGenerator is an intelligent system that helps job seekers automatically generate **personalized cold emails** for job applications using **LLMs**, **vector search**, and a lightweight web frontend.

---

## 🚀 Features

- 🔍 Extracts job details like skills, tech stack, and requirements from job postings
- 🧠 Matches job postings with your projects and experience using semantic search
- 📧 Generates tailored cold emails with LLaMA 3B (locally hosted model)
- 🧾 Clean UI for inputting data and generating emails (built with **StreamLit**)

---

<img src="https://github.com/yaseeng-md/ColdEmailGenerator/blob/main/data/Workflow.png" alt="App Screenshot" width="600"/>


## 🧭 Workflow Overview

1. **User Profile Ingestion**
   - The user submits personal details, GitHub links, and project information.
   - Data is embedded and stored in a **vector database (Chroma)**.

2. **Job Posting Input**
   - A new job listing is provided to the system.
   - Could be raw text or pasted from job boards (e.g., LinkedIn, Indeed).

3. **Job Information Extraction**
   - An **LLM** parses the job description to extract:
     - 🔧 Skills
     - 💼 Role
     - 💰 Pay
     - 📚 Experience
     - 🛠️ Tech Stack

4. **Semantic Matching**
   - The system uses Chroma DB to match relevant user projects and skills to the job.

5. **Email Generation**
   - A tailored email is generated using the **LLaMA 3B** model (persistent and locally hosted).
   - The result is a **personalized, professional, and role-aligned cold email.**

6. **Frontend UI**
   - A simple, responsive UI built using **Streamlit** for:
     - Inputting user data
     - Uploading job descriptions
     - Displaying the generated email

---

## 🛠️ Tech Stack

| Component        | Technology                      |
|------------------|----------------------------------|
| Frontend         | [Stralit](https://github.com/stralit/stralit) |
| LLM Inference    | LLaMA 3B |
| Vector DB        | Chroma                          |
| Embedding Model  | Sentence Transformers|
| Job Info Parsing | LLM (LLaMA)  |
| Backend Orchestration | Python / Streamlit            |

---

## Result:

<img src="https://github.com/yaseeng-md/ColdEmailGenerator/blob/main/data/Result.png" alt="App Screenshot" width="600"/>


---

## 📌 Future Improvements

- Email tone customization (formal, friendly, confident)
- Resume parsing support

---

## 🧑‍💻 Contributors

- [Gandluru Mohammed Yaseen](https://github.com/yaseeng-md)

---




