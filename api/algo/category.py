import os
import pandas as pd

script_dir = os.path.dirname(os.path.realpath(__file__))
csv_path = os.path.join(script_dir, '../dataset/finalData.csv')
data = pd.read_csv(csv_path)

def get_cat(keywords):
   
    keywords_lower = [kw.lower() for kw in keywords]

   
    relevant_articles = data[data["category"].str.contains('|'.join(keywords_lower), case=False, na=False)]

   
    relevant_articles_list = relevant_articles.to_dict(orient='records')

    return relevant_articles_list

    
    


def myCategory(query):
     
    my_cat_art = get_cat(query)
    return my_cat_art