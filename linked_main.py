import requests
from bs4 import BeautifulSoup
from linkedin import linkedin

# LinkedIn API credentials
client_id = '7878c18zylxgtf'
client_secret = 'qGwa59LXMwOdu1E0'
redirect_uri = 'http://localhost:8000/auth/linkedin/callback'

# Create a LinkedIn application object
application = linkedin.LinkedInApplication(
    client_id,
    client_secret,
    redirect_uri,
    permissions=["r_liteprofile", "r_emailaddress"]
)

# Generate authorization URL
auth_url = application.auth.get_authorization_url()

# Print the URL and manually visit it in your browser
print("Visit this URL to authorize your application:", auth_url)

# After authorization, LinkedIn will redirect to your redirect URI with a code
# Use this code to obtain an access token
code = input("Enter the authorization code from the redirect URI: ")
access_token = application.auth.get_access_token(code)

# Use the access token to make a request to LinkedIn's API to retrieve the user's profile data
profile_url = "https://www.linkedin.com/in/amar-nath-prajapati-1b514421b/"
headers = {"Authorization": "Bearer " + access_token['access_token']}
response = requests.get(profile_url, headers=headers)

# Parse the JSON response to extract specific information using BeautifulSoup
profile_data = response.json()

# Extract and print profile information
print("LinkedIn Profile Information:")
print("Name:", profile_data['localizedFirstName'], profile_data['localizedLastName'])
print("Headline:", profile_data['localizedHeadline'])
print("Location:", profile_data['localizedLocation']['country']['preferredLocale']['country'])
print("Industry:", profile_data['localizedIndustry'])
