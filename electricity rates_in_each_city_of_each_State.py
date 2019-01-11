import bs4 as bs
import lxml
import urllib.request
from urllib.request import urlopen,Request
import csv
import pandas as pd

df = pd.read_csv('list of cities and state in usa.csv')
city = list(df['City'].astype('str'))
state = list(df['State full'].astype('str'))

city = [x.lower() for x in city]
state = [x.lower() for x in state]

# print(city)
# print(state)
file = open('Ohio.csv','a+',encoding='utf-8',newline='')
file1 = csv.writer(file)
file1.writerow(['State_name','City_name','Commercial','Resedential','Industrial'])

page = []
# state = []
for i in range(1,40):
    url = 'https://www.electricitylocal.com/states/'+(state[i])+'/'+city[i]+'/'
    # page.append(url)
# for item in page:
    try:
        p = urllib.request.Request(url, data=None, headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'})
        page = urllib.request.urlopen(p).read()
    except urllib.request.HTTPError as e:
        # print("we failed with error code",e.code)
        continue
    else:

        soup = bs.BeautifulSoup(page, 'lxml')
        # print(soup.find('div',id = 'cities'))
        div_1 = soup.find('div',class_='info1')
        commercial_rate = div_1.find('ul',class_='no2')
        print(url)
        print(commercial_rate.strong.text)

        div_2 = soup.find('div', class_='info2')
        resedential_rate = div_2.find('ul', class_='no2')
        print(resedential_rate.strong.text)

        div_3 = soup.find('div', class_='info3')
        industrial_rate = div_3.find('ul', class_='no2')
        print(industrial_rate.strong.text)

        file1.writerow([df['State full'][i],df['City'][i],commercial_rate.strong.text,resedential_rate.strong.text,industrial_rate.strong.text])
