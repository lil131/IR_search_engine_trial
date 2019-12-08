import csv

class createBase:
    def __init__(self):
        self.database = {}
        self.csv_file = csv.reader(open('datahouse.csv','r'))
        for line in self.csv_file:
            self.database[line[0]] = line[1:]
        #self.csv_file.close()
        return
