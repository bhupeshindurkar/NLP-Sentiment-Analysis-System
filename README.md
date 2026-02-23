# NLP-Based Sentiment Analysis System for Product Reviews

## Overview
This is a professional, modular Python-based sentiment analysis system designed to process product reviews. It uses Natural Language Processing (NLP) techniques and the VADER sentiment analysis tool to categorize reviews as **Positive**, **Negative**, or **Neutral**.

## Project Structure
```text
LP-SENTIMENT-ANALYSIS-BHUPESH/
│
├── src/                    # Source code modules
│   ├── 01_data_loader.py    # Data ingestion and validation
│   ├── 02_text_cleaner.py   # Text preprocessing pipeline
│   ├── 03_sentiment_core.py # Core sentiment analysis logic
│   ├── 04_visualizer.py     # Data visualization (charts)
│   └── 05_main.py           # Main integration entry point
│
├── data/                   # Input data files (CSV)
│   └── sample_reviews.csv
│
├── output/                 # Generated results and plots
│   ├── results.txt
│   └── sentiment_chart.png
│
├── docs/                   # Documentation and reports
│   └── project_report.docx
│
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
└── .gitignore              # Files to ignore in Git
```

## Visual Results
The system generates a distribution chart of the sentiments found in the analysis. Below is the generated chart:

![Sentiment Distribution Chart](output/sentiment_chart.png)

## Features
- **Modular Design**: Each component (loading, cleaning, analysis, visualization) is isolated for better maintainability.
- **Robust Cleaning**: Removes stopwords, special characters, and handles lowercase conversion.
- **VADER Sentiment**: Uses the VADER lexicons for high-accuracy sentiment detection on social media/product review text.
- **Visual Insights**: Automatically generates a distribution chart of the results.

## Setup Instructions

### 1. Prerequisites
Ensure you have Python 3.8+ installed.

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python src/05_main.py
```

## Functional Requirements Covered
- [x] Load CSV data using pandas.
- [x] Handle missing values and validate input.
- [x] Clean text (lowercase, punctuation removal, stopwords).
- [x] Tokenization using NLTK.
- [x] Sentiment analysis with polarity scores.
- [x] Visualization of distribution.
- [x] Result saving to text file.

## Project By:
**Bhupesh Indurkar**
