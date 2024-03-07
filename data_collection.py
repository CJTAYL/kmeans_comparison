import pandas as pd

raw_url = 'https://raw.githubusercontent.com/CJTAYL/kmeans_comparison/main/data/seeds_dataset.txt'

def fetch_seeds_data():
    """
    Function to retrieve seeds dataset from GitHub repository

    Parameters
    ----------
    None:

    Returns
    Dataframe: dataframe
        Dataframe containing information about the geometric properties of three varieties of wheat seeds
    """
    # Use pandas to read text file with whitespace delimiter
    try:
        df = pd.read_csv(raw_url, delim_whitespace=True, header=None)
        # Rename columns
        df.columns = ['area', 'perimeter', 'compactness', 'length', 'width', 'asymmetry', 'groove', 'variety']
        # Convert 'type' to a categorical type
        df['variety'] = df['variety'].astype('category')
        return df
    except Exception as e:
        print(f'Error reading data from url: {e}')
