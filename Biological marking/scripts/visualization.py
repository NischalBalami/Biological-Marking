import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def visualize_pca(df, title):
    pca = PCA(n_components=2)
    components = pca.fit_transform(df[['m/z', 'rt', 'pa_normalized']])
    plt.scatter(components[:, 0], components[:, 1])
    plt.title(title)
    plt.xlabel('PCA Component 1')
    plt.ylabel('PCA Component 2')
    plt.show()

if __name__ == "__main__":
    healthy_df = pd.read_excel(r"C:\path\to\cleaned\healthy_samples_cleaned.xlsx")
    unhealthy_df = pd.read_excel(r"C:\path\to\cleaned\unhealthy_samples_cleaned.xlsx")
    treated_df = pd.read_excel(r"C:\path\to\cleaned\treated_samples_cleaned.xlsx")

    visualize_pca(healthy_df, 'Healthy Samples PCA')
    visualize_pca(unhealthy_df, 'Unhealthy Samples PCA')
    visualize_pca(treated_df, 'Treated Samples PCA')
