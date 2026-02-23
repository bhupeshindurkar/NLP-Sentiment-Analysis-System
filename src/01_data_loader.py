import pandas as pd
import os

class DataLoader:
    """
    Module to handle data ingestion from CSV files.
    """
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        """
        Loads CSV data into a pandas DataFrame.
        Handles missing values and validates input format.
        """
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Error: The file '{self.file_path}' was not found.")
        
        try:
            # Load CSV
            df = pd.read_csv(self.file_path)
            
            # Basic validation: Check if required column exists
            if 'review_text' not in df.columns:
                raise ValueError("Error: CSV must contain a 'review_text' column.")
            
            # Handle missing values: Drop rows where review_text is NaN
            initial_count = len(df)
            df = df.dropna(subset=['review_text'])
            final_count = len(df)
            
            if initial_count > final_count:
                print(f"INFO: Dropped {initial_count - final_count} rows with missing 'review_text'.")
                
            return df
        except Exception as e:
            print(f"CRITICAL: Failed to load data. {str(e)}")
            return None

if __name__ == "__main__":
    # Test the loader
    loader = DataLoader('../data/sample_reviews.csv')
    data = loader.load_data()
    if data is not None:
        print(f"Successfully loaded {len(data)} reviews.")
        print(data.head())
