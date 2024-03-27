import requests
from bs4 import BeautifulSoup

url = "https://www.bing.com/search?q=google+ceo"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())
results = soup.find_all("li", class_="b_algo")
for result in results:
    # Find the text of the anchor tag inside h2
    h2_text = result.find("h2").find("a").text.strip()
    # Find the text of p tag with class "b_lineclamp2 b_algoSlug"
    p_text = result.find("p", class_="b_algoSlug").text.strip()
    print(h2_text)
    print(p_text)
