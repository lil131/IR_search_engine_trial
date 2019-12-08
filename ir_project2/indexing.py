import indexWriter as MyIndexWriter

corpus = open('preprocessdata.txt', "r", encoding="utf8")
indexWriter = MyIndexWriter.indexWriter()
count = 0
# line = corpus.readline()
# while line:
#     docNo = line.strip('\n')
#     line = corpus.readline()
#     content = corpus.readline().strip('\n')
def nextDoc():
    docNo = corpus.readline().strip('\n')
    if docNo == "":
        corpus.close()
        return
    content = corpus.readline().strip('\n')
    return [docNo, content]

while True:
    doc = nextDoc()
    if doc == None:
        break
    print(doc[0])
    indexWriter.index(doc[0], doc[1])
    count += 1
    if count % 30000 == 0:
        print("finish ", count, " docs")
print("totally finish ", count, " docs")
indexWriter.close()

