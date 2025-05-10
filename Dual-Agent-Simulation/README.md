# 🧠 Dual-Agent Simulation: Interviewer + Expert Feedback App

**Path:** [Dual-Agent-Simulation](https://github.com/Bhairavi-avt/Algorithms_DS/tree/main/Dual-Agent-Simulation)

This Streamlit-based application simulates a dynamic multi-agent interaction between:
- 🧑‍💼 **Interviewer**
- 👩‍💻 **Interviewee**
- 👨‍🏫 **Guru (expert judge)**

It serves as a smart roleplay interface to:
- Emulate interview question flow
- Generate expert-level feedback using LLMs
- Provide simulated conversational training

---

## 🎯 Key Features
- ✨ Uses the [Together.ai](https://www.together.ai/) LLM API to power multiple agents  
- 🗣️ Agents include:
  - **Interviewer**: Asks topic-related questions
  - **Interviewee**: Responds as a student or candidate
  - **Guru**: Provides constructive critique + rating
- 📊 Results tab summarizes all questions, answers, feedback, and pass/fail metrics
- ♻️ Supports conversation replay via session history in Streamlit

---

## 🗂️ Project Structure

```bash
Dual-Agent-Simulation/
├── app.py               # Main Streamlit app UI
├── requirements.txt     # Required packages
└── utils/
    ├── helper.py        # LLM interaction logic and API function
  
