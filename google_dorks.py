import itertools

def generate_google_search_url(operator, keywords):
  
    # Encode the keywords
    encoded_keywords = '+'.join(keywords)

    # Construct the search URL with the specified operator
    search_url = f"https://www.google.com/search?q={operator}%3A{encoded_keywords}"

    return search_url

# Example keywords
keywords = ["Sundar Pichai", "Google", "CEO"]

# Example operators
operators = ["intitle", "site", "inurl", "intext"]

# Generate Google search URLs with various operators for each combination of keywords
combinationURL = []

# Loop through each operator
for operator in operators:
    # Generate Google search URLs for each combination of keywords
    for i in range(2, len(keywords) + 1):
        combinations = itertools.combinations(keywords, i)
        for combo in combinations:
            combinationURL.append(generate_google_search_url(operator, combo))

