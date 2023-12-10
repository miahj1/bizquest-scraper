import requests
import re
import pandas as pd
from bs4 import BeautifulSoup
from threading import Event
from types import NoneType

def process_urls_on_page(soup):
  container = "title"
  post_frame = soup.find_all('b', {'class':container})

  processed_business_urls = []
  for frame in post_frame:
    business_url = str(frame).split("href=")[1].split(" ")[0].split('"')[1]

    if "https" not in business_url:
      pass
    else:
      processed_business_urls.append(business_url)

  return processed_business_urls

def extract_data_to_df(processed_business_urls):
  for processed_business_url in processed_business_urls:
    r = requests.get(processed_business_url, headers=headers, timeout=5).text
    return BeautifulSoup(r, 'lxml'), processed_business_url

def sidebar(page_soup, listing_url):
  sections, financial_values = [], []

  if "                " in page_soup.find("h1").text:
    title = page_soup.find("h1").text.split("                ")[1].split("\r")[0]
    sections.append("Title")
    financial_values.append(title)
  else:
    title = page_soup.find("h1").text
    sections.append("Title")
    financial_values.append(title)

  business_desc = page_soup.find('div', {'style':"word-wrap: break-word;"}).get_text(strip = True)
  sections.append("Business Description")
  financial_values.append(business_desc)

  sections.append("Listing URL")
  financial_values.append(listing_url)

  sidebar_sections = page_soup.find_all('b', {'class':"text-info"})[:-1]

  for section in sidebar_sections:
    sections.append(section.get_text()[:-1])

  if type(list_item_soup.find('b', {'class':"price"})) == NoneType:
    pass
  else:
    price = page_soup.find('b', {'class':"price"}).get_text()
    financial_values.append(price)

  for el in page_soup.find_all('b', {'class':"other-financial"}):
    m0 = re.match(r"\$\d+,\d+", el.get_text(strip=True))

    if (el.get_text(strip=True) == "Not Disclosedincluded in asking price"):
      financial_values.append(el.get_text(strip=True).split("included in asking price")[0] + " " + el.get_text(strip=True).split("Not Disclosed")[1])
    elif m0:
      leftover = re.split(r"\$\d+,\d+", el.get_text(strip=True))[1]
      financial_values.append(f"{m0.group()} {leftover}")
    else:
      financial_values.append(el.get_text(strip=True))

  key_value_pairs = zip(sections, financial_values)
  return dict(key_value_pairs)

def about_business_sale(page_soup):
  about_sections = []
  for section in page_soup.find_all('dt'):
    about_sections.append(section.get_text(strip = True)[:-1])

  section_infos = []
  for section_info in page_soup.find_all('dd'):
    section_infos.append(section_info.get_text(strip = True))

  key_value_pairs = zip(about_sections[:-2], section_infos[:-2])
  return dict(key_value_pairs)

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
}

first_page_url = "https://www.bizquest.com/businesses-for-sale/"
page_n_url = first_page_url + "page-{}/"
page = 1

master_list = []
while True:
  if page == 1:
      url = first_page_url
  else:
      url = page_n_url.format(page)

  r = requests.get(url, headers=headers, timeout=5)
  soup = BeautifulSoup(r.text, 'lxml')
  business_urls = process_urls_on_page(soup)

  for index, business_url in enumerate(business_urls):
    content_r = requests.get(business_url, headers=headers, timeout=5).text
    list_item_soup = BeautifulSoup(content_r, 'lxml')
    sidebar_dict = sidebar(list_item_soup, business_url)
    about_dict = about_business_sale(list_item_soup)
    merged_dict = {**sidebar_dict, **about_dict}
    master_list.append(merged_dict)

  if r.status_code != 200: break;

  page += 1
  Event().wait(5.0)

df = pd.DataFrame(master_list)
df.to_csv("bizquest_scrape.csv", index=False)