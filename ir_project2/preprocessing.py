from nltk.stem.snowball import EnglishStemmer
from nltk.corpus import stopwords
import nltk
#nltk.download('stopwords')
f = open('irdata.txt', 'r')
wr = open('preprocessdata.txt','w')
line = f.readline()
docNo = ""
content = ""
store = {}
stemmer2 = EnglishStemmer()
STOPWORDS = set(stopwords.words('english'))

while line:
    if '<content>' in line:
        line = line.split()
        content = line[1:-1]
        normalContent = ''
        for word in content:
            word = ''.join(e for e in word if e.isalnum())
            word = word.lower()
            stem_word = stemmer2.stem(word)
            if stem_word not in STOPWORDS:
                normalContent += (stem_word + ' ')
        wr.write(normalContent + '\n')

    if '<titleid>' in line:
        linelist = line.split()
        docNo = linelist[1][:9]  # the content in the second place is the docno
        wr.write(docNo + '\n')        # print(docNo)
    line = f.readline()


f.close()
wr.close()