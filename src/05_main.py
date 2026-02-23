import os
import sys

# Ensure the current directory is in path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Imports are handled dynamically in the main function to support numeric filenames

# Function name must be valid, but filename starts with numbers. 
# In Python, we can use import_module or just rename files.
# For professional standards, filenames usually don't start with numbers, 
# but I followed the user's specific requested structure.
# I will use a helper to import them if needed, or just import them directly if the environment allows.
# Actually, 'from 01_data_loader' is invalid syntax in Python.
# I should rename the files to valid Python identifiers or use dynamic imports.
# Given the user's request for "clean modular architecture", I'll rename them internally 
# but keep the logic within the requested structure if possible.
# Actually, the user's requested structure is a bit problematic for direct imports.
# I will rename them to: data_loader.py, text_cleaner.py, etc. 
# NO, the user's prompt showed `01_data_loader.py`.
# I'll use `__import__` or `importlib` if I must keep those names.
# Better choice: Rename them to `data_loader.py`, etc., and explain to the user.
# Wait, I can use `importlib.import_module`.

def main():
    print("="*50)
    print("NLP-BASED SENTIMENT ANALYSIS SYSTEM")
    print("="*50)

    # Paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.join(current_dir, "../data/sample_reviews.csv")
    output_txt = os.path.join(current_dir, "../output/results.txt")

    try:
        # Import modules with numeric names using importlib
        import importlib
        dl_mod = importlib.import_module("01_data_loader")
        tc_mod = importlib.import_module("02_text_cleaner")
        sc_mod = importlib.import_module("03_sentiment_core")
        vz_mod = importlib.import_module("04_visualizer")

        DataLoader = dl_mod.DataLoader
        TextCleaner = tc_mod.TextCleaner
        SentimentAnalyzer = sc_mod.SentimentAnalyzer
        Visualizer = vz_mod.Visualizer

        # Initialize modules
        loader = DataLoader(data_file)
        cleaner = TextCleaner()
        analyzer = SentimentAnalyzer()
        viz = Visualizer()

        # Menu for user choice
        print("\nCHOOSE AN OPTION:")
        print("1. Process Sample Reviews (CSV)")
        print("2. Analyze Custom Text (Manual Input)")
        print("3. Exit")
        
        choice = input("\nEnter choice (1-3): ")

        if choice == '1':
            # 1. Load Data
            print("\n[1/5] Loading data...")
            df = loader.load_data()
            if df is None:
                return

            # 2. Preprocess Text
            print("[2/5] Cleaning text...")
            df['cleaned_text'] = df['review_text'].apply(cleaner.clean_text)

            # 3. Sentiment Analysis
            print("[3/5] Analyzing sentiments...")
            results = df['review_text'].apply(analyzer.get_sentiment)
            df['sentiment_score'] = results.apply(lambda x: x['score'])
            df['sentiment_label'] = results.apply(lambda x: x['label'])

            # 4. Save Results
            print("[4/5] Saving results to output/results.txt...")
            with open(output_txt, 'w', encoding='utf-8') as f:
                f.write("SENTIMENT ANALYSIS RESULTS\n")
                f.write("="*30 + "\n\n")
                for _, row in df.iterrows():
                    f.write(f"Review ID: {row.get('review_id', 'N/A')}\n")
                    f.write(f"Original: {row['review_text']}\n")
                    f.write(f"Sentiment: {row['sentiment_label']} (Score: {row['sentiment_score']:.2f})\n")
                    f.write("-" * 20 + "\n")
            
            # 5. Visualize
            print("[5/5] Generating visualization...")
            viz.plot_sentiment_distribution(df)

            print("\n" + "="*50)
            print("PROCESS COMPLETED SUCCESSFULLY!")
            print(f"Results saved in: {output_txt}")
            print(f"Chart saved in: output/sentiment_chart.png")
            print("="*50)

        elif choice == '2':
            user_text = input("\nEnter the review text to analyze: ")
            if user_text.strip():
                # Clean
                cleaned = cleaner.clean_text(user_text)
                # Analyze
                result = analyzer.get_sentiment(user_text) # VADER prefers original text usually
                
                print("\n" + "-"*30)
                print(f"ANALYSIS RESULT:")
                print(f"Sentiment: {result['label']}")
                print(f"Score:     {result['score']:.4f}")
                print("-"*30)
                
                # Append to results.txt
                with open(output_txt, 'a', encoding='utf-8') as f:
                    f.write(f"Manual Input: {user_text}\n")
                    f.write(f"Sentiment: {result['label']} (Score: {result['score']:.2f})\n")
                    f.write("-" * 20 + "\n")
                print("\nResult appended to output/results.txt")
            else:
                print("Empty input. Returning to menu.")

        elif choice == '3':
            print("Exiting system. Goodbye!")
            return
        else:
            print("Invalid choice. Please run again.")

    except Exception as e:
        print(f"\nCRITICAL ERROR in main process: {str(e)}")

if __name__ == "__main__":
    main()
