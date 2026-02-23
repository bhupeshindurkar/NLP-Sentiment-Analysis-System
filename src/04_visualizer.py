import matplotlib.pyplot as plt
import seaborn as sns
import os

class Visualizer:
    """
    Module for generating and saving visualization charts.
    """
    def __init__(self, output_dir=None):
        if output_dir is None:
            # Default to 'output' directory relative to the project root
            # Assuming the script is in 'src'
            current_dir = os.path.dirname(os.path.abspath(__file__))
            self.output_dir = os.path.join(current_dir, "../output/")
        else:
            self.output_dir = output_dir

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def plot_sentiment_distribution(self, df, filename="sentiment_chart.png"):
        """
        Generates a bar chart showing the distribution of sentiments.
        """
        if 'sentiment_label' not in df.columns:
            print("ERROR: DataFrame does not contain 'sentiment_label' column.")
            return

        plt.figure(figsize=(10, 6))
        sns.set_style("whitegrid")
        
        # Count the occurrences of each label
        ax = sns.countplot(x='sentiment_label', data=df, palette='viridis', order=['Positive', 'Neutral', 'Negative'])
        
        plt.title('Distribution of Sentiment in Product Reviews', fontsize=15)
        plt.xlabel('Sentiment Label', fontsize=12)
        plt.ylabel('Number of Reviews', fontsize=12)
        
        # Add count labels on top of bars
        for p in ax.patches:
            ax.annotate(f'{int(p.get_height())}', (p.get_x()+0.35, p.get_height()+0.1))

        output_path = os.path.join(self.output_dir, filename)
        plt.savefig(output_path)
        plt.close()
        print(f"INFO: Sentiment distribution chart saved to {output_path}")

if __name__ == "__main__":
    import pandas as pd
    # Test data
    df = pd.DataFrame({'sentiment_label': ['Positive', 'Positive', 'Negative', 'Neutral', 'Positive']})
    viz = Visualizer()
    viz.plot_sentiment_distribution(df)
