from bs4 import BeautifulSoup
import requests
source = requests.get("https://coreyms.com").text
soup = BeautifulSoup(source,"lxml")
# for article in soup.find_all('div',class_='content_video_ima-countdown-divima-countdown-div'):
#     headline = article.h2.a.text
#     print(headline)
#print(soup)
article = soup.find("article")
#print(article.prettify())
vid_src = article.find("iframe", class_ ='youtube-player')['src']
vid_id = vid_src.split('/')[4]
#print(vid_src)
print(vid_id)

