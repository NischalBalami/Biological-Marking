import pandas as pd
from scipy.stats import ttest_ind

def normalize_data(df):
    df['pa_normalized'] = df['pa'] / df['pa'].sum() #Normalizing pa values  #we are divifnig every pa values with sum of the total pa values
    return df

def load_and_normalize(file_path):
    df = pd.read_excel(file_path) #data loading for normalizong
    return normalize_data(df)

def find_significant_features(df1, df2, feature):
    significant_features = []
    for mz in df1['m/z'].unique():
        values1 = df1[df1['m/z'] == mz][feature]
        values2 = df2[df2['m/z'] == mz][feature]
        if len(values1) > 1 and len(values2) > 1:
            t_stat, p_value = ttest_ind(values1, values2)
            if p_value < 0.05:  # update this threshold
                significant_features.append((mz, p_value))
    return significant_features


if __name__ == "__main__":
    healthy_df = load_and_normalize(r"C:\Users\User\OneDrive\Desktop\Biological marking\data\cleaned\healthy_samples.xlsx")
    unhealthy_df = load_and_normalize(r"C:\Users\User\OneDrive\Desktop\Biological marking\data\cleaned\unhealthy_samples.xlsx")
    treated_df = load_and_normalize(r"C:\Users\User\OneDrive\Desktop\Biological marking\data\cleaned\treated_samples.xlsx")



    significant_mz_pa = find_significant_features(healthy_df, unhealthy_df, 'pa_normalized')
    print("Significant m/z values based on peak area (pa):", significant_mz_pa)
