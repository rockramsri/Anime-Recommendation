
from mal import AnimeSearch
from bs4 import BeautifulSoup
import csv

import requests
import json
from requests.auth import HTTPBasicAuth
#getting Reviews from myAnimeList of a particular Anime
class MyAnimeList:
    animeName=""
    def __init__(self, animeName: str):
        self.animeName = animeName
   
    def fetchData(self):

        search = AnimeSearch(self.animeName);
        auth = HTTPBasicAuth("dbf858acc27540fec28ad5c0dce932d4", "5e188df3d82064606b5a71d8cd77462b0965771dc973998612444bf9f67e9e76");
        p=1
        animeListUrl=search.results[0].url+"/reviews?sort=suggested&filter_check=&filter_hide=&preliminary=on&p="
        filename = "Data-Preparation\AnimeDataScrapper\MyAnimeListData.csv"
        with open(filename, 'w', newline='') as file:
            fieldnames = ['name', 'Review',"animeName"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
           
            while(True):
                updateUrl=animeListUrl+str(p)
                print(updateUrl)
                rsp = requests.request("get",updateUrl, headers=None, auth=auth)
                soup = BeautifulSoup(rsp.content, 'html5lib')
                comments = soup.body.find_all('div', attrs={'class' : 'js-review-element'})
                for eachComment in comments:
                    name = eachComment.find('a', attrs={'data-ga-click-type' : 'review-anime-reviewer'}).get_text()
                    Review = eachComment.find('div', attrs={'class' : 'text'}).get_text()
                    writer.writerow({'name': name, 'Review': Review.encode("utf-8"), 'animeName':self.animeName})

                if(soup.body.find('a', attrs={'data-ga-click-type' : 'review-more-reviews'})):
                    p+=1
                else:
                    break

