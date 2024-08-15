import requests
from bs4 import BeautifulSoup

def get_article_content(url):
    # Send a GET request to the specified URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the title of the article
        title = soup.title.string
        paragraphs = soup.find_all(attrs={'data-component-name':'p'})
        content = ''

        # Extract all paragraphs
        paragraphs = soup.find_all("p")

        # Print each paragraph separately
        for paragraph in paragraphs:
            print(paragraph.text)
            print("-" * 20)  # Separator between paragraphs

        return title, content
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None, None

# Example URL 
article_url = 'https://10best.usatoday.com/awards/travel/best-beach-in-florida-2024/'

title, content = get_article_content(article_url)
print('-'*50)
if(title != None and content != None): 
    print(title)
    print(content)