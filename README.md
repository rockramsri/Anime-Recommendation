# Anime Recommendation System

This project aims to build an intelligent Anime Recommendation System using data scraped from various anime-related websites and user comments. The system preprocesses and analyzes user-generated content to derive meaningful insights, enabling personalized recommendations powered by machine learning and LLM-based retrieval-augmented generation (RAG).

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Folder Structure](#folder-structure)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

The Anime Recommendation System scrapes data from popular anime websites, including **genres, names, ratings**, and **user comments** from relevant threads. The comments are preprocessed, analyzed, and scored, which are then utilized by machine learning models for recommendations. Using a Retrieval-Augmented Generation (RAG) model, the system delivers highly personalized recommendations based on user queries and interest ratings.

---

## Features

- **Data Scraping**: Extracts comprehensive data from anime platforms, such as MyAnimeList, Reddit, and AniCrush.
- **Comment Analysis**: Preprocesses user comments to remove noise and extract meaningful insights for recommendations.
- **Machine Learning**: Employs scoring models to rank anime based on user preferences.
- **LLM Integration**: Utilizes RAG for query-based recommendations, enhancing user experience.
- **Data Cleaning**: Includes robust scripts for cleaning and preparing data for analysis.

---

## Folder Structure

```plaintext
Anime-Recommendation/
├── Build-Docs/
│   ├── DataPreparation.log          # Logs for data preparation process
│   ├── FileLogger.py                # Logging utilities
│   └── InstallHeaders               # Script for environment setup
├── Data-Preparation/
│   ├── Anicrush-data/
│   │   ├── AnimeListFromAnicrush.csv
│   │   ├── anicrushextradetails.py
│   │   └── get_animedetails_from_anicrush.py
│   ├── AnimeDataScrapper/
│   │   ├── AniScrapper.py
│   │   ├── MyAnimeList.py
│   │   ├── MyAnimeListData.csv
│   │   ├── RedditData.csv
│   │   └── RedditScrapper.py
├── Data-Preprocessing/
│   ├── pre_process_for_comment_analysis.py
│   ├── pre_processing.py
├── ML-Files/
│   ├── LLMWithCSVandVectorDB.ipynb   # Jupyter notebook for LLM integration
│   ├── score_generation.py
│   ├── score_generation_analysis.ipynb
