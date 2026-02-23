from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import os
import sys
import importlib

# Add current dir to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)
CORS(app)

# Ensure NLTK data is downloaded on server start
try:
    import nltk
    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('punkt_tab')
    nltk.download('vader_lexicon')
except Exception as e:
    print(f"NLTK Download error: {e}")

# Import our modular logic
tc_mod = importlib.import_module("02_text_cleaner")
sc_mod = importlib.import_module("03_sentiment_core")

cleaner = tc_mod.TextCleaner()
analyzer = sc_mod.SentimentAnalyzer()

# HTML Template with Premium Design (Glassmorphism, Animations, Dark Mode)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sentiment AI | Product Review Insights</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #6366f1;
            --primary-glow: rgba(99, 102, 241, 0.5);
            --bg: #0f172a;
            --card-bg: rgba(30, 41, 59, 0.7);
            --text: #f8fafc;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Outfit', sans-serif;
        }

        body {
            background: radial-gradient(circle at top right, #1e1b4b, #0f172a, #000);
            color: var(--text);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow-x: hidden;
        }

        .container {
            width: 90%;
            max-width: 800px;
            padding: 40px;
            background: var(--card-bg);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 24px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            animation: fadeIn 0.8s ease-out;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        h1 {
            font-size: 2.5rem;
            font-weight: 600;
            margin-bottom: 10px;
            background: linear-gradient(to right, #818cf8, #c084fc);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
        }

        p.subtitle {
            text-align: center;
            color: #94a3b8;
            margin-bottom: 30px;
        }

        .input-group {
            position: relative;
            margin-bottom: 25px;
        }

        textarea {
            width: 100%;
            height: 150px;
            background: rgba(15, 23, 42, 0.5);
            border: 2px solid rgba(255, 255, 255, 0.05);
            border-radius: 16px;
            padding: 20px;
            color: white;
            font-size: 1.1rem;
            resize: none;
            transition: all 0.3s ease;
            outline: none;
        }

        textarea:focus {
            border-color: var(--primary);
            box-shadow: 0 0 20px var(--primary-glow);
        }

        button {
            width: 100%;
            padding: 16px;
            background: linear-gradient(135deg, #6366f1, #a855f7);
            border: none;
            border-radius: 12px;
            color: white;
            font-size: 1.1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(99, 102, 241, 0.4);
        }

        button:active { transform: translateY(0); }

        #result {
            margin-top: 30px;
            padding: 20px;
            border-radius: 16px;
            display: none;
            text-align: center;
            animation: slideIn 0.5s ease-out;
        }

        @keyframes slideIn {
            from { opacity: 0; filter: blur(5px); }
            to { opacity: 1; filter: blur(0); }
        }

        .sentiment-card {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .label {
            font-size: 1.5rem;
            font-weight: 600;
            padding: 8px 20px;
            border-radius: 50px;
            display: inline-block;
            margin: 0 auto;
        }

        .score-bar-bg {
            width: 100%;
            height: 8px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            margin-top: 15px;
            overflow: hidden;
        }

        .score-bar-fill {
            height: 100%;
            width: 0%;
            transition: width 1s cubic-bezier(0.4, 0, 0.2, 1);
        }

        .Positive { background: rgba(34, 197, 94, 0.2); color: #4ade80; border: 1px solid #22c55e; }
        .Negative { background: rgba(239, 68, 68, 0.2); color: #f87171; border: 1px solid #ef4444; }
        .Neutral { background: rgba(100, 116, 139, 0.2); color: #94a3b8; border: 1px solid #64748b; }

        .loader {
            display: none;
            width: 30px;
            height: 30px;
            border: 3px solid rgba(255, 255, 255, 0.1);
            border-radius: 50%;
            border-top-color: var(--primary);
            animation: spin 1s linear infinite;
            margin: 20px auto;
        }

        @keyframes spin { to { transform: rotate(360deg); } }
    </style>
</head>
<body>
    <div class="container">
        <h1>Sentiment AI</h1>
        <p class="subtitle">Experience real-time NLP analysis for your product reviews</p>
        
        <div class="input-group">
            <textarea id="reviewInput" placeholder="Enter your product review here... (e.g., 'This product is absolutely amazing and I love the quality!')"></textarea>
        </div>
        
        <button onclick="analyzeSentiment()">Analyze Sentiment</button>
        
        <div class="loader" id="loader"></div>
        
        <div id="result">
            <div class="sentiment-card">
                <div id="sentimentLabel" class="label">Neutral</div>
                <p id="sentimentScoreText" style="color: #94a3b8; margin-top: 10px;">Confidence Score: 0.00</p>
                <div class="score-bar-bg">
                    <div id="scoreBarFill" class="score-bar-fill"></div>
                </div>
            </div>
        </div>

        <div style="margin-top: 40px; text-align: center; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 20px;">
            <p style="color: #64748b; font-size: 0.9rem; letter-spacing: 1px;">
                DEVELOPED BY <span style="color: #818cf8; font-weight: 600;">BHUPESH INDURKAR</span>
            </p>
        </div>
    </div>

    <script>
        async function analyzeSentiment() {
            const text = document.getElementById('reviewInput').value;
            if (!text.trim()) return alert("Please enter some text!");

            const resultDiv = document.getElementById('result');
            const loader = document.getElementById('loader');
            const labelEl = document.getElementById('sentimentLabel');
            const scoreText = document.getElementById('sentimentScoreText');
            const barFill = document.getElementById('scoreBarFill');

            // Reset
            resultDiv.style.display = 'none';
            loader.style.display = 'block';

            try {
                const response = await fetch('/analyze', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ text })
                });
                
                const data = await response.json();
                
                setTimeout(() => {
                    loader.style.display = 'none';
                    resultDiv.style.display = 'block';
                    
                    labelEl.innerText = data.label;
                    labelEl.className = 'label ' + data.label;
                    scoreText.innerText = `Sentiment Polarity: ${data.score.toFixed(4)}`;
                    
                    // Progress bar logic (map -1 to 1 into 0% to 100%)
                    const percentage = ((data.score + 1) / 2) * 100;
                    barFill.style.width = percentage + '%';
                    
                    if(data.label === 'Positive') barFill.style.background = '#4ade80';
                    else if(data.label === 'Negative') barFill.style.background = '#f87171';
                    else barFill.style.background = '#94a3b8';
                }, 600);

            } catch (error) {
                alert("Server error. Make sure Python app is running!");
                loader.style.display = 'none';
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    text = data.get('text', '')
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400
        
    cleaned = cleaner.clean_text(text)
    result = analyzer.get_sentiment(text) # VADER works better with original text
    
    return jsonify({
        'label': result['label'],
        'score': result['score'],
        'cleaned': cleaned
    })

if __name__ == '__main__':
    print("Web server starting at http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
