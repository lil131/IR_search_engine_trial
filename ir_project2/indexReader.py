import whoosh.index as index
from whoosh.query import *


class MyIndexReader:
    searcher = []

    def __init__(self):
        path_dir= "data//"
        self.searcher = index.open_dir(path_dir).searcher()
        self.reader = index.open_dir(path_dir).reader()

    # Return the integer DocumentID of input string DocumentNo.
    def getDocId(self, docNo):
        return self.searcher.document_number(doc_no=docNo)

    # Return the string DocumentNo of the input integer DocumentID.
    def getDocNo(self, docId):
        return self.searcher.stored_fields(docId)["doc_no"]

    # Return DF.
    def DocFreq(self, token):
        results = self.searcher.search(Term("doc_content", token))
        return len(results)

    # Return the frequency of the token in whole collection/corpus.
    def CollectionFreq(self, token):
        results = self.searcher.search(Term("doc_content", token), limit=None)
        count = 0
        for result in results:
            words = self.searcher.stored_fields(result.docnum)["doc_content"].split(" ")
            for word in words:
                if word == token:
                    count += 1
        return count

    # Return posting list in form of {documentID:frequency}.
    def getPostingList(self, token):
        results = self.searcher.search(Term("doc_content", token), limit=None)
        postList = {}
        for result in results:
            words = self.searcher.stored_fields(result.docnum)["doc_content"].split(" ")
            count = 0
            for word in words:
                if word == token:
                    count += 1
            postList[result.docnum] = count
        return postList

    # Return the length of the requested document.
    def getDocLength(self, docId):
        words = self.searcher.stored_fields(docId)["doc_content"].split(" ")
        return len(words)

    def sumcount(self):
        docs = self.reader.all_doc_ids()
        # print(len(list(docs)))
        totalwordcount = 0

        for doc in docs:
            wor = self.searcher.stored_fields(doc)["doc_content"].split(" ")
            totalwordcount += len(wor)
        #print(totalwordcount)

        return totalwordcount
