# import lxml
# import bs4 as bs
# import re
# import urllib.request
# import csv
#
# file = open('Farmland_prices_in_oregon.csv','a+',encoding='utf-8')
# file1 = csv.writer(file)
# file1.writerow(['Name_of_fram','Price_of_fram','Description_details'])
# page = []
#
# name = []
# price = []
# description = []
#
# for i in range(1,4):
#         url = 'http://homeslandcountrypropertyforsale.com/farms/state/or/page/'+str(i)+'/'
#         page.append(url)
#
# for item in page:
#     page_no = urllib.request.urlopen(item).read()
#     soup = bs.BeautifulSoup(page_no,'lxml')
#     main_div = soup.find('div',class_='row')
#     farm_name_div = main_div.find_all('div',class_='property_listing')
#     for nm in farm_name_div:
#         print(nm.h4.a.text)
#         name.append(nm.h4.a.text)
#
#     price_of_farm = main_div.find_all('div',class_='listing_unit_price_wrapper')
#     for pr in price_of_farm:
#         print(pr.text)
#         price.append(pr.text)
#
#     description_of_farm = main_div.find_all('div',class_='listing_details the_grid_view')
#     for dr in description_of_farm:
#         print(dr.text)
#         description.append(dr.text)
#     for i in range(0,len(name)):
#         file1.writerow([name[i],price[i],description[i]])
#     # for nm in farm_name_div:
#     #     link = nm.get('data-link')
#     #     start = link.find('http://homeslandcountrypropertyforsale.com/farms/properties/')
#     #     end = link.find('',start)
#     #     print(link[start:end])
import bs4 as bs
import lxml
import urllib.request
from urllib.request import urlopen,Request


page = []

for i in range(1,2):
    url = 'https://www.medicinenet.com/mold_exposure/greensboro-nc_city.htm'
    page.append(url)

for item in page:
    p = urllib.request.Request(item, data=None, headers={
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'})
    page = urllib.request.urlopen(p).read()
    soup = bs.BeautifulSoup(page, 'lxml')
    main_div = soup.find('div',class_='locList')
    all_p = main_div.find_all('p')
    for data in all_p:
        print(data.text)