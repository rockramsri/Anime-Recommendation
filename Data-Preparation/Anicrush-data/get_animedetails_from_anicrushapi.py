# -*- coding: utf-8 -*-
"""Get AnimeDetails from AnicrushAPI.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fY53pQEeyXkta8vrhYl1bd04hJjyXKIm
"""

#!pip install boto3
#!pip install s3fs

import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import requests
import pandas as pd
from pandas import json_normalize
import boto3
import json
#from Build_Docs.FileLogger import FileLogger

class AnicrushBasicDetail:
    URL=""
    COMMENT_ENDPOINT=""
    ANIME_INFO=""
    EPISODE_INFO="shared/v2/episode/list?_movieId="
    s3=None
    defaultUrl = ""
    headers=None
    animecount=0
    INDIVIDUAL_ANIME_INFO="shared/v2/movie/getById/"

    def initialize_accessKeys(self):
      self.s3=boto3.resource(
          service_name='s3',
          region_name='ap-south-1',
          aws_access_key_id='AKIAW3MEFXW7FMKXZGXR',
          aws_secret_access_key='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'
          )
    
    def intialize_constants(self):
      self.URL="https://api.anicrush.to/"
      self.COMMENT_ENDPOINT="v1/comment/list"
      self.ANIME_INFO="shared/v2/movie/list"
      self.defaultUrl = "https://api.anicrush.to/shared/v2/movie/list?firstLetter=&limit=24&page=1"
      self.EPISODE_INFO="shared/v2/episode/list?_movieId="
      self.INDIVIDUAL_ANIME_INFO="shared/v2/movie/getById/"

    def initialize_request_headers(self):
      self.headers = {
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Referer': 'https://anicrush.to/',
        'Access-Control-Allow-Origin':'*',
        'Sec-Ch-Ua' : "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
        'Sec-Ch-Ua-Mobile':'?0',
        'Sec-Ch-Ua-Platform':"Windows",
        'X-Site':'anicrush'
        }

    def getUrlbuilderFromPageIndexAndLimit(self,limit,endpoint,page):
      return self.URL+endpoint+"?firstLetter=&limit="+str(limit)+"&page="+str(page)

    def extract_values_List(self,json_data):
      values = json_data.values()
      distinct_values = []
      for value in values:
        if isinstance(value, list):
          for item in value:
            distinct_values.append(item)
        else:
            distinct_values.append(value)
      return distinct_values
    
    def getAnimeFillerBinaryString(self,id):
      response = requests.get(self.URL+self.EPISODE_INFO+str(id), headers=self.headers)
      self.animecount+=1
      print("Anime count {}",self.animecount)
      r=""
      if 'result' in response.json():
        df=json_normalize(self.extract_values_List(response.json()['result']))
        m= df['is_filler'].values.astype(str)
        r="".join(m)
      return r
    
    def getAnimeDescriptionString(self,id):
      response = requests.get(self.URL+self.INDIVIDUAL_ANIME_INFO+str(id), headers=self.headers)
      if 'result' in response.json() and 'overview' in response.json()['result']:
        return response.json()['result']['overview']
      return ""
    
    def getDataFrameFromAnimeAPIResponse(self,animeList):
      animeListDf=json_normalize(animeList)
      animeListDf['genres'].apply(lambda x: [i['name'] for i in x])
      animeListDf['genres']=animeListDf['genres'].map(lambda x: ','.join([i['name'] for i in x]))
      print("Filler Extraction begins")
      animeListDf['fillers']=animeListDf['id'].apply(self.getAnimeFillerBinaryString)
      animeListDf['description']=animeListDf['id'].apply(self.getAnimeDescriptionString)
      return animeListDf

    def getNumberOfAnimePagesFromAPIRespone(self,response):
      try:
        print("Number of Anime pages: "+str(response['result']['totalPages']))
        return response['result']['totalPages']
      except:
        print('Error in getting number of AnimeList')
        return 0

    # default constructor
    def __init__(self):
      self.intialize_constants()
      self.initialize_accessKeys()
      self.initialize_request_headers()

    def upload_to_s3_bucket(self):
      self.s3.Bucket('anicrushdatas').upload_file(Filename='AnimeListFromAnicrush.csv',Key='AnimeListFromAnicrush.csv')
    
    # Method to get Anime Info From AniCrush and upload in S3 bucket
    def start_And_upload(self):
      defaultResponse = requests.get(self.defaultUrl, headers=self.headers)
      st=self.getUrlbuilderFromPageIndexAndLimit(int(defaultResponse.json()['result']['totalItems']),self.ANIME_INFO,1)
      animeResponse=requests.get(st, headers=self.headers)
      finalDf=self.getDataFrameFromAnimeAPIResponse(animeResponse.json()['result']['movies'])
      finalDf.to_csv('AnimeListFromAnicrush.csv', index=False, encoding='utf-8')
      self.upload_to_s3_bucket()
# logger = FileLogger("training")
# logger.log("debug", "Starting training process...")
# logger.log("info", "Training on epoch 1")
r=AnicrushBasicDetail()
r.start_And_upload()      














