🔍 Searchbot: AI-Powered Credibility Evaluation Tool

Searchbot is a modular project that evaluates the credibility of web URLs using a combination of domain trust analysis, semantic similarity, sentiment analysis, citation tracking, and user feedback modeling. The project is divided into 3 structured deliverables with distinct approaches.

📁 Project Structure


![image](https://github.com/user-attachments/assets/670fa3bd-70de-4526-aee7-e8b9f8cfed27)

## 🚀 Deliverable 1: Streamlit Credibility App  
**Path:** [Searchbot/Deliverable1](https://github.com/Bhairavi-avt/Algorithms_DS/tree/main/Searchbot/Deliverable1)

A fully functional Streamlit app to interactively analyze URL credibility.  
Supports:
- ✅ Semantic similarity using Sentence Transformers  
- ✅ Domain trust heuristics  
- ✅ Google fact-check API  
- ✅ Sentiment bias detection  
- ✅ Chatbot-style interaction and star-based rating display

**📄 Key Files:**
- [`app.py`](https://github.com/Bhairavi-avt/Algorithms_DS/blob/main/Searchbot/Deliverable1/app.py): Streamlit dashboard UI  
- [`deliverable1.py`](https://github.com/Bhairavi-avt/Algorithms_DS/blob/main/Searchbot/Deliverable1/deliverable1.py): Core backend logic  
- [`requirements.txt`](https://github.com/Bhairavi-avt/Algorithms_DS/blob/main/Searchbot/Deliverable1/requirements.txt): Package dependencies  
- [`image.png`](https://github.com/Bhairavi-avt/Algorithms_DS/blob/main/Searchbot/Deliverable1/image.png): Screenshot of UI

---

## 🔎 Deliverable 2: URL Validator Class-Based Model  
**Path:** [Searchbot/Deliverable_2](https://github.com/Bhairavi-avt/Algorithms_DS/tree/main/Searchbot/Deliverable_2)

Encapsulates the scoring logic inside a robust class-based architecture (`URLValidator`) with deep API integration.

✨ **Enhancements:**
- BERT-tiny for fake news classification  
- SERP API for citation count from Google Scholar  
- Modular scoring system: content relevance, domain trust, fact-check, bias  
- Generates star rating and reasoning for results

**📄 Key Files:**
- [`Deliverable2.ipynb`](https://github.com/Bhairavi-avt/Algorithms_DS/blob/main/Searchbot/Deliverable_2/Deliverable2.ipynb): Class-based implementation  
- [`Test_run.ipynb`](https://github.com/Bhairavi-avt/Algorithms_DS/blob/main/Searchbot/Deliverable_2/Test_run.ipynb): Execution notebook  
- [`sample_csv_bhairavi.csv`](https://github.com/Bhairavi-avt/Algorithms_DS/blob/main/Searchbot/Deliverable_2/sample_csv_bhairavi.csv): Sample dataset  
- [`requirements.txt`](https://github.com/Bhairavi-avt/Algorithms_DS/blob/main/Searchbot/Deliverable_2/requirements.txt): Dependencies

---

## 🧠 Deliverable 3: Hugging Face Neural Network for Rating Prediction  
**Path:** [Searchbot/Deliverable3](https://github.com/Bhairavi-avt/Algorithms_DS/tree/main/Searchbot/Deliverable3)

A deep learning pipeline trained to predict credibility ratings using:
- Custom labeled datasets scraped from GitHub CSVs  
- BERT + Neural network with dense layers and text embeddings  
- Hybrid inputs: user prompt text + function score  

Includes upload/download integration with Hugging Face Hub for real-time deployment.

**📄 Key Files:**
- [`credibility_scorer.ipynb`](https://github.com/Bhairavi-avt/Algorithms_DS/blob/main/Searchbot/Deliverable3/credibility_scorer.ipynb): Model pipeline  
- [`hf_credibility_scorer_v2.ipynb`](https://github.com/Bhairavi-avt/Algorithms_DS/blob/main/Searchbot/Deliverable3/hf_credibility_scorer_v2%20(1).ipynb): Hugging Face deployment  
- [`repo_extractor.ipynb`](https://github.com/Bhairavi-avt/Algorithms_DS/blob/main/Searchbot/Deliverable3/repo_extractor.ipynb): CSV downloader + merger

---

## 📦 Shared Dependencies
- Python ≥ 3.8  
- `transformers`, `sentence-transformers`, `tensorflow`, `streamlit`, `beautifulsoup4`, `scikit-learn`, `requests`

See [`requirements.txt`](https://github.com/Bhairavi-avt/Algorithms_DS/blob/main/Searchbot/requirements.txt) for global dependencies.

📦 Model Output:

Predicts binary credibility label (High vs Low) based on text + numeric features.

Precision: 80%, Recall: 94% for high-credibility content.

## 🤖 Features Across All Deliverables

Sentence-BERT for semantic similarity.

Fake news classification.

Domain authority mapping.

Fact-checking via Google.

Citation validation via SerpAPI.

Sentiment-based bias scoring.

Streamlit + Hugging Face + TensorFlow integration.




