import csv
import spacy
def normalizacion(nlp):
    stop_words = ['el', 'la', 'los', 'las','un', 'una', 'unos', 'unas','a', 'de', 'en', 'con', 'por', 'para', 'según','ante', 'bajo', 'cabe', 'contra', 'desde', 'hacia', 'hasta','sin','tras', 'vía','mí', 'ti', 'él', 'ella', 'nosotros', 'vosotros', 'ellos', 'ellas', 'sí', 'aquel', 'aquella', 'aquellos', 'aquellas','me', 'te', 'se', 'nos', 'os', 'lo', 'la', 'los', 'las', 'le', 'les', 'quien', 'quienes', 'que', 'cual', 'cuales', 'cuyo', 'cuyos', 'cuya', 'cuyas', 'qué', 'quién', 'quienes', 'cuál', 'cuáles', 'ello','esto','aquello','y', 'o', 'pero', 'sino','aunque', 'porque','si', 'pues', 'así', 'mientras', 'cuando', 'donde', 'aunque', 'luego', 'siquiera', 'bien', 'mal','e', 'u', 'ni', 'mas', 'sino', 'que', 'como', 'pues', 'cuanto', 'tanto', 'tal', 'así', 'antes', 'después', 'mientras', 'bien', 'mal', 'adonde', 'cuándo','al','del','yo','tu','tú','este','ese','aquel','estos','aquellos']
    with open('./raw_data_corpus.csv','r',newline='',encoding='utf-8') as archivo:
        reader = csv.reader(archivo, delimiter=',')
        lectura = []
        for row in reader:
            lectura.append(row)
        conter = 0
        for lect in lectura:
            if conter == 0:
                conter = 1
                continue
            doc_title = nlp(lect[1])
            doc_noticia = nlp(lect[2])
            cadena1 = ""
            cadena2 = ""
            for title_token in doc_title:
                if stop_words.count(str(title_token).lower()) > 0:
                    continue
                cadena1=cadena1+" "+str(title_token.lemma_)
            for noticia_token in doc_noticia:
                if stop_words.count(str(noticia_token).lower()) > 0:
                    continue
                cadena2=cadena2+" "+str(noticia_token.lemma_)
            lectura[conter][1] = cadena1
            lectura[conter][2] = cadena2
            conter = conter + 1
        return lectura
def escritura(data):
    with open('./normalized_data_corpus.csv','w',newline='',encoding='utf-8') as archivo:
        writer = csv.writer(archivo,delimiter=',')
        writer.writerows(data)
if __name__ == '__main__':
    nlp = spacy.load("es_core_news_sm")
    data = normalizacion(nlp)
    escritura(data)