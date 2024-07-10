import requests
import pandas as pd
import logging
import json

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def query_hmdb(mz_value, tolerance=0.1):
    url = f"http://www.hmdb.ca/unearth/q?utf8=✓&query={mz_value}&searcher=metabolites"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        logging.error(f"Failed to query HMDB for m/z value {mz_value}")
        return None


def identify_biomarkers(input_file, output_file):
    significant_mz_df = pd.read_excel(input_file)
    results = []
    for index, row in significant_mz_df.iterrows():
        mz = row['m/z']
        p_value = row['p_value']
        response = query_hmdb(mz)
        if response:
            results.append({
                'm/z': mz,
                'p_value': p_value,
                'hmdb_response': response
            })
    df_results = pd.DataFrame(results)
    df_results.to_excel(output_file, index=False)
    logging.info(f"Biomarker identification results saved to {output_file}")


if __name__ == "__main__":
    # Load configuration
    with open('../config.json') as config_file:
        config = json.load(config_file)

    input_file = "../data/results/significant_mz_values.xlsx"
    output_file = "../data/results/biomarker_identification_results.xlsx"

    identify_biomarkers(input_file, output_file)
