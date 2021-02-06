import sys
import urllib.request
import urllib.parse
import json

def getWikiLink(searchString):
    params={'action':'opensearch', 'search':searchString, 'limit':'10', 'namespace':'0', 'format':'json'}
    webUrl = urllib.request.urlopen("https://en.wikipedia.org/w/api.php?"+urllib.parse.urlencode(params))
    webUrlCode=webUrl.getcode()
    if webUrlCode==200:
        web_data=webUrl.read()
        json_data=json.loads(web_data)
        return(json_data[3][0])
    else:
        return('Response code: ' +webUrlCode)

def writeLinkToFile(link, filename):
    file=open(filename, "a")
    file.write(link+"\n")
    file.close()

def readAllLinks(filename):
    file=open(filename, "r")
    print(file.read())
    file.close()

if __name__=='__main__':
    searchKey=''
    filename='logWikipediaLinks.txt'
    if len(sys.argv)==1:
        searchString=input("What do you wanna search about? Mention it here:-\n")
    else:
        searchString=' '.join(sys.argv[1:])
    link=getWikiLink(searchString)
    writeLinkToFile(link, filename)
    print("Link added to the logs.")
    choice=input("Would you like to see the logs?(y/n)")
    if choice=="y":
        readAllLinks(filename)
