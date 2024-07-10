import pandas as pd

def remove_redundant_data(input_file, output_file):
    try:
        # Read data from Excel file into DataFrame
        df = pd.read_excel(input_file)

        # Identify and remove redundant data
        df_cleaned = df.drop_duplicates()

        # Write cleaned data to Excel file
        df_cleaned.to_excel(output_file, index=False)
        print("Data cleaning complete. Cleaned data saved to:", output_file)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Input and output file paths
    input_file = r"C:\Users\User\OneDrive\Desktop\Biological marking\before.xlsx"
    output_file = r"C:\Users\User\OneDrive\Desktop\Biological marking\after.xlsx"

    # Call function to remove redundant data
    remove_redundant_data(input_file, output_file)
