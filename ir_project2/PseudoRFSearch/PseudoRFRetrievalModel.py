import Classes.Query as Query
import PseudoRFSearch.QueryRetrievalModel as original


class PseudoRFRetreivalModel:
    indexReader = []

    def __init__(self, ixReader):
        self.indexReader = ixReader
        self.search = original.QueryRetrievalModel(self.indexReader)
        self.oritable = {}
        return


    def retrieveQuery(self, query, topN, topK, alpha):

        newtable = {}
        newrank = {}

        TokenRFScore = self.GetTokenRFScore(query, topK)
        for doc in self.oritable:                            # grt the table of the probability of each term in each docid
            newtable[doc] = {}
            # prob = 1.0
            for q in self.oritable[doc]:
                newtable[doc][q] = alpha * self.oritable[doc].get(q) + (1 - alpha) * TokenRFScore.get(q)

        for doc in newtable:
            prob = 1.0
            for q in newtable[doc]:
                prob *= newtable[doc].get(q)
            newrank[doc] = prob
        newprob = sorted(newrank.items(), key=lambda d: d[1], reverse=True)
        newtop = newprob[:topN]
        # sort all retrieved documents from most relevant to least, and return TopN
        results = []
        for r in newtop:
            resultq = Query.Query()
            docNo = self.indexReader.getDocNo(r[0])
            resultq.setDocNo(docNo)
            resultq.setScore(r[1])

            results.append(resultq)

        return results

    def GetTokenRFScore(self, query, topK):
        TokenRFScore = {}

        relevent = self.search.retrieveQuery(query, topK)       # use hw3 get relevant feedback
        rflen = 0
        q_rf = {}
        sumrfq = {}
        que = query
        que = que.split()
        idlist = []

        for result in relevent:                     # get the list of relevant docid
            id = result.getDocNo()
            id = self.indexReader.getDocId(id)
            rflen += self.indexReader.getDocLength(id)
            idlist.append(id)

        for i in que:
            qfreq = 0
            qrf = self.indexReader.getPostingList(i)
            for id in idlist:
                qfreq += qrf.get(id, 0)  # query term's freq in pesudo doc
            if qfreq == 0:  # to deal with dysohagia
                qfreq = 1
            score = self.search.smooth(rflen, qfreq, self.indexReader.CollectionFreq(i))  # func from hw3
            TokenRFScore[i] = score

        self.oritable = self.search.smoothprob()
        # print(TokenRFScore)
        return TokenRFScore
