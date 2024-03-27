import requests
from bs4 import BeautifulSoup
url = "https://www.google.com/search?q=amarnath+prajapati"

# Step 1: Get the HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# Step 2: Parse the HTML or Creating the soup
soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup.prettify())