import requests
from bs4 import BeautifulSoup
import pandas as pd

Name=[]
Location=[]
City=[]
P_O_Box=[]
Phone=[]
Mobile=[]
Company_page_link=[]
Logo_url=[]

for i in range(1,67):
    #response=requests.get('https://www.yellowpages-uae.com/uae/restaurant'+str(i))
    response=requests.get(f'https://www.yellowpages-uae.com/uae/restaurant-{i}.html')
    soup=BeautifulSoup(response.content, 'html.parser')
    #print(soup.prettify())

    box=soup.find('div', id="content_left650")

    names = box.find_all("div", class_="col-lg-11 col-md-10 col-sm-8 col-xs-8 col-12 title-div")
    #print(names)
    for i in names:
        n=i.text
        Name.append(n)
    print(len(Name))


    locations = box.find_all("span", itemprop="streetAddress")

    for i in locations:
        n=i.text
        Location.append(n)
    print(len(Location))

    cities = box.find_all("strong", itemprop="addressLocality")

    for i in cities:
        n=i.text
        City.append(n)
    print(len(City))

    p_o_boxs = box.find_all("span", class_="pobox")

    for i in p_o_boxs:
        n=i.text
        P_O_Box.append(n)
    print(len(P_O_Box))

    phone = box.find_all("a", title="Phone")

    for i in phone:
        n=i.text
        Phone.append(n)
    print(len(Phone))

    mobile = box.find_all("a", title="Mobile")

    for i in mobile:
        n=i.text
        Mobile.append(n)
    print(len(Mobile))

    company_link = soup.find_all("a")
    for i in company_link:
        source = i['href']
        if source:
            if r'website' in source:
                source
    Company_page_link.append(source)
    print(len(Company_page_link))

    logo_url = box.find_all("img")

    for i in logo_url:
        source1 = i['src']
        if source1:
            if r'image' in source1:
                source1
    Logo_url.append(source1)
    print(len(Logo_url))

df = {"Name":Name,"Location":Location,"City":City,"P.O Box":P_O_Box,"Phone":Phone,"Mobile":Mobile,"Company Page URL":Company_page_link,"Logo URL":Logo_url}
df=pd.DataFrame.from_dict(df, orient='index')
df=df.transpose()
#print(df)

df.to_csv("results.csv")