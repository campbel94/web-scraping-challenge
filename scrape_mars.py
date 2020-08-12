# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

from bs4 import BeautifulSoup
from splinter import Browser
import requests
import pandas as pd


def init_browser():
    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)


# %%
url = 'https://mars.nasa.gov/news/'
browser.visit(url)


# %%
soup = BeautifulSoup(browser.html, 'html.parser')


# %%
### NASA Mars News


# %%
title_results = soup.find_all('div', class_='content_title')

par_results = soup.find_all('div', class_='article_teaser_body')

news_title = title_results[1].text
news_p = par_results[0].text

print(news_title)
print(news_p)


# %%
### JPL Mars Space Images - Featured Image


# %%
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# %%
find_id = browser.find_by_id('full_image')
find_id.click()


# %%
browser.is_element_not_present_by_text('more info', wait_time=1)


# %%
more_info = browser.click_link_by_partial_text('more info')


# %%
soup = BeautifulSoup(browser.html, 'html.parser')
results = soup.find('figure', class_='lede')
img_path = results.a['href']
featured_image_url = 'https://www.jpl.nasa.gov' + img_path
print(featured_image_url)


# %%
### Mars Weather


# %%
### Mars Facts


# %%
url = 'https://space-facts.com/mars/'
tables = pd.read_html(url)
tables


# %%
df = tables[0]
df.columns = ['Mars Metrics', 'Values']
df.head(10)


# %%
html_table = df.to_html()
print(html_table)


# %%
### Mars Hemispheres


# %%
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# %%
soup = BeautifulSoup(browser.html, 'html.parser')
find_items = soup.find_all('div', class_='item')
hemisphere_image_urls = []
default_url = 'https://astrogeology.usgs.gov'

for i in find_items: 
    title = i.find('h3').text
    specific_url = i.find('a', class_='itemLink product-item')['href']
    browser.visit(default_url + specific_url)
    soup = BeautifulSoup(browser.html, 'html.parser')
    img_url = default_url + soup.find('img', class_='wide-image')['src']
    hemisphere_image_urls.append({"title" : title, "img_url" : img_url})    

hemisphere_image_urls


