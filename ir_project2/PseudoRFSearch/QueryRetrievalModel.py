import Classes.Query as Query


class QueryRetrievalModel:
    indexReader = []

    def __init__(self, ixReader):
        self.indexReader = ixReader

        # self.allword = self.indexReader.sumcount()  # get the REF
        self.allword = 1864857
        self.result = []

        return

    # query:  The query to be searched for.
    # topN: The maximum number of returned documents.
    # The returned results (retrieved documents) should be ranked by the score (from the most relevant to the least).
    # You will find our IndexingLucene.Myindexreader provides method: docLength().
    # Returned documents should be a list of Document.
    def retrieveQuery(self, query, topN):
        self.probtablesmoo = {}
        postcontainer = {}
        table = {}  # the table of  each doc and q freq
        container = {}
        newpostlist = []
        postlistlen = {}
        que = query
        que = que.split()
        self.probtable = {}
        result = []
        probabily = {}
        # allword=self.indexReader.sumcount()

        for q in que:
            container[q] = {}
            if self.indexReader.DocFreq(q) != 0:
                # print(self.indexReader.DocFreq(q))
                container[q]['total_count'] = self.indexReader.CollectionFreq(q)  # total count of this word
                postlist = self.indexReader.getPostingList(q)
                postcontainer[q] = postlist
                container[q]['docfreq'] = self.indexReader.DocFreq(q)
            else:
                container[q]['total_count'] = 1
                postcontainer[q] = {}
                container[q]['docfreq'] = {}

        for q in postcontainer:
            for lis in postcontainer[q]:
                newpostlist.append(lis)

        newpostlist = list(set(newpostlist))

        for doc in newpostlist:
            postlistlen[doc] = self.indexReader.getDocLength(doc)  # store the length of each doc
        # print(postlistlen)

        for doc in newpostlist:
            table[doc] = {}
            for q in container:
                table[doc][q] = postcontainer[q].get(doc, 0)
            # table[doc][lenght] = self.indexReader.

        # smooth table
        # table is like the matrix in exam
        for doc in table:
            self.probtable[doc] = {}
            lendoc = postlistlen[doc]
            for q in table[doc]:
                countword = table[doc].get(q)
                totalkeyword = container[q]['total_count']
                self.probtable[doc][q] = self.smooth(lendoc, countword, totalkeyword)
        self.probtablesmoo = self.probtable

        for doc in self.probtable:
            prob = 1.0
            for q in self.probtable[doc]:
                prob *= self.probtable[doc].get(q)
            probabily[doc] = prob

        newprob = sorted(probabily.items(), key=lambda d: d[1], reverse=True)    # sort the rank list

        results = newprob[:topN]
        for r in results:
            resultq = Query.Query()
            docNo = self.indexReader.getDocNo(r[0])
            resultq.setDocNo(docNo)
            resultq.setScore(r[1])

            result.append(resultq)

        return result

    # smooth method
    def smooth(self, lendoc, countword, totalkeyword):
        miu = 500
        newprob = (countword + miu * (totalkeyword / self.allword)) / (lendoc + miu)
        return newprob

    def smoothprob(self):
        #print(self.probtablesmoo.keys())
        return self.probtablesmoo