from MyAnimeList import MyAnimeList
from RedditScrapper import RedditScrapper


class AniScrapper():
    def __init__(self, animeName: str):
        self.animeName = animeName
    

    def fetchReviewFrom(website):
        if website == "Reddit" or website == "all":
            t1=RedditScrapper("kaiju no 8")
            t1.fetchData()
        if website == "Reddit" or website == "all":
            t1=MyAnimeList("Demon Slayer")
            t1.fetchData()


    #def sendToAws():
        #send to aws
    
    #def fetchandProcess():

      

