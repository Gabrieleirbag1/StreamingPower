import requests
from bs4 import BeautifulSoup

url = "http://films.lizziewizzie.site/films_et_series/Person%20of%20Interest%20Season%201%20Complete%20720p%20BluRay%20x264%20%5bi_c%5d/"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

video_links = soup.find_all(lambda tag: tag.name == "a" and not tag.find_parent("th") and tag.text.strip() != "Parent Directory")

for link in video_links:
    video_url = link.get("href")
    video_text = link.text
    
    if video_url:
        print(f'{url}{video_url}')


