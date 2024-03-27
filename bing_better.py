import requests
from bs4 import BeautifulSoup
from itertools import combinations
from pymongo import MongoClient
client = MongoClient("mongodb+srv://amarnath:scrap3142@cluster0.ipuz3gi.mongodb.net/")
db = client.bingSearch
collection = db.bingSearchData



# url = "https://www.google.com/search?q=Ashutosh Kumar+Fourbrick"
# dUrl = getURL(keywords)
final_combined_data = []
def crawlingProfile(url):
    response = requests.get(url)
    final_data = {}

    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all("li", class_="b_algo")
    for i, result in enumerate(results, start=1):
        # Find the text of the anchor tag inside h2
        h2_text = result.find("h2").find("a").text.strip()
        # Find the text of p tag with class "b_lineclamp2 b_algoSlug"
        p_text = result.find("p", class_="b_algoSlug").text.strip()
        modified_text = p_text.replace("Web", "",1)
        final_data[f"Heading {i}"] = h2_text
        final_data[f"Description {i}"] = modified_text

    final_combined_data.append(final_data)

def generate_permutations_combinations(input_list):
    # Storing combinations with length greater than 2
    result_combinations = []
    for r in range(1, len(input_list) + 1):
        for comb in combinations(input_list, r):
            if len(comb) >= 2:
                result_combinations.append(comb)
    return result_combinations

# Example usage
# input_list = ["Amar Nath", "Microsoft", "CEO"]
# input_list = ["Satya Nadella", "Microsoft", "CEO"]
# input_list = ["Amar Nath", "Google", "CEO"]
input_list = ["Sundar Pichai", "Google", "CEO"]
combinations_list = generate_permutations_combinations(input_list)

def getURL(keywords):
    base_url = "https://www.bing.com/search?q="
    keyword_str = "+".join(keywords)
    return base_url + keyword_str

# Generating URLs using combinations
combinationURL = []
for combination in combinations_list:
    url = getURL(combination)
    combinationURL.append(url)
    print(url)
    crawlingProfile(url)
    
# print(final_data)
datas={"data":final_combined_data}
# print(datas)
# post_id = collection.insert_one(datas).inserted_id
# print("fasdfafasfaf",post_id)


#getting probability of reality
def calculate_probability(data):
    count_ceo = 0
    count_total = 0

    for entry in data.get("data", []):  # Access the "data" key and provide an empty list as default
        if isinstance(entry, dict):
            for key, value in entry.items():
                if isinstance(value, str) and "google" in value.lower():
                    count_total += 1
                    if ("ceo" in value.lower()) and ("sundar" in value.lower() or "pichai" in value.lower() ):
                    # if ("ceo" in value.lower()) and ("amar" in value.lower() or "nath" in value.lower() ):
                        count_ceo += 1

    if count_total == 0:
        return 0  # Return 0 if there are no mentions of Microsoft in the data

    probability = count_ceo / count_total
    return probability

probability = calculate_probability(datas)
# print("Probability that Amar Nath is the CEO of Microsoft:", probability)
print("Probability :", probability)