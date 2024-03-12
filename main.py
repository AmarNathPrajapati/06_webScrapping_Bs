# If you want to scrape a website:
# 1. Use the API
# 2. HTML Web Scraping using some tool like bs4

# Step 0: Install all the requirements
# pip install requests
# pip install bs4
# pip install html5lib

import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

# Step 1: Get the HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# Step 2: Parse the HTML or Creating the soup
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify())

# Step 3: HTML Tree traversal
# 
# Commonly used types of objects:

title = soup.title
# print(type(title)) # 1. Tag
# print(type(title.string)) # 2. NavigableString
# print(type(soup)) # 3. BeautifulSoup


# # 4. Comment
# markup = "<p><!-- this is a comment --></p>"
# soup2 = BeautifulSoup(markup)
# print(soup2.string)
# print(type(soup2.p.string))
# exit()


# Get the title of the HTML page
# title = soup.title

# Get all the paragraphs from the page
# paras = soup.find_all('p')
# print(paras)

# print(anchors)
# anchor = soup.find_all("a")
# print(anchor)



# Get first element in the HTML page
# print(soup.find('p') ) 

# Get classes of any element in the HTML page
# print(soup.find('p')['class'])

# find all the elements with class lead
# print(soup.find_all("div", class_="p-4 md:w-1/3 flex justify-center"))

# Get the text from the tags/soup
# print(soup.find('p').get_text())
# print(soup.get_text())

# Get all the anchor tags from the page
# anchors = soup.find_all('a')
# all_links = set()
# # Get all the links on the page:
# for link in anchors:
#     if(link.get('href') != '#'): 
#         linkText = "https://codewithharry.com" +link.get('href')
#         all_links.add(link)
#         print(linkText)

navbarSupportedContent = soup.find(class_='p-4 md:w-1/3 flex justify-center')

# .contents - A tag's children are available as a list ------ slow ------- store in memorhy
# .children - A tag's children are available as a generator   ------fast ------ not store in memory
# for elem in navbarSupportedContent.contents:
#     print(elem)
 
# for item in navbarSupportedContent.strings:
#     print(item)

# for item in navbarSupportedContent.stripped_strings:
#     print(item)

# print(navbarSupportedContent.parent)
# for item in navbarSupportedContent.parents: 
#     print(item.name)

# print(navbarSupportedContent.next_sibling.next_sibling)
# print(navbarSupportedContent.previous_sibling.previous_sibling)

elem = soup.select('.text-3xl')
print(elem)
for item in elem:
    print(item.string)
# elem = soup.select('#loginModal')[0] 
# print(elem)

