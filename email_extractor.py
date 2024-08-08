import re
import requests
from bs4 import BeautifulSoup
# url = "https://www.fourbrick.com/services"
url = "https://en.wikipedia.org/wiki/Email_address"
r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent,'html.parser')
# print(soup.prettify())
# title = soup.title
# print(title)

# Selecting all elements with class "nTiihL wixui-box"
# elements = soup.find_all(class_="wixui-rich-text__text")

# # Printing the text content of each element
# for element in elements:
#     print(element.get_text())

# Email validation regex pattern
email_pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
# Find all <ul> tags
ul_tags = soup.find_all('ul')

# Iterate over each <ul> tag
for ul in ul_tags:
    # Find all <li> tags within the current <ul> tag
    li_tags = ul.find_all('li')
    # Iterate over each <li> tag and print its text content
    for li in li_tags:
        # Extract all email addresses from the text
        emails = email_pattern.findall(li.get_text(strip=True))
        # Print each email address found
        for email in emails:
            print(email)

