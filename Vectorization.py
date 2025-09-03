from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd
import os.path
import sys
import pickle
import csv
def lectura_csv(opc): #opc será la opcion para determinar si es 1=titulo, 2=contenido o 3=titulo + contenido
    corpus = []
    with open("normalized data corpus.csv",'r',newline='',encoding='utf-8') as archivo:
        reader = csv.reader(archivo, delimiter=',')
        if(opc == 1 or opc == 2):
            for ro in reader:
                corpus.append(ro[opc])
        else:
            for ro in reader:
                corpus.append(ro[1]+" "+ro[2])
    return corpus
def binarizado_unigrama(opc, nombre="original"):
    nombre = nombre+"_binarizado_unigrama.pkl"
    if (os.path.exists(nombre)):
        print("El objeto ya existe")
        vector_archivo = open (nombre,'rb')
        X = pickle.load(vector_archivo)
    else:
        vector_archivo = open (nombre,'wb')
        vectorizador_binario = CountVectorizer(binary=True, token_pattern= r'(?u)\w+\-\w+|\w\+|\d+\.\d+\.\d+|\d+\.\d+%|\d+%|\d+\.\d+|\d+-\d+|\w+|\w+\n|\d+|\:|,|;|"|\.|\¿|\?',ngram_range = (1,1))
        corpus = lectura_csv(opc)
        X = vectorizador_binario.fit_transform(corpus)
        pickle.dump(X, vector_archivo)
        vector_archivo.close()
        vocabulario_archivo = open ("vocab_"+nombre,'wb')
        vocab = vectorizador_binario.fit(corpus)
        pickle.dump(vocab, vocabulario_archivo)
        vocabulario_archivo.close()
    return X
def binarizado_bigrama(opc, nombre="original"):
    nombre = nombre+"_binarizado_bigrama.pkl"
    if (os.path.exists(nombre)):
        print("El objeto ya existe")
        vector_archivo = open (nombre,'rb')
        X = pickle.load(vector_archivo)
    else:
        vector_archivo = open (nombre,'wb')
        vectorizador_binario = CountVectorizer(binary=True, token_pattern= r'(?u)\w+\-\w+|\w\+|\d+\.\d+\.\d+|\d+\.\d+%|\d+%|\d+\.\d+|\d+-\d+|\w+|\w+\n|\d+|\:|,|;|"|\.|\¿|\?',ngram_range = (2,2))
        corpus = lectura_csv(opc)
        X = vectorizador_binario.fit_transform(corpus)
        pickle.dump(X, vector_archivo)
        vector_archivo.close()
        vocabulario_archivo = open ("vocab_"+nombre,'wb')
        vocab = vectorizador_binario.fit(corpus)
        pickle.dump(vocab, vocabulario_archivo)
        vocabulario_archivo.close()
    return X
def frecuencia_unigrama(opc, nombre="original"):
    nombre = nombre+"_frecuencia_unigrama.pkl"
    if (os.path.exists(nombre)):
        print("El objeto ya existe")
        vector_archivo = open (nombre,'rb')
        X = pickle.load(vector_archivo)
    else:
        vector_archivo = open (nombre,'wb')
        vectorizador_frecuencia = CountVectorizer(token_pattern= r'(?u)\w+\-\w+|\w\+|\d+\.\d+\.\d+|\d+\.\d+%|\d+%|\d+\.\d+|\d+-\d+|\w+|\w+\n|\d+|\:|,|;|"|\.|\¿|\?',ngram_range = (1,1))
        corpus = lectura_csv(opc)
        X = vectorizador_frecuencia.fit_transform(corpus)
        pickle.dump(X, vector_archivo)
        vector_archivo.close()
        vocabulario_archivo = open ("vocab_"+nombre,'wb')
        vocab = vectorizador_frecuencia.fit(corpus)
        pickle.dump(vocab, vocabulario_archivo)
        vocabulario_archivo.close()
    return X
def frecuencia_bigrama(opc, nombre="original"):
    nombre = nombre+"_frecuencia_bigrama.pkl"
    if (os.path.exists(nombre)):
        print("El objeto ya existe")
        vector_archivo = open (nombre,'rb')
        X = pickle.load(vector_archivo)
    else:
        vector_archivo = open (nombre,'wb')
        vectorizador_frecuencia = CountVectorizer(token_pattern= r'(?u)\w+\-\w+|\w\+|\d+\.\d+\.\d+|\d+\.\d+%|\d+%|\d+\.\d+|\d+-\d+|\w+|\w+\n|\d+|\:|,|;|"|\.|\¿|\?',ngram_range = (2,2))
        corpus = lectura_csv(opc)
        X = vectorizador_frecuencia.fit_transform(corpus)
        pickle.dump(X, vector_archivo)
        vector_archivo.close()
        vocabulario_archivo = open ("vocab_"+nombre,'wb')
        vocab = vectorizador_frecuencia.fit(corpus)
        pickle.dump(vocab, vocabulario_archivo)
        vocabulario_archivo.close()
    return X
def tf_idf_unigrama(opc, nombre="original"):
    nombre = nombre+"_tfidf_unigrama.pkl"
    if (os.path.exists(nombre)):
        print("El objeto ya existe")
        vector_archivo = open (nombre,'rb')
        X = pickle.load(vector_archivo)
    else:
        vector_archivo = open (nombre,'wb')
        vectorizador_tf_idf = TfidfVectorizer(token_pattern= r'(?u)\w+\-\w+|\w\+|\d+\.\d+\.\d+|\d+\.\d+%|\d+%|\d+\.\d+|\d+-\d+|\w+|\w+\n|\d+|\:|,|;|"|\.|\¿|\?',ngram_range = (1,1))
        corpus = lectura_csv(opc)
        X = vectorizador_tf_idf.fit_transform(corpus)
        pickle.dump(X, vector_archivo)
        vector_archivo.close()
        vocabulario_archivo = open ("vocab_"+nombre,'wb')
        vocab = vectorizador_tf_idf.fit(corpus)
        pickle.dump(vocab, vocabulario_archivo)
        vocabulario_archivo.close()
    return X
def tf_idf_bigrama(opc, nombre="original"):
    nombre = nombre+"_tfidf_bigrama.pkl"
    if (os.path.exists(nombre)):
        print("El objeto ya existe")
        vector_archivo = open (nombre,'rb')
        X = pickle.load(vector_archivo)
    else:
        vector_archivo = open (nombre,'wb')
        vectorizador_tf_idf = TfidfVectorizer(token_pattern= r'(?u)\w+\-\w+|\w\+|\d+\.\d+\.\d+|\d+\.\d+%|\d+%|\d+\.\d+|\d+-\d+|\w+|\w+\n|\d+|\:|,|;|"|\.|\¿|\?',ngram_range = (2,2))
        corpus = lectura_csv(opc)
        X = vectorizador_tf_idf.fit_transform(corpus)
        pickle.dump(X, vector_archivo)
        vector_archivo.close()
        vocabulario_archivo = open ("vocab_"+nombre,'wb')
        vocab = vectorizador_tf_idf.fit(corpus)
        pickle.dump(vocab, vocabulario_archivo)
        vocabulario_archivo.close()
    return X
def imprimir_vector(vector, nombre="original"):
    for elemento in vector:
        print(elemento)
if __name__ == '__main__':
   x1=binarizado_bigrama(1,"titulo")
   print("binarizado bigrama con titulo")
   print(x1)
   x2=binarizado_bigrama(2,"contenido")
   print("binarizado bigrama con contenido")
   print(x2)
   x3=binarizado_bigrama(3,"titulo_contenido")
   print("binarizado bigrama con titulo + contenido")
   print(x3)
   x4=binarizado_unigrama(1,"titulo")
   print("binarizado unigrama con titulo")
   print(x4)
   x5=binarizado_unigrama(2,"contenido")
   print("binarizado unigrama con contenido")
   print(x5)
   x6=binarizado_unigrama(3,"titulo_contenido")
   print("binarizado unigrama con titulo + contenido")
   print(x6)
   x7=frecuencia_bigrama(1,"titulo")
   print("frecuencia bigrama con titulo")
   print(x7)
   x8=frecuencia_bigrama(2,"contenido")
   print("frecuencia bigrama con contenido")
   print(x8)
   x9=frecuencia_bigrama(3,"titulo_contenido")
   print("frecuencia bigrama con titulo + contenido")
   print(x9)
   x10=frecuencia_unigrama(1,"titulo")
   print("frecuencia unigrama con titulo")
   print(x10)
   x11=frecuencia_unigrama(2,"contenido")
   print("frecuencia unigrama con contenido")
   print(x11)
   x12=frecuencia_unigrama(3,"titulo_contenido")
   print("frecuencia unigrama con titulo + contenido")
   print(x12)
   x13=tf_idf_bigrama(1,"titulo")
   print("tf-idf bigrama con titulo")
   print(x13)
   x14=tf_idf_bigrama(2,"contenido")
   print("tf-idf bigrama con contenido")
   print(x14)
   x15=tf_idf_bigrama(3,"titulo_contenido")
   print("tf-idf bigrama con titulo + contenido")
   print(x15)
   x16=tf_idf_unigrama(1,"titulo")
   print("tf-idf unigrama con titulo")
   print(x16)
   x17=tf_idf_unigrama(2,"contenido")
   print("tf-idf unigrama con contenido")
   print(x17)
   x18=tf_idf_unigrama(3,"titulo_contenido")
   print("tf-idf unigrama con titulo + contenido")
   print(x18)
