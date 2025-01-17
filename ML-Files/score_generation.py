from ast import List
import pandas as pd
from transformers import pipeline
import sys
import os
import math

#sys.path.insert(0, '../AnimeProject/Anime-Recommendation/Data_Preparation/AnimeDataScrapper')
sys.path.append('D:/Ml projects/AnimeProject/Anime-Recommendation/Data_Preparation/AnimeDataScrapper')
from AniScrapper import AniScrappers
sys.path.append('D:/Ml projects/AnimeProject/Anime-Recommendation/Data_Preprocessing')
from pre_processing import PreProcess

class ScoreGeneration:
    commentPipline=None
    count=0
    def __init__(self, modelName="siebert/sentiment-roberta-large-english") -> None:
        self.commentPipline=pipeline("sentiment-analysis",model=modelName,tokenizer=modelName, max_length=514, truncation=True,device_map="auto")
        self.count=0
    def animeListCommentsScore(self,comments):
        self.count+=1
        print(f"Comment Processing ,Count {self.count}")
        scoresMapList=[]
        for comment in comments:
            try:
                r=self.commentPipline(comment)
                scoresMapList.append(r)
                print(r)
            except Exception as e:
                print(e)
                print(comment)
                pass
        avgScore=0
        if scoresMapList!=None and len(scoresMapList)!=0:
            try:
                for score in scoresMapList:
                    if score[0]["label"]=="POSITIVE":
                        avgScore+=score[0]["score"]
                    else:
                        avgScore+=(1-score[0]["score"])
                avgScore/=len(scoresMapList)
            except:
                pass
        return round(avgScore,3)
    def fillerPatternScore(self,fillerStr: str):
        # Count the total number of 1s
        total_ones = fillerStr.count('1')
        # Find clusters of 1s
        clusters = []
        current_cluster = 0
        for char in fillerStr:
            if char == '1':
                current_cluster += 1
            else:
                if current_cluster > 0:
                    clusters.append(current_cluster)
                    current_cluster = 0
        if current_cluster > 0:
            clusters.append(current_cluster)
    
        # Calculate the number of clusters
        number_of_clusters = len(clusters)
    
        # Evaluate the length of each cluster
        cluster_lengths = clusters
    
        # Frequency of clusters between zeros
        frequency_between_zeros = max(0, number_of_clusters - 1)

        w1 = 2  # weight for presence of 1s
        w2 = 3  # weight for clustering of 1s (penalize more for larger clusters)
        w3 = 1  # weight for frequency of clusters between zeros

        penalty = (w1 * total_ones +
               w2 * sum(cluster ** 2 for cluster in clusters) +  # quadratic penalty for larger clusters
               w3 * frequency_between_zeros)
        
        return penalty
    
    def trendingAndLatestHiringSocre(self):
        pass
    


# # m=PreProcess().preprocess_Reddit_comments(AniScrappers("One Piece").fetchReviewFrom("all"))
# # print(m[0:3])
# print(r.animeListCommentsScore(["this anime is bad","this anime i s gooog"]))

