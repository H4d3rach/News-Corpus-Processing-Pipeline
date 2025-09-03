import feedparser
import re
import csv
def get_rss(url):
    rss = feedparser.parse(url)
    division=re.split("[\-:]",rss.feed.title)
    source = division[0]
    section = division[1]
    lista = []
    for entrada in rss.entries:
        title = entrada.title
        description = entrada.description
        pubdate = str(entrada.published_parsed[2])+"/"+str(entrada.published_parsed[1])+"/"+str(entrada.published_parsed[0])
        link = entrada.link
        lista.append([source,title,description,section,link,pubdate])
    return lista
def corpus_raw_operation(corpus_list):
    header = ["Source", "Title", "Content", "Section", "URL", "Date"]
    with open('./raw_data_corpus.csv','r',newline='',encoding='utf-8') as archivo:
        reader = csv.reader(archivo, delimiter=',')
        lectura = []
        for ro in reader:
            lectura.append(ro)
        if len(lectura) == 0:
            lectura.insert(0,header)
        elif lectura[0] != header:
            lectura.insert(0,header)
        for first in corpus_list:
            for second in first:
                for third in lectura:
                    if second[1] == third[1]:
                        conter = 0
                        break
                    else:
                        conter = 1
                if conter == 1:
                    lectura.append(second)
    with open('./raw_data_corpus.csv','w',newline='',encoding='utf-8') as archivo:
        writer = csv.writer(archivo,delimiter=',')
        writer.writerows(lectura)
if __name__ == '__main__':
    url = 'https://www.jornada.com.mx/rss/economia.xml?v=1'
    url2 = 'https://expansion.mx/rss/economia'
    url3 = 'https://www.jornada.com.mx/rss/ciencias.xml?v=1'
    url4 = 'https://expansion.mx/rss/tecnologia'
    url5 = 'https://www.jornada.com.mx/rss/deportes.xml?v=1'
    url6 = 'https://www.jornada.com.mx/rss/cultura.xml?v=1'
    url_colection = [url,url2,url3,url4,url5,url6]
    corpus_list = []
    for u in url_colection:
        corpus_list.append(get_rss(u))
    corpus_raw_operation(corpus_list)