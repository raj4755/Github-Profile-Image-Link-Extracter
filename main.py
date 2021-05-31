import requests
from bs4 import BeautifulSoup as bs


def github_photo():
    github_profile = input("Enter Github User Profile : ")
    github_url = "https://github.com/" + github_profile
    response = requests.get(github_url)

    soup = bs(response.content, 'html.parser')
    profile_image = soup.find('img', {'alt' : '@' + github_profile})['src']
    return profile_image

if __name__ == "__main__":
    try:
        result = github_photo()
        print(result)
    
    except Exception as e:
        print("Something Error Occured....")