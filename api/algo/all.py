import os
import pandas as pd

script_dir = os.path.dirname(os.path.realpath(__file__))
csv_path = os.path.join(script_dir, '../dataset/finalData.csv')
data = pd.read_csv(csv_path)


def  get_all():
    df_slice = data.head(50)
    data_list = df_slice.to_dict(orient='records')
    return data_list