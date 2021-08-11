import time
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
import requests

DATAURL = 'https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'

browser = webdriver.Chrome("chromedriver")
browser.get(DATAURL)

time.sleep(10)

headers = ["name","ligth_years_from_earth","planet_mass","stellar_magnitude","discovery_date","hyper_link","planet_type","planet_radius","orbital_radius","orbital_period"]

planetdata = [ ]
newplanetdata=[]

def scrap():

    for i in range(1,444):
        soup = BeautifulSoup(browser.page_source , "html.parser")

        for ultag in soup.find_all("ul" , attrs={"class":"exoplanet"}):
            litags = ultag.find_all("li")
            temp=[ ]
            for index,litag in enumerate(litags):
                if index == 0:
                    temp.append(litag.find_all("a")[0].contents[0])
                else :
                    try:
                        temp.append(litag.contents[0])
                    except:
                        temp.append(" ")

            hyperlinklitag = litags[0]
            temp.append("https://exoplanets.nasa.gov"+hyperlinklitag.find_all("a" , href = True)[0]["href"])
            planetdata.append(temp)

        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()

def scrapmoredata(hyper_link):
    try:
        page = requests.get(hyper_link)
        soup = BeautifulSoup(page.content , "html.parser")
        list = []
        for tr_tag in soup.find_all("tr", attrs={"class":"fact_row"}):
            td_tags = tr_tag.find_all("td")
            for tdtag in td_tags:
                try:
                    list.append(tdtag.find_all("div",attrs={"class":"value"})[0].contents[0])
                except:
                    list.append(" ")
        newplanetdata.append(list)

    except:
        time.sleep(2)
        scrapmoredata(hyper_link)

scrap()
for index,data in enumerate(planetdata):
    scrapmoredata(data[5])

planet = planetdata+newplanetdata
print(planet[1])

with open("final.csv","w")as f:
    write = csv.writer(f)
    write.writerow(headers)
    write.writerows(planet)


