# Clean data
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
import pandas as pd

def separate_ground_truth(df):
    """
    Function to separate ground truth from dataframe

    Parameters
    ----------
    df: dataframe
        Dataframe containing true labels of groups (clusters)

    Returns
    ----------
    ground_truth: array-like, (n_samples,)
        Array containing the true labels for each data point
    """
    ground_truth = df['variety']
    return ground_truth


def scale_data(df):
    """
    Function to scale numerical data

    Parameters
    ----------
    df: dataframe
        Dataframe containing true labels of groups (clusters)

    Returns
    ----------
    df_scaled: dataframe
        Dataframe containing scaled values of numeric variables
    """
    numeric_columns = df.select_dtypes(include=['float64', 'int']).columns
    categorical_columns = df.select_dtypes(exclude=['float64', 'int']).columns
    ct = ColumnTransformer([
        ('scale', StandardScaler(), numeric_columns)
    ], remainder='drop')

    df_scaled = ct.fit_transform(df)

    df_scaled = pd.DataFrame(df_scaled, columns=numeric_columns.tolist())
    return df_scaled
