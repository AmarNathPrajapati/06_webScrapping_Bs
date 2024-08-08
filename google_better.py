# import requests
# from bs4 import BeautifulSoup

# # url = "https://www.google.com/search?q=amarnath+prajapati"
# url = "https://www.google.com/search?q=amarnath+prajapati"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
# }  # Adding user-agent to avoid bot detection

# response = requests.get(url, headers=headers)
# final_data = {}
# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html.parser')
#     results = soup.find_all("div", class_="MjjYud")
#     i = 1
#     for result in results:
#         h3_tags = result.find_all("h3", class_="LC20lb MBeuO DKV0Md")
#         for h3_tag in h3_tags:
#             print(i,h3_tag.text)
            
#         desc = result.find_all("div", class_="VwiC3b yXK7lf lVm3ye r025kc hJNv6b Hdw6tb")
#         for data in desc:
#             desc_data = data.find_all("span")
#             description = ''
#             for span in desc_data:
#                 description += span.text
#             print(i,description)
#         i = i+1
        
# else:
#     print("Failed to retrieve the page. Status code:", response.status_code)











import requests


from pymongo import MongoClient
client = MongoClient("mongodb+srv://amarnath:scrap3142@cluster0.ipuz3gi.mongodb.net/")
db = client.googleSearch
collection = db.googleSearchData





from bs4 import BeautifulSoup
from itertools import combinations


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
}  # Adding user-agent to avoid bot detection


# url = "https://www.google.com/search?q=Ashutosh Kumar+Fourbrick"
# dUrl = getURL(keywords)
final_combined_data = []
def crawlingProfile(url):
    response = requests.get(url, headers=headers)
    final_data = {}

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all("div", class_="MjjYud")

        for i, result in enumerate(results, start=1):
            # h3_tags = result.find_all("h3", class_="LC20lb MBeuO DKV0Md")
            # for h3_tag in h3_tags:
            #     final_data[f"Heading {i}"] = h3_tag.text

            desc = result.find_all("div", class_="VwiC3b yXK7lf lVm3ye r025kc hJNv6b Hdw6tb")
            for data in desc:
                description = data.text
                desc_data = data.find_all("span")
                for span in desc_data:
                    description += span.text
                final_data[f"Description {i}"] = description

    else:
        print("Failed to retrieve the page. Status code:", response.status_code)
        
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
# input_list = ["Barack Obama", "United States", "President"]

combinations_list = generate_permutations_combinations(input_list)

def getURL(keywords):
    base_url = "https://www.google.com/search?q="
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

probability = calculate_probability(datas,input_list)
# print("Probability that Amar Nath is the CEO of Microsoft:", probability)
print("Percentage of Reality :", probability*100, "%")


# import requests
# from bs4 import BeautifulSoup

# url = "https://www.google.com/search?q=amarnath+prajapati"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
# }  # Adding user-agent to avoid bot detection

# response = requests.get(url, headers=headers)
# final_data = {"heading": [], "description": []}

# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html.parser')
#     results = soup.find_all("div", class_="MjjYud")
    
#     for result in results:
#         h3_tags = result.find_all("h3", class_="LC20lb MBeuO DKV0Md")
#         for h3_tag in h3_tags:
#             final_data["heading"].append(h3_tag.text)
            
#         desc = result.find_all("div", class_="VwiC3b yXK7lf lVm3ye r025kc hJNv6b Hdw6tb")
#         for data in desc:
#             desc_data = data.find_all("span")
#             description = ''
#             for span in desc_data:
#                 description += span.text
#             final_data["description"].append(description)
        
# else:
#     print("Failed to retrieve the page. Status code:", response.status_code)

# print(final_data)


# import requests
# from pymongo import MongoClient
# from bs4 import BeautifulSoup
# import json

# client = MongoClient("mongodb+srv://amarnath:scrap3142@cluster0.ipuz3gi.mongodb.net/")
# db = client.googleSearch
# collection = db.googleSearchData

# url = "https://www.google.com/search?q=amarnath+prajapati"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
# }  # Adding user-agent to avoid bot detection

# response = requests.get(url, headers=headers)
# final_data = {"heading": [], "description": []}

# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html.parser')
#     results = soup.find_all("div", class_="MjjYud")
    
#     for result in results:
#         h3_tags = result.find_all("h3", class_="LC20lb MBeuO DKV0Md")
#         for h3_tag in h3_tags:
#             final_data["heading"].append(h3_tag.text)
            
#         desc = result.find_all("div", class_="VwiC3b yXK7lf lVm3ye r025kc hJNv6b Hdw6tb")
#         for data in desc:
#             desc_data = data.find_all("span")
#             description = ''
#             for span in desc_data:
#                 description += span.text
#             final_data["description"].append(description)
        
# else:
#     print("Failed to retrieve the page. Status code:", response.status_code)

# # Convert final_data to JSON format
# json_data = json.dumps(final_data)
# print(json_data)
# # Insert JSON data into MongoDB collection
# post_id = collection.insert_one(json_data).inserted_id
# print("Inserted document with ID:", post_id)
