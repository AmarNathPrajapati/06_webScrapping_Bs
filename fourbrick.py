import requests
from bs4 import BeautifulSoup
url = "https://www.fourbrick.com/services"
r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent,'html.parser')
# print(soup.prettify())
title = soup.title
print(title)

# Selecting all elements with class "nTiihL wixui-box"
elements = soup.find_all(class_="wixui-rich-text__text")

# Printing the text content of each element
for element in elements:
    print(element.get_text())
