import sys
import time
from progress.bar import Bar
import wikipediaapi

def WikiPedia(item,logfile):
    SearchTerm = item.lower()
    wiki_wiki = wikipediaapi.Wikipedia('en') 
    page_py = wiki_wiki.page(SearchTerm)

    with open(logfile, 'a') as file:
        file.write(page_py.fullurl + "\n")

    bar = Bar('Appending Wikipedia Link...', max = 100)    
    for i in range(100):
        bar.next()
        time.sleep(0.01)
    bar.finish()
    print("Wikipedia link for " + item + " added to " + logfile + '\n')


if __name__=="__main__":
    if (len(sys.argv)==1):
        searchTerm = input("Enter search item: ")
        LogFile = input("Enter logfile name: ")
        WikiPedia(searchTerm,LogFile)

    else:
        searchTerm = sys.argv[1]
        LogFile = sys.argv[2] 
        WikiPedia(searchTerm,LogFile) 