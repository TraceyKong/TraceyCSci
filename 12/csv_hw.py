import csv

def inverted_index_reader(l):
    f = open(l)
    data =  [line for line in csv.reader(f)]
    f.close()
    wordList= {}
    for word in [w for wl in data for w in wl[1].split(' ')]:
        wordList.setdefault(word,[line[0] for line in data if word in line[1]])
    return wordList
    
def reader_searcher(searchWord,d):
    if searchWord in d.keys():
        for l in d[searchWord]:
            print(l)
        return
    print('no result')

def inverted_index_dict(l):
    file = open(l)
    f = csv.DictReader(file)
    headers = f.fieldnames
    doc = [line for line in f]
    file.close()
    d = {}
    for i in headers[1:]:
        temp = {}
        for j in doc:
            temp.setdefault(j[i],[])
            temp[j[i]].append(j["Execution #"])
        d.setdefault(i,temp)
    return d
    
def dict_reader_searcher(attribute,searchWord,d):
    if attribute in d.keys():
        temp = d[attribute]
        if searchWord in temp.keys():
            for l in temp[searchWord]:
                print(l)
            return
    print('no result')

sample_text = inverted_index_reader("sample-texts.csv")
offenders_clean = inverted_index_dict("offenders-clean.csv")