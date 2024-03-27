import requests
import itertools
from pymongo import MongoClient
client = MongoClient("mongodb+srv://amarnath:scrap3142@cluster0.ipuz3gi.mongodb.net/")
db = client.googleSearch
collection = db.googleSearchData
from bs4 import BeautifulSoup
from itertools import combinations
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
}  # Adding user-agent to avoid bot detection

#Performing Crawling
final_combined_data = []
def crawlingProfile(url):
    response = requests.get(url, headers=headers)
    final_data = {}

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all("div", class_="MjjYud")

        for i, result in enumerate(results, start=1):
            desc = result.find_all("div", class_="VwiC3b yXK7lf lVm3ye r025kc hJNv6b Hdw6tb")
            for data in desc:
                description = data.text
                desc_data = data.find_all("span")
                for span in desc_data:
                    description += span.text
                final_data[f"Description {i}"] = description


    # else:
    #     print("Failed to retrieve the page. Status code:", response.status_code)
        
    final_combined_data.append(final_data)



def generate_google_search_url(operator, keywords):
    encoded_keywords = '+'.join(keywords)
    search_url = f"https://www.google.com/search?q={operator}%3A{encoded_keywords}"
    return search_url

# keywords = ["Sundar Pichai", "Google", "CEO"]
keywords = ["Amar Nath", "Fourbrick", "Software Engineer"]
operators = ["intitle", "site", "inurl", "intext"]
combinationURL = []

for operator in operators:
    # Generate Google search URLs for each combination of keywords
    for i in range(2, len(keywords) + 1):
        combinations = itertools.combinations(keywords, i)
        
        for combo in combinations:
            combinationURL.append(generate_google_search_url(operator, combo))
            
for url in combinationURL:
    print(url)
    crawlingProfile(url)
    
    
# print(final_data)
datas={"data":final_combined_data}
post_id = collection.insert_one(datas).inserted_id
print("fasdfafasfaf",post_id)
#getting probability of reality
def calculate_probability(data,keywords):
    count_ceo = 0
    count_total = 0
    fullName = keywords[0].lower()
    firstName, lastName = fullName.split()
    company = keywords[1].lower()
    position = keywords[2].lower()
    print(firstName,lastName,company,position)
    for entry in data.get("data", []):  # Access the "data" key and provide an empty list as default
        if isinstance(entry, dict):
            for key, value in entry.items():
                if isinstance(value, str) and company in value.lower():
                    count_total += 1
                    if (position in value.lower()) and (firstName in value.lower() or lastName in value.lower() ):
                    # if ("ceo" in value.lower()) and ("amar" in value.lower() or "nath" in value.lower() ):
                        count_ceo += 1

    if count_total == 0:
        return 0  # Return 0 if there are no mentions of Microsoft in the data

    probability = count_ceo / count_total
    return probability

probability = calculate_probability(datas,keywords)
# print("Probability that Amar Nath is the CEO of Microsoft:", probability)
print("Percentage of Reality :", probability*100, "%")
