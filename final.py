from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import os
from PIL import Image
import tweepy as tp
import time

consumer_key = 'EmP6oyH9UgpQ9GhYF787LAwqB'
consumer_secret = '6BM2uUuuyWmmRJfvo7TdGvF5oZIHJroJRyMCGLIffgGnwIvj6g'
access_token = '1256203452700647424-pWhe38QMUi35ChzttO5sJfDc8eekHh'
access_secret = 'HVSzRHUzOz9asHGDY5qbzyDv2ox67SgsQgDrTX4WXtOOj'


url = 'https://unsplash.com/s/photos/flowers'
driver = webdriver.Chrome("C://Users/pc/Downloads/chromedriver")
driver.get(url)
content = driver.page_source
soup = BeautifulSoup(content,features="lxml")
image_tags=soup.findAll('img')

if not os.path.exists('models'):
    os.makedirs('models')
os.chdir('models')

x = 0
for image in image_tags:
    try:
        url = image['src']
        response = requests.get(url)
        if response.status_code == 200:
            with open('model-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x += 1 
        if x>15:
            break
    except:
        pass


auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

for model_image in os.listdir('.'):
    img=Image.open(model_image)
    width, height=img.size
    if width>=100 and height>=100:
        api.update_with_media(model_image)
        time.sleep(4)
    else:
        continue
