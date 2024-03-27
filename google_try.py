import requests
from bs4 import BeautifulSoup

def scrape_google_results(query, num_pages=1):
    results = []

    for page in range(num_pages):
        url = f"https://www.google.com/search?q={query}&start={page*10}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
        }  # Adding user-agent to avoid bot detection

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            search_results = soup.find_all("div", class_="tF2Cxc")
            
            for result in search_results:
                title = result.find("h3", class_="LC20lb").text.strip()
                description = result.find("div", class_="IsZvec").text.strip()
                link = result.find("a").get("href")
                results.append({"title": title, "description": description, "link": link})
        else:
            print(f"Failed to retrieve page {page}. Status code:", response.status_code)

    return results

# Example usage
query = "amarnath prajapati"
num_pages = 1  # Number of pages to scrape
search_results = scrape_google_results(query, num_pages)

# Print the scraped results
for i, result in enumerate(search_results, start=1):
    print(f"Result {i}:")
    print("Title:", result["title"])
    print("Description:", result["description"])
    print("Link:", result["link"])
    print()
