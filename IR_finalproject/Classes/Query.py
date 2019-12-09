class Query:

    def __init__(self):
        return

    queryContent = ""
    topicId = ""

    docNo = ''
    score = ''

    def getQueryContent(self):
        return self.queryContent

    def getTopicId(self):
        return self.topicId

    def setQueryContent(self, content):
        self.queryContent = content

    def setTopicId(self, id):
        self.topicId = id

    def getDocNo(self):
        return self.docNo

    def getScore(self):
        return self.score

    def setDocNo(self, docno):
        self.docNo = docno

    def setScore(self, score):
        self.score = score
