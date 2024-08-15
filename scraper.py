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
        title = soup.find('h1').get_text()

        # Extract the content of the article
        paragraphs = soup.find_all('p')
        content = '\n'.join([paragraph.get_text() for paragraph in paragraphs])

        return title, content
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None, None

# Example URL from BBC News
article_url = 'https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html'

# Get the article title and content
title, content = get_article_content(article_url)

# Display the results
if title and content:
    print(f"Title: {title}\n\nContent:\n{content}")
else:
    print("Failed to retrieve article information.")
