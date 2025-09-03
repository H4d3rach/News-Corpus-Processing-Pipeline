from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from numpy import ndarray
import math
import pickle
import csv
import spacy

NORM_DATA_CORPUS = "normalized data corpus.csv"
TITLE = 0
CONTENT = 1
SECTION = 2

vectorizados = [(1,"tfidf"), (2,"frecuencia"), (3,"binarizado")]
ngramas = [(1,"unigrama"), (2,"bigrama")]
comparaciones = [(1,"titulo"), (2,"contenido"), (3,"titulo_contenido")]

def load_corpus():
    titles = []
    content = []
    section = []
    with open(NORM_DATA_CORPUS, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            titles.append(row['title'])
            content.append(row['content_summary'])
            section.append(row['section'])
    return [titles, content, section]

def build_vectorizers(corpus: list, cmp: str):
    vectorizador = None
    for vec in vectorizados:
        for ngram in ngramas:
            if vec[0] == 1 and ngram[0] == 1:
                vectorizador = TfidfVectorizer(token_pattern= r'(?u)\w\w+|\w\w+\n|\.|\¿|\?', ngram_range = (1,1))
            if vec[0] == 1 and ngram[0] == 2:
                vectorizador = TfidfVectorizer(token_pattern= r'(?u)\w\w+|\w\w+\n|\.|\¿|\?', ngram_range = (1,2))
            if vec[0] == 2 and ngram[0] == 1:
                vectorizador = CountVectorizer(binary=False, token_pattern= r'(?u)\w+|\w+\n|\.|\¿|\?', ngram_range=(1,1))
            if vec[0] == 2 and ngram[0] == 2:
                vectorizador = CountVectorizer(binary=False, token_pattern= r'(?u)\w+|\w+\n|\.|\¿|\?', ngram_range=(1,2))
            if vec[0] == 3 and ngram[0] == 1:
                vectorizador = CountVectorizer(binary=True, token_pattern= r'(?u)\w+|\w+\n|\.|\¿|\?', ngram_range=(1,1))
            if vec[0] == 3 and ngram[0] == 2:
                vectorizador = CountVectorizer(binary=True, token_pattern= r'(?u)\w+|\w+\n|\.|\¿|\?', ngram_range=(1,2))
            X = vectorizador.fit_transform(corpus)
            nombre_vectorizador = ("vocab_" + vec[1] + "_" + 
                                   ngram[1] + "_" + cmp + ".pkl")
            nombre_vectores = (vec[1] + "-" + ngram[1] 
                               + "-" + cmp + ".pkl")
            with open(nombre_vectorizador, 'wb') as file_vectorizer:
                pickle.dump(vectorizador, file_vectorizer)
            with open(nombre_vectores, 'wb') as file_vectors:
                pickle.dump(X, file_vectors)

def build_corpus_vectoricers():
    corpus = load_corpus()
    for item in comparaciones:
        if item[0] == 1:
            build_vectorizers(corpus[TITLE], item[1])
        elif item[0] == 2:
            build_vectorizers(corpus[CONTENT], item[1])
        elif item[0] == 3:
            new_corpus = []
            for i in range(0, len(corpus[TITLE])):
                new_corpus.append(corpus[TITLE][i] + " " + corpus[CONTENT][i])
            build_vectorizers(corpus[CONTENT], item[1])

nlp = spacy.load("es_core_news_sm")
def text_normalization(text: str):
    doc = nlp(text)
    normalized_text = []
    for token in doc:
        if not token.is_stop and not token.is_punct:
            normalized_text.append(token.lemma_.lower())
    return " ".join(normalized_text)

def cosine(test_vec: ndarray, vectors: ndarray):
    similarity = []
    for i in range(0, vectors.shape[0]):
        v = test_vec[0]
        w = vectors[i]
        val = sum(v[index] * w[index] for index in range(len(v)))
        sr_v = math.sqrt(sum(v_val**2 for v_val in v))
        sr_w = math.sqrt(sum(w_val**2 for w_val in w))
        if sr_v == 0 or sr_w == 0:
            res = 0
        else:
            res = val/(sr_v*sr_w)
        similarity.append(res)
    return similarity
        

def compare_text(text: str, options: dict):
    name_vectorizer = ("vocab_" + comparaciones[options["comparaciones"]][1] + "_" + 
                       vectorizados[options["vectorizados"]][1] + "_" + ngramas[options["ngramas"]][1]
                       + ".pkl")
    name_vectors = (comparaciones[options["comparaciones"]][1] + "_" + 
                    vectorizados[options["vectorizados"]][1] + "_" + ngramas[options["ngramas"]][1]
                    + ".pkl")
    vectorizer = None
    vectors = None
    with open(name_vectorizer, "rb") as file:
        vectorizer = pickle.load(file)
    with open(name_vectors, "rb") as file:
        vectors = pickle.load(file)
    text = text_normalization(text)
    test_vector = vectorizer.transform([text])
    return cosine(test_vector.toarray(), vectors.toarray())

def list_comparations(comparation: ndarray, options: dict):
    corpus = load_corpus()
    table = [["Documento", "Representacion vectorial", "Caracteristicas extraidas", "Elemento de comparacion", "Similaridad"]]
    for index in range(0, len(corpus[1])):
        row = []
        if options["comparaciones"] == 0:
            row.append(corpus[TITLE][index])
        elif options["comparaciones"] == 1:
            row.append(corpus[CONTENT][index])
        elif options["comparaciones"] == 2:
            row.append(corpus[TITLE][index] + " " + corpus[CONTENT][index])
        row.append(vectorizados[options["vectorizados"]][1])
        row.append(ngramas[options["ngramas"]][1])
        row.append(comparaciones[options["comparaciones"]][1])
        row.append(comparation[index])
        table.append(row)
    with open('comparaciones.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(table)
        
def prubas():
    corpus = load_corpus()
    table = [["Nombre TXT", "Documento", "Representacion vectorial", "Caracteristicas extraidas", "Elemento de comparacion", "Similaridad"]]
    documents_path = ["./Pruebas 1/América_titulo-contendio-nuevo.txt", "./Pruebas 1/Bellas Artes_recorte.txt", "./Pruebas 1/Inversión_contenido.txt", "./Pruebas 1/Inversión_contenido.txt", "./Pruebas 1/Pemex_título.txt", "./Pruebas 1/Xiaomi_título-contenido.txt"]
    for path in documents_path:
        text = ""
        with open(path, mode="r", encoding="utf-8") as file:
            text = file.read()
        text = text_normalization(text)
        for vec in vectorizados:
            for ngram in ngramas:
                for comp in comparaciones:
                    row = []
                    a = {"vectorizados": vec[0]-1, "ngramas": ngram[0]-1, "comparaciones": comp[0]-1}
                    similarity = compare_text(text, a) # Comparacion de texto
                    for index in range(0, len(corpus[1])):
                        row = []
                        row.append(path)
                        if comp[0]-1 == 0:
                            row.append(corpus[TITLE][index])
                        elif comp[0]-1 == 1:
                            row.append(corpus[CONTENT][index])
                        elif comp[0]-1 == 2:
                            row.append(corpus[TITLE][index] + " " + corpus[CONTENT][index])
                        row.append(comp[1])
                        row.append(ngram[1])
                        row.append(comparaciones[1])
                        row.append(similarity[index])
                        print(row)
                        table.append(row)
    with open('pruebas.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(table)
                    
# prubas()