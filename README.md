This Python project deliverable 1 provides a feature to evaluate the validity of a given URL based on various metrics like domain trust, content relevance, fact-checking, bias, and citation scores.

Features
Fetch Page Content: Extracts text content from the specified URL.
Domain Trust: Evaluates the trustworthiness of the domain (currently uses a placeholder value).
Content Relevance: Measures semantic similarity between the user query and the webpage content using Sentence Transformers.
Fact-Checking: Uses Google Fact Check API to assess the factual accuracy of the content.
Bias Detection: Detects bias using sentiment analysis via the Hugging Face pipeline.
Citation Check: Checks citations for the given URL using a DuckDuckGo search query.
Installation
Prerequisites
Python 3.8 or later.
pip installed on your system.
Install Dependencies
Create a virtual environment:

bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
Install required libraries:

bash
Copy
Edit
pip install -r requirements.txt
Required Libraries
The requirements.txt file includes the following dependencies:

requests
beautifulsoup4
transformers
sentence-transformers
Usage
Clone the repository or copy the code into your project directory.

Run the script with a user query and a URL. Example usage:

python
Copy
Edit
if __name__ == "__main__":
    user_query = "Impact of climate change on agriculture"
    test_url = "https://www.example.com/article-about-agriculture"
    result = rate_url_validity(user_query, test_url)
    print(result)
The output will include:

Domain Trust
Content Relevance
Fact-Check Score
Bias Score
Citation Score
Final Validity Score
How It Works
Fetch Content: Fetches the textual content from the URL using requests and BeautifulSoup.

Domain Trust: Placeholder logic for domain trust; replace with an actual domain trust scoring API if available.

Content Relevance:

Uses Sentence Transformers (all-mpnet-base-v2) to calculate semantic similarity between the user query and webpage content.
Fact-Checking: Calls the Google Fact Check API to cross-verify content.

Bias Detection: Uses cardiffnlp/twitter-roberta-base-sentiment for sentiment analysis to identify bias.

Citation Check: Utilizes DuckDuckGo search queries to estimate citations for the given URL.

Notes
Limitations:

The domain trust metric is currently a placeholder and should be replaced with a robust API.
Citation checking and fact-checking are dependent on external APIs or search results.
Future Enhancements:

Integrate a robust domain authority API.
Improve citation checking mechanisms.
Add more granularity to bias detection.
