import csv

f = open("sample-texts.csv")
sampleText = [line for line in csv.reader(f)]
f.close()
f = open("offenders-clean.csv")
offendersClean = [line for line in csv.DictReader(f)]
f.close()

def inverted_index_reader(l):
    wordList= {}
    for word in [w for wl in l for w in wl[1].split(' ')]:
        wordList.setdefault(word,[line[0] for line in l if word in line[1]])
    return wordList

def inverted_index_dict(l):
    return l
    

reader = inverted_index_reader(sampleText)
dreader = inverted_index_dict(offendersClean)