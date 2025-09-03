# News Corpus Processing Pipeline

This repository contains a complete pipeline for **collecting, preprocessing, vectorizing, and comparing news articles (Document Similarity)** from RSS feeds.  
The pipeline consists of four main stages:

1. **Corpus Collection (Raw Data)**  
   - Extract news articles from RSS feeds (titles, descriptions, dates, sources, sections, and links).  
   - Store the raw corpus in CSV format.  

2. **Corpus Normalization**  
   - Tokenize and lemmatize text using **spaCy** (`es_core_news_sm`).  
   - Remove Spanish stop words.  
   - Store the normalized corpus in CSV format.  

3. **Vectorization & Feature Extraction**  
   - Convert normalized text into vector representations using:
     - Binary Count (Unigrams / Bigrams)  
     - Frequency Count (Unigrams / Bigrams)  
     - TF-IDF (Unigrams / Bigrams)  
   - Save vectors and vocabularies as serialized `.pkl` files.  

4. **Text Comparison (GUI Application)**  
   - A **Tkinter-based GUI** allows users to:
     - Select a text file (`.txt`) for comparison.  
     - Choose between vectorizers (TF-IDF, Frequency, Binary).  
     - Select N-gram level (Unigram, Bigram).  
     - Compare against the corpus using titles, content, or both.  

---

## Repository Structure


- Parser.py # Collects raw news articles from RSS feeds
- normalizacion.py # Normalizes text using spaCy (lemmatization + stopword removal)
- Vectorizacion.py # Vectorization (Count, TF-IDF) with unigrams & bigrams
- GUI_Document_Similarity.py # Tkinter GUI for text comparison against the corpus
- Vector.py Engine behind GUI

---
## Requirements
1. Python 3.8+
2. feedparser
3. spacy
4. scikit-learn
5. numpy
6. pandas
7. tkinter

---
## Usage
1. **Collect Raw Corpus**
   - This will fetch news from the defined RSS feeds and save them in raw_data_corpus.csv.
   ```bash
   python Parser.py

3. **Normalize Text**  
   - This will lemmatize and remove stopwords, generating normalized_data_corpus.csv.  
   ```bash
   python normalizacion.py  

4. **Vectorize Corpus**  
   - This will generate .pkl files for: Binary unigram / bigram vectors, Frequency unigram / bigram vectors & TF-IDF unigram / bigram vectors 
   ```bash
   python Vectorization.py 


5. **Use the GUI**
```bash
   python GUI_Document_Similarity.py 
