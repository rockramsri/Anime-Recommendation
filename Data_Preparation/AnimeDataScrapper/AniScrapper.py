from MyAnimeList import MyAnimeList
from RedditScrapper import RedditScrapper


class AniScrappers:
    
    def fetchReviewFromReddit(self,animeName):
        try:
            t1=RedditScrapper(self.animeName)
            return t1.fetchData()
        except:
            return None
    def fetchReviewFromMyAnimeList(self,animeName):
        try:
            t1=MyAnimeList(self.animeName)
            return t1.fetchData()
        except:
            return None


    #def sendToAws():
        #send to aws
    
    #def fetchandProcess():

      

