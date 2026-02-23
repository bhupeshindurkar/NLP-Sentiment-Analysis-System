 Project Files Structure:
text
LP-SENTIMENT-ANALYSIS-BHUPESH/
│
├── src/
│   ├── 01_data_loader.py
│   ├── 02_text_cleaner.py
│   ├── 03_sentiment_core.py
│   ├── 04_visualizer.py
│   └── 05_main.py
│
├── data/
│   ├── sample_reviews.csv
│   └── test_inputs.txt
│
├── output/
│   ├── results.txt
│   └── sentiment_chart.png
│
├── docs/
│   └── project_report.docx
│
├── requirements.txt
├── README.md
└── .gitignore


Functional Requirements:

Data Loader Module

Load CSV data using pandas

Handle missing values

Validate input format

Text Cleaner Module

Convert text to lowercase

Remove punctuation and special characters

Remove stopwords

Perform tokenization

Sentiment Core Module

Implement sentiment analysis using:

TextBlob OR

VADER (NLTK) OR

Machine Learning (Logistic Regression / Naive Bayes)

Return polarity score and sentiment label (Positive / Negative / Neutral)

Visualizer Module

Generate sentiment distribution chart using matplotlib or seaborn

Save output as sentiment_chart.png

Main Module

Integrate all modules

Accept user input from terminal

Save results to results.txt

 Project By:
   Bhupesh Indurkar