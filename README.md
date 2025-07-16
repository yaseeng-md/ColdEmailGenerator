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
<pre lang="markdown"> 
```json 
   { "role": "Distribution Manager", 
   "experience": "Proven experience in leading teams, operations, logistics, transportation, retail/wholesale", 
   "skills": [ "TEAM MANAGEMENT", "ENGLISH Language skills", "Dutch language skills (in most instances)", 
   "CHANGE AGILITY", "ANALYTICAL thinking", "NONHIERARCHICAL leadership" ], 
   "description": "As a Distribution Manager, you will be working together with distribution manager colleagues on one of our Omnichannel Distribution Centers (DC) at our European Logistics Center (ELC) across Ham and Laakdal in Belgium. You will lead a team of Coaches (4 to 8 direct reports) who are our first line leaders of our athletes (employees) and drive our ELC purpose." } ```
</pre>

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

### 📧 Sample Generated Email

```text
Subject: Application for Distribution Manager Role at European Logistics Center

Dear Hiring Manager,

I am excited to apply for the Distribution Manager position at your esteemed organization, as advertised. Although my background is in Artificial Intelligence and Machine Learning, I am confident that my skills in team management, analytical thinking, and adaptability make me an ideal candidate for this role.

As a Post Gradation Student in Artificial and Machine Learning at Lovely Professional University, I have developed strong analytical and problem-solving skills, which I believe are essential for a Distribution Manager. My experience as a Machine Learning Intern has taught me the importance of teamwork, leadership, and effective communication. I am eager to leverage these skills in a new challenge and contribute to the success of your team.

I am particularly drawn to this role because of the emphasis on team management, change agility, and non-hierarchical leadership. My research experience, including authoring a paper on "Attention Based Explicit Content Detection - A Transformer-based approach," has honed my ability to work independently and collaboratively. I am excited about the opportunity to lead a team of Coaches and drive the ELC purpose.

While my experience may not be directly related to logistics or distribution, I am a quick learner, and my proficiency in English and basic understanding of Dutch will enable me to communicate effectively with the team. I am confident that my strong work ethic, analytical thinking, and ability to adapt to new situations will make me a valuable asset to your team.

I would like to showcase my capabilities through some of my projects, which demonstrate my ability to work on complex problems and collaborate with others. You can find my projects on GitHub, including:

* Explicit Content Detection: https://github.com/yaseeng-md/Explicit-Content-Detection
* Question and Answering RAGs: https://github.com/yaseeng-md/Question-And-Answering-RAG

These projects demonstrate my ability to design, develop, and implement innovative solutions, which I believe will be beneficial in a Distribution Manager role.

Thank you for considering my application. I would welcome the opportunity to discuss how my skills and experience align with the requirements of this role. Please do not hesitate to contact me if you require any additional information.

Best regards,  
Gandluru Mohammed Yaseen


---

## 📌 Future Improvements

- Email tone customization (formal, friendly, confident)
- Resume parsing support

---

## 🧑‍💻 Contributors

- [Gandluru Mohammed Yaseen](https://github.com/yaseeng-md)

---




