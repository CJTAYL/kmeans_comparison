# Clean data
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
import pandas as pd

def separate_ground_truth(df):
    """
    Function to separate ground truth from dataframe
    """
    ground_truth = df['variety']
    return ground_truth


def scale_data(df):
    """
    Function to scale numerical data
    """
    numeric_columns = df.select_dtypes(include=['float64', 'int']).columns
    categorical_columns = df.select_dtypes(exclude=['float64', 'int']).columns
    ct = ColumnTransformer([
        ('scale', StandardScaler(), numeric_columns)
    ], remainder='drop')

    df_scaled = ct.fit_transform(df)

    df_scaled = pd.DataFrame(df_scaled, columns=numeric_columns.tolist())
    return df_scaled
