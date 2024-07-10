import pandas as pd
import logging
import os

def setup_logging():
    log_file = r"C:\Users\User\OneDrive\Desktop\Biological marking\logs\data_cleaning.log"
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

def remove_redundant_data(input_file, output_file, remove_duplicates=True, handle_missing='drop'):
    logging.info(f"Processing file: {input_file}")
    df = pd.read_excel(input_file)
    if remove_duplicates:
        original_row_count = len(df)
        df = df.drop_duplicates()
        removed_duplicates = original_row_count - len(df)
        logging.info(f"Removed {removed_duplicates} duplicate rows.") # removing the duplicates here
    if handle_missing == 'drop':
        original_row_count = len(df)
        df = df.dropna()
        dropped_rows = original_row_count - len(df)
        logging.info(f"Dropped {dropped_rows} rows with missing values.") #dropping the missing values
    elif handle_missing == 'fill':
        df = df.fillna(method='ffill').fillna(method='bfill')
        logging.info("Filled missing values.")  #filling the missing values

    df.to_excel(output_file, index=False)
    logging.info(f"Cleaned data written to: {output_file}")

if __name__ == "__main__":
    setup_logging()

    files = {
        'healthy': {
            'input': r"C:\Users\User\OneDrive\Desktop\Biological marking\data\raw\healthy_samples.xlsx",
            'output': r"C:\Users\User\OneDrive\Desktop\Biological marking\data\cleaned\healthy_samples.xlsx",
        },
        'unhealthy': {
            'input': r"C:\Users\User\OneDrive\Desktop\Biological marking\data\raw\unhealthy_samples.xlsx",
            'output': r"C:\Users\User\OneDrive\Desktop\Biological marking\data\cleaned\unhealthy_samples.xlsx",
        },
        'treated': {
            'input': r"C:\Users\User\OneDrive\Desktop\Biological marking\data\raw\treated_samples.xlsx",
            'output': r"C:\Users\User\OneDrive\Desktop\Biological marking\data\cleaned\treated_samples.xlsx",
        }
    }

    for group in files:
        output_dir = os.path.dirname(files[group]['Output'])
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    for group, paths in files.items():
        remove_redundant_data(paths['input'], paths['output'], remove_duplicates=True, handle_missing='drop')
