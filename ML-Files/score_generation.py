from ast import List
import pandas as pd
from transformers import pipeline

class ScoreGeneration:
    commentPipline=None
    def __init__(self, modelName="siebert/sentiment-roberta-large-english") -> None:
        self.commentPipline=pipeline("sentiment-analysis",model=modelName,tokenizer=modelName)
    def animeListCommentsScore(self,comments: List[str]):
        scoresMapList=self.commentPipline(comments)
        avgScore=0
        if scoresMapList!=None:
            for score in scoresMapList:
                if "POSITIVE"==score["label"]:
                    avgScore+=score["score"]
                else:
                    avgScore+=(1-score["score"])
            avgScore/=len(scoresMapList)
        return round(avgScore,3)
    def fillerPatternScore(self,fillerStr: str):
        pass
    def trendingAndLatestHiringSocre(self):
        pass
    




