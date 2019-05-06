import random
import sys
import os
import re
import urllib.request as urlRequest
import urllib.parse as urlParse
from bs4 import BeautifulSoup


directory = os.path.dirname(os.path.dirname(os.path.realpath(__file__)) +"\images\\")

if not os.path.exists(directory):
    os.makedirs(directory)

page = urlRequest.urlopen(urlRequest.Request("https://critrole.com/fan-art-gallery-into-the-woods/", headers={'User-Agent': 'Mozilla/5.0'})).read()

images = BeautifulSoup(page, 'html.parser') \
	.find('div', attrs={'class': 'wonderplugin-gridgallery-list'}) \
	.find_all('div', attrs={'class': 'wonderplugin-gridgallery-item'})

image0 = images[0].find('a')

image_url = image0.get('href')
image_title = os.path.join(directory, re.sub('[^a-zA-Z]+', '_', image0.get('data-title'))+ ".jpg") 
urlRequest.urlretrieve(image_url, image_title )
