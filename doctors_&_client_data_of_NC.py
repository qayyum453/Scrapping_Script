import lxml
import pandas as pd
import bs4 as bs
import urllib.request
from urllib.request import urlopen,Request
import csv

file = open('doctors_&_client_data_collection_of_asthma_disease_SC.csv','a+',encoding='utf-8')
file1 = csv.writer(file)
file1.writerow(['Doctors Name','Clinic','phone_no','full_address','Patients_type'])
doctors_name = []
phone_no = []
clinic_name = []
street_location = []
location = []
patient_type = []
id_list = []

def asthm_data_collection_of_NC_func(count = 1,count1 = 1,count2=1):
    page = []
    snd_page = []
    for i in range(1,9):
        url = 'http://allergist.aaaai.org/find/index.php?City=&State=SC&Country=&ZipCode=29401&Distance=200&Search=Search&page='+str(i)+'#directoryresultstop'
        page.append(url)
    for item in page:
        p = urllib.request.Request(item,data=None,headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'})
        page_no = urllib.request.urlopen(p).read()
        soup = bs.BeautifulSoup(page_no,'lxml')

        main_div = soup.find('div',id='directory')
        # print(main_div.text)
        a_tag = main_div.find_all('a',class_='providername')
        for cont in a_tag:
            print(str(count1)+cont.get('href'))
            id_list.append(cont.get('href'))
            count1 += 1
    # print("list of ids ")
    # print(id_list)

    for i in id_list:
        if(i == 'detail.php?id=45014' or i == 'detail.php?id=112041' or i == 'detail.php?id=80169' or i == 'detail.php?id=121214' or i == 'detail.php?id=103336'):
            continue
        else:
            url = 'http://allergist.aaaai.org/find/'+str(i)
            snd_page.append(url)
    for item in snd_page:
        p = urllib.request.Request(item, data=None, headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'})
        page_no = urllib.request.urlopen(p).read()
        soup = bs.BeautifulSoup(page_no, 'lxml')
        # print(soup.h2.text)
        doctors_name.append(soup.h2.text)
        # main_div = soup.find('div',class_='section-content col sm-12 md-12 lg-12')
        # for con in main_div:
        #     print(con)
        # fildset_p = soup.find_all('fieldset',class_='')
        # print(fildset_p.p.p.text)
        div_call = soup.find('div',class_='call')
        print(str(count)+div_call.text)
        count +=1

        phone_no.append(div_call.text)
        clinic_div = soup.find('div',class_='dir_backlink')
        # print(clinic_div.findNext('fieldset',attrs = {'class':''}).legend.text)
        street_location.append(clinic_div.findNext('fieldset',attrs = {'class':''}).div.text)
        clinic_name.append(clinic_div.findNext('fieldset',attrs = {'class':''}).legend.text)
        # print(div_call.previous_sibling.text)

        location.append(div_call.previous_sibling.text)
        # print(location+street_location)
        patient_type2 = soup.findAll('fieldset')[1]
        # print(patient_type2.strong.findNext('strong').text)
        if patient_type2.strong is not None:
            print(str(count2)+' '+patient_type2.p.findNext('p').text)
            patient_type.append(patient_type2.p.findNext('p').text)
        else:
            patient_type1 = soup.findAll('fieldset')[2]
            if patient_type1.strong is not None:
                print(str(count2)+' '+patient_type1.p.findNext('p').text)
                patient_type.append(patient_type1.p.findNext('p').text)
            else:
                print("empty")
                patient_type.append('empty')
        count2 +=1
        # if(patient_type2.strong.text == 'Patients'):
        #     print(patient_type2.p.findNext('p').text)
        #
        # else:
        #     print(item)
    for i in range(0,len(location)):
        print(location[i]+" "+street_location[i])
    # print("doctors")
    # print(len(doctors_name))
    # print("phone_no")
    # print(len(phone_no))
    # print("patinet")
    # print(len(patient_type))
    # print("clinic")
    # print(len(clinic_name))
    # print("location")
    # print(len(location))
    for i in range(0,len(doctors_name)):
        file1.writerow([doctors_name[i],clinic_name[i],phone_no[i],location[i]+" "+street_location[i],patient_type[i]])
asthm_data_collection_of_NC_func()

# df = pd.read_html('https://ipfs.io/ipfs/QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/List_of_California_wildfires.html#cite_note-20',header=None)
# print(df)
# #
# # url = 'https://ipfs.io/ipfs/QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/List_of_California_wildfires.html#cite_note-20'
# # page = urllib.request.urlopen(url).read()
# # soup = bs.BeautifulSoup(page,'lxml')
# # main_div = soup.find('div',id='mw-content-text')
# # print(main_div.text)
# # table = main_div.find('table',class_ = 'wikitable sortable')
# # print(table.text)
