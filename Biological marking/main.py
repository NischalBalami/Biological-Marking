import pandas as pd
from scripts.data_cleaning import remove_redundant_data
from scripts.data_analysis import find_significant_features
from scripts.biomarker_identification import identify_biomarkers
from scripts.visualization import visualize_pca

def main():
    # Define paths
    data_paths = {
        'healthy': 'data/raw/healthy_samples.xlsx',
        'unhealthy': 'data/raw/unhealthy_samples.xlsx',
        'treated': 'data/raw/treated_samples.xlsx'
    }
    cleaned_data_paths = {
        'healthy': 'data/cleaned/healthy_samples_cleaned.xlsx',
        'unhealthy': 'data/cleaned/unhealthy_samples_cleaned.xlsx',
        'treated': 'data/cleaned/treated_samples_cleaned.xlsx'
    }
    significant_mz_file = 'data/results/significant_mz_values.xlsx'
    biomarker_results_file = 'data/results/biomarker_identification_results.xlsx'

    # Clean and normalize data
    remove_redundant_data(data_paths['healthy'], cleaned_data_paths['healthy'])
    remove_redundant_data(data_paths['unhealthy'], cleaned_data_paths['unhealthy'])
    remove_redundant_data(data_paths['treated'], cleaned_data_paths['treated'])

    # Perform statistical analysis
    find_significant_features(cleaned_data_paths['healthy'], cleaned_data_paths['unhealthy'], significant_mz_file)

    # Identify biomarkers
    identify_biomarkers(significant_mz_file, biomarker_results_file)

    # Visualize PCA
    healthy_df = pd.read_excel(cleaned_data_paths['healthy'])
    unhealthy_df = pd.read_excel(cleaned_data_paths['unhealthy'])
    treated_df = pd.read_excel(cleaned_data_paths['treated'])

    visualize_pca(healthy_df, title='Healthy Samples PCA')
    visualize_pca(unhealthy_df, title='Unhealthy Samples PCA')
    visualize_pca(treated_df, title='Treated Samples PCA')

if __name__ == "__main__":
    main()
