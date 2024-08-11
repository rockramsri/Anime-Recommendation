
import praw
from praw.models import MoreComments
import csv
import pandas as pd

#getting Reviews from Reddit of a particular Anime

class RedditScrapper:
    animeName=""
    def __init__(self, animeName: str):
        self.animeName = animeName
        print(animeName)
    
    def fetchData(self):
        reddit = praw.Reddit(client_id="IVbyFluVv38VHU_GcU9xbA",         # your client id
                                client_secret="RsZPzB1RcktthdibGALZD_DJDg_OJg",      # your client secret
                                user_agent="Maximuzz")        # your user agent
        #filename = "Data-Preparation\AnimeDataScrapper\RedditData.csv"
        #with open(filename, 'w', newline='') as file:
        fieldnames = ['name', 'Review',"Reddit_Title"]
            #writer = csv.DictWriter(file, fieldnames=fieldnames)
            #writer.writeheader()
        commentList=[]
        for submission in reddit.subreddit("all").search(self.animeName+" anime"):
            #print('\033[1m' +submission.title)            
            url = "https://www.reddit.com"+submission.permalink;
            submission = reddit.submission(url=url)
            for top_level_comment in submission.comments:
                if isinstance(top_level_comment, MoreComments):
                    continue
                commentList.append([top_level_comment.author,top_level_comment.body.encode("utf-8"),submission.title])
                #writer.writerow({'name': top_level_comment.author  , 'Review': top_level_comment.body.encode("utf-8"), 'Reddit_Title':submission.title})
                #print(top_level_comment.body)
        return pd.DataFrame(commentList,columns=fieldnames)

# r=RedditScrapper("Demon Slayer")
# m=r.fetchData()
# print(m.head())


