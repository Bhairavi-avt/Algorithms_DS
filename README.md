Algorithms_DS/
├── README.md                    
│
├── Dual-Agent-Simulation/
│   ├── app.py
│   ├── requirements.txt
│   └── utils/
│       ├── helper.py
│       └── helper.ipynb
│   └── README.md                
│
├── Final_Project/
│   ├── nypd_crime_analysis.ipynb
│   └── README.md              
│
├── Searchbot/
│   ├── Deliverable1/
│   │   ├── app.py
│   │   ├── deliverable1.py
│   │   ├── image.png
│   │   └── requirements.txt
│   │
│   ├── Deliverable_2/
│   │   ├── Deliverable2.ipynb
│   │   ├── Test_run.ipynb
│   │   ├── sample_csv_bhairavi.csv
│   │   └── requirements.txt
│   │
│   ├── Deliverable3/
│   │   ├── credibility_scorer.ipynb
│   │   ├── hf_credibility_scorer_v2 (1).ipynb
│   │   └── repo_extractor.ipynb
│   │
│   └── README.md                
│
├── Tiny-Troupe/
│   ├── tinyperson.py
│   ├── persona_examples/
│   └── README.md               



# 📊 Algorithms_DS: AI-Powered Projects Collection

This repository contains a collection of modular AI applications and machine learning projects, structured as separate folders with their own deliverables. Each project has its own README file with detailed explanations.

---

## 🔍 [Searchbot](./Searchbot)

Analyze and score the **credibility of URLs** based on:
- Semantic similarity to a user's query
- Domain trust
- Sentiment bias
- Google Scholar citations
- Fact-check presence

Includes a Streamlit app for interactive evaluation.

---

## 🎭 [Tiny-Troupe](./Tiny-Troupe)

An AI-driven simulation of multi-agent personas using TinyPerson. You can create your own personas, place them in an environment, and simulate role-based conversations.

🗣️ Includes multiple simulations such as:
- Lisa Carter (Data Scientist)
- Bhairavi (Grad Student)
- Mike (Professor)

---

## 🤖 [Dual-Agent-Simulation](./Dual-Agent-Simulation)

A two-agent Streamlit app using Hugging Face LLMs to simulate:
- Interviewer + Interviewee + Guru

📁 Structure:
- `app.py`: Streamlit simulation app
- `utils/helper.py`: Core logic for agent interactions

- 
https://huggingface.co/spaces/bhairavee37/Duel-Agent-Simulation
---

## 🕵️‍♂️ [Final_Project – NYC Crime Analysis](./Final_Project)

Using NYPD Arrest Data, this project:
- Uses **supervised ML** to predict **crime severity**
- Uses **unsupervised clustering** to find **crime hotspots**
- Combines spatial and demographic analysis

Notebook: `Algo_for_DS_Final_Projectipynb.ipynb`

---

Each sub-project has its own environment, code, and `README.md`. To run the Streamlit apps, follow setup steps inside their respective folders.

---
