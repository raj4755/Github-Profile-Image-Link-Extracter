import requests
from bs4 import BeautifulSoup as bs

try:
    github_profile = input("Enter Github User Profile : ")

    github_url = "https://github.com/" + github_profile
    response = requests.get(github_url)
    # print(response.content)

    soup = bs(response.content, 'html.parser')
    profile_image = soup.find('img', {'alt' : '@' + github_profile})['src']
    print(profile_image)
except Exception as e:
    print("Something Error Occured....")


