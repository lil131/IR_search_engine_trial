import indexReader as MyIndexReader
from nltk.stem.snowball import EnglishStemmer
from nltk.corpus import stopwords
import PseudoRFSearch.PseudoRFRetrievalModel as PseudoRFRetrievalModel
import PseudoRFSearch.QueryRetrievalModel as original
import database.createBase as createdb
import json
import nltk
nltk.download("stopwords")

# index = MyIndexReader.MyIndexReader()
# pesudo_search = PseudoRFRetrievalModel.PseudoRFRetreivalModel(index)
# originalsearch = original.QueryRetrievalModel(index)
# base = createdb.createBase()
# database = base.database
# query = 'harry potter destroy Voldemort'
#
# stemmer2 = EnglishStemmer()
# STOPWORDS = set(stopwords.words('english'))
#
# def normalQuery(query):
#     query = query.split()
#     normal = ''
#     for word in query:
#         print(word)
#         word = ''.join(e for e in word if e.isalnum())
#         word = word.lower()
#         stem_word = stemmer2.stem(word)
#
#         if stem_word not in STOPWORDS:
#             normal += (stem_word + ' ')
#     return normal
#
# newq = normalQuery(query)
# print(newq)
#
# results = pesudo_search.retrieveQuery(query, 10, 2, 0.4)
# relevent = originalsearch.retrieveQuery(query, 10)
# rank = 0
# for result in relevent:
#     no = result.getDocNo()
#     print(newq, ' ', rank, ' ', database[no])
#     rank += 1


class searchmov:

    # query = 'harry potter destroy Voldemort'
    def __init__(self):
        self.stemmer2 = EnglishStemmer()
        self.STOPWORDS = set(stopwords.words('english'))
        index = MyIndexReader.MyIndexReader()
        self.pesudo_search = PseudoRFRetrievalModel.PseudoRFRetreivalModel(
            index)
        self.originalsearch = original.QueryRetrievalModel(index)
        base = createdb.createBase()
        self.database = base.database

    def normalQuery(self, query):
        query = query.split()
        normal = ''
        for word in query:
            print(word)
            word = ''.join(e for e in word if e.isalnum())
            word = word.lower()
            stem_word = self.stemmer2.stem(word)

            if stem_word not in self.STOPWORDS:
                normal += (stem_word + ' ')
        return normal

    def searchmovie(self, query):
        newq = self.normalQuery(query)
        print(newq)

        results = self.pesudo_search.retrieveQuery(newq, 10, 2, 0.4)
        relevent = self.originalsearch.retrieveQuery(newq, 20)
        rank = 0
        response = []
        for result in relevent:
            no = result.getDocNo()
            res = {}
            res['id'] = no
            res['name'] = self.database[no][0]
            res['rating'] = self.database[no][1]
            res['description'] = self.database[no][2]
            res['storyline'] = self.database[no][3]
            res['imdbURL'] = self.database[no][4]
            res['poster'] = self.database[no][5]
            res = json.dumps(res)
            print(res)
            #print(newq, ' ', rank, ' ', database[no])
            response.append(res)
            rank += 1
        return response

    def searchonemovie(self, no):
        res = {}
        res['id'] = no
        res['name'] = self.database[no][0]
        res['rating'] = self.database[no][1]
        res['description'] = self.database[no][2]
        res['storyline'] = self.database[no][3]
        res['imdbURL'] = self.database[no][4]
        res['poster'] = self.database[no][5]
        res = json.dumps(res)
        return res


query = 'harry'
# search = searchmov()
# print(search.searchmovie(query))

def run(query):
    search = searchmov()
    return search.searchmovie(query)

def runOne(id):
    search = searchmov()
    return search.searchonemovie(id)
