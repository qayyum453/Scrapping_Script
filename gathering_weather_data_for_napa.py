import pandas as pd
import numpy as np
import bs4 as bs
import lxml
import csv
from urllib.request import Request,urlopen
import urllib.request

file = open('Weather_data_of_sonoma_by_month_for_40_years2.csv','a+',encoding='utf-8',newline='')
file1 = csv.writer(file)

def func():
    min_temp = []
    min_t = 0
    max_temp = []
    max_t = 0
    mean_temp = []
    mean_t = 0
    rain = []
    rain_t = 0
    snow = []
    snow_t = 0
    mean_wind_speed = []
    mean_w_s = 0
    max_wind_speed = []
    max_w_s = 0
    max_wind_gust = []
    max_w_g = 0
    for y in range(2014,2018):
        for m in range(1, 13):
            page_no = []
            file1.writerow(['Year', y, 'Month', m])
            file1.writerow(
                ['Min_Temp', 'Mean_Temp', 'Max_T+emp', 'Rain', 'Mean_wind', 'Max_wind', 'Max_wind_gust'])
            if (m == 2):
                for d in range(1, 29):
                    url = 'https://www.almanac.com/weather/history/OR/Oregon%20City/' + str(y) + '-' + str(m) + '-' + str(d)
                    page_no.append(url)
                for item in page_no:
                    p = urllib.request.Request(item, data=None, headers={
                        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'})
                    page = urllib.request.urlopen(p).read()
                    soup = bs.BeautifulSoup(page, 'lxml')
                    print(item)
                    table = soup.find('table', class_='weatherhistory_results')
                    min_tr = table.find('tr', class_='weatherhistory_results_datavalue temp_mn')
                    min_temp.append(min_tr.td.text)
                    mean_tr = table.find('tr', class_='weatherhistory_results_datavalue temp')
                    mean_temp.append(mean_tr.td.text)
                    max_tr = table.find('tr', class_='weatherhistory_results_datavalue temp_mx')
                    max_temp.append(max_tr.td.text)
                    rain_tr = table.find('tr', class_='weatherhistory_results_datavalue prcp')
                    rain.append(rain_tr.td.text)
                    # snow_tr = table.find('tr', class_='weatherhistory_results_datavalue sndp')
                    # snow.append(snow_tr.td.text)
                    mean_win_tr = table.find('tr', class_='weatherhistory_results_datavalue wdsp')
                    mean_wind_speed.append(mean_win_tr.td.text)
                    max_win_tr = table.find('tr', class_='weatherhistory_results_datavalue mxspd')
                    max_wind_speed.append(max_win_tr.td.text)
                    max_win_gus_tr = table.find('tr', class_='weatherhistory_results_datavalue gust')
                    max_wind_gust.append(max_win_gus_tr.td.text)
                    file1.writerow([min_temp[min_t], mean_temp[mean_t], max_temp[max_t], rain[rain_t],
                                    mean_wind_speed[mean_w_s], max_wind_speed[max_w_s], max_wind_gust[max_w_g]])
                    min_t += 1
                    mean_t += 1
                    max_t += 1
                    rain_t += 1

                    mean_w_s += 1
                    max_w_s += 1
                    max_w_g += 1

            else:
                for d in range(1, 31):
                    url = 'https://www.almanac.com/weather/history/OR/Oregon%20City/' + str(y) + '-' + str(m) + '-' + str(d)
                    page_no.append(url)
                for item in page_no:
                    p = urllib.request.Request(item, data=None, headers={
                        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'})
                    page = urllib.request.urlopen(p).read()
                    soup = bs.BeautifulSoup(page, 'lxml')
                    print(item)
                    table = soup.find('table', class_='weatherhistory_results')
                    min_tr = table.find('tr', class_='weatherhistory_results_datavalue temp_mn')
                    min_temp.append(min_tr.td.text)
                    mean_tr = table.find('tr', class_='weatherhistory_results_datavalue temp')
                    mean_temp.append(mean_tr.td.text)
                    max_tr = table.find('tr', class_='weatherhistory_results_datavalue temp_mx')
                    max_temp.append(max_tr.td.text)
                    rain_tr = table.find('tr', class_='weatherhistory_results_datavalue prcp')
                    rain.append(rain_tr.td.text)
                    # snow_tr = table.find('tr', class_='weatherhistory_results_datavalue sndp')
                    # snow.append(snow_tr.td.text)
                    mean_win_tr = table.find('tr', class_='weatherhistory_results_datavalue wdsp')
                    mean_wind_speed.append(mean_win_tr.td.text)
                    max_win_tr = table.find('tr', class_='weatherhistory_results_datavalue mxspd')
                    max_wind_speed.append(max_win_tr.td.text)
                    max_win_gus_tr = table.find('tr', class_='weatherhistory_results_datavalue gust')
                    max_wind_gust.append(max_win_gus_tr.td.text)
                    file1.writerow([min_temp[min_t], mean_temp[mean_t], max_temp[max_t], rain[rain_t],
                                    mean_wind_speed[mean_w_s], max_wind_speed[max_w_s], max_wind_gust[max_w_g]])
                    min_t += 1
                    mean_t += 1
                    max_t += 1
                    rain_t += 1

                    mean_w_s += 1
                    max_w_s += 1
                    max_w_g += 1
                    # print(table.text)
                    # table_rows = table.find_all('tr')
                    #
                    # for tr in table_rows:
                    #     td = tr.find_all('td')
                    #     row = [i.text for i in td]
                    #     print(row)

                    # # getting table data using pandas library
                    # dfs = pd.read_html(item,header=0)
                    # for df in dfs:
                    #     print(df)

func()




