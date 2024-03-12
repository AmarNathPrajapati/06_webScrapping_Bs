import requests
from bs4 import BeautifulSoup
url = "https://www.linkedin.com/in/amar-nath-prajapati-1b514421b/"
r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent,'html.parser')
print(soup.prettify())
# title = soup.title
# print(title)
