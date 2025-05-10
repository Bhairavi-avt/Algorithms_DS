🔍 Searchbot: AI-Powered Credibility Evaluation Tool

Searchbot is a modular project that evaluates the credibility of web URLs using a combination of domain trust analysis, semantic similarity, sentiment analysis, citation tracking, and user feedback modeling. The project is divided into 3 structured deliverables with distinct approaches.

📁 Project Structure
![image](https://github.com/user-attachments/assets/670fa3bd-70de-4526-aee7-e8b9f8cfed27)

🚀 Deliverable 1: Streamlit Credibility App

Path: Deliverable1/

A fully functional Streamlit app to interactively analyze URL credibility.

Supports semantic similarity via sentence transformers, domain trust heuristics, fact-checking via Google API, and sentiment bias checks.

Shows results with star ratings and chatbot-style interaction.

🔧 Key files:

app.py: Streamlit dashboard UI.

deliverable1.py: Core logic.

requirements.txt: Dependencies.

🔎 Deliverable 2: URL Validator Class-Based Model

Path: Deliverable_2/

A class-based architecture (URLValidator) encapsulating credibility scoring.

Adds deeper citation checks via SERP API + robust bias detection + domain trust heuristics.

Uses BERT-tiny for fake news detection.

📊 Enhancements:

Structured explanations of final scores.

Modular method calls for each credibility dimension.

📁 Key files:

Deliverable2.ipynb: Core code logic.

Test_run.ipynb: Usage testing.

sample_csv_bhairavi.csv: Example input.

🧠 Deliverable 3: Feedback-Driven Credibility Classifier (ML Model)

Path: Deliverable3/

Uses a hybrid neural network combining:

User prompt (BERT-embedded text input)

Numerical rating inputs (functionality)

Trained on real CSVs collected from 15+ classmates via GitHub.

Uploaded final trained model + tokenizer to Hugging Face Hub.

🧩 Components:

hf_credibility_scorer_v2.ipynb: Builds the NN classifier and uploads to Hugging Face.

repo_extractor.ipynb: Pulls and cleans external data from multiple GitHub repos.

credibility_scorer.ipynb: Experimentation and visualization of results.

📦 Model Output:

Predicts binary credibility label (High vs Low) based on text + numeric features.

Precision: 80%, Recall: 94% for high-credibility content.

🤖 Features Across All Deliverables

Sentence-BERT for semantic similarity.

Fake news classification.

Domain authority mapping.

Fact-checking via Google.

Citation validation via SerpAPI.

Sentiment-based bias scoring.

Streamlit + Hugging Face + TensorFlow integration.

📎 Useful Links

🧪 Hugging Face Model: My-TF-NN-Model-v2

🌐 GitHub Repository: Algorithms_DS > Searchbot
