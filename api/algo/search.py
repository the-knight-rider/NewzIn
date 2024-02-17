import os
import pandas as pd

script_dir = os.path.dirname(os.path.realpath(__file__))
csv_path = os.path.join(script_dir, '../dataset/finalData.csv')
data = pd.read_csv(csv_path)

def search_news(keywords):
    relevant_articles = []

   
    keywords = keywords.lower()

    for index, row in data.iterrows():
        headline = row["title"].lower()  

        if all(keyword in headline for keyword in keywords.split()):
            relevant_articles.append({
                "source_name": row["source_name"],
                "author": row["author"],
                "title": row["title"],
                "description": row["description"],
                "url": row["url"],
                "url_to_image": row["url_to_image"],
                "published_at": row["published_at"],
                "category": row["category"],
                "full_content": row["full_content"]
            })
    
    return relevant_articles


def mySearch(query):
    
    rel_art = search_news(query)
    return rel_art