import pandas as pd
import numpy as np
import spacy
sp=spacy.load("en_core_web_lg")

class PreProcess:
    def preprocess_for_NLP(self,text):
        modText=sp(text)
        if modText!=None and len(modText)!=0:
            text=" ".join([word.lemma_ for word in modText if not (word.is_stop or word.is_punct or word.is_quote or word.is_space)])
        return text.lower()
    def preprocess_MyAnimeList_Comments(self,myAnimeData):
        myAnimeData.drop(columns=['name','animeName'],inplace=True)
        myAnimeData.dropna(inplace=True)
        animeData = myAnimeData["Review"].apply(self.preprocess_for_NLP)
        return animeData
    def preprocess_Reddit_comments(self,redditData):
        redditData.drop(columns=['name','Reddit_Title'],inplace=True)
        redditData.dropna(inplace=True)
        animeData = redditData["Review"].apply(self.preprocess_for_NLP)
        return animeData
    


