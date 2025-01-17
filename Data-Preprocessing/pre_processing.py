import pandas as pd
import numpy as np
import spacy


class PreProcess:
    sp=None
    def __init__(self):
        self.sp=spacy.load("en_core_web_lg")
    def preprocess_for_NLP(self,text):
        if isinstance(text, bytes):
            text = text.decode('utf-8')
        modText=self.sp(text)
        if modText!=None and len(modText)!=0:
            text=" ".join([word.lemma_ for word in modText if not (word.is_stop or word.is_punct or word.is_quote or word.is_space)])
        return text.lower()
    def preprocess_MyAnimeList_Comments(self,myAnimeData):
        try:
            myAnimeData.drop(columns=['name','animeName'],inplace=True)
            myAnimeData.dropna(inplace=True)
            animeData = myAnimeData["Review"].apply(self.preprocess_for_NLP)
            return animeData
        except:
            return []
    def preprocess_Reddit_comments(self,redditData):
        try:
            redditData.drop(columns=['name','Reddit_Title'],inplace=True)
            redditData.dropna(inplace=True)
            animeData = redditData["Review"].apply(self.preprocess_for_NLP)
            return animeData
        except:
            return []


