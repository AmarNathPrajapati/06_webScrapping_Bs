import requests
from bs4 import BeautifulSoup

# URL of the LinkedIn profile to scrape
profile_url = "https://www.linkedin.com/in/amar-nath-prajapati-1b514421b/"

# Send a GET request to the profile URL with a User-Agent header
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
response = requests.get(profile_url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract specific information from the profile page
    name = soup.find(class_="inline t-24 t-black t-normal break-words").get_text().strip()
    headline = soup.find(class_="mt1 t-18 t-black t-normal break-words").get_text().strip()
    location = soup.find(class_="t-16 t-black t-normal inline-block").get_text().strip()
    industry = soup.find(class_="pv-top-card-v2-section__entity-info-container").find_all("p")[1].get_text().strip()

    # Print the extracted information
    print("Name:", name)
    print("Headline:", headline)
    print("Location:", location)
    print("Industry:", industry)
else:
    print("Failed to retrieve the LinkedIn profile. Status code:", response.status_code)
