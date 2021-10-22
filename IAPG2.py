import urllib.request
from bs4 import BeautifulSoup
import datetime

right_now = datetime.datetime.now().isoformat()          
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))


def retrieveitemcollections(url):

    try:

        html = urllib.request.urlopen(url)
        html = html.read()

        soup = BeautifulSoup(html,"html.parser")

        tags = soup('a')

        collist = []

        for tag in tags:
            atag = tag.get('href', None)

            #if '@' not in str(atag) and 'netlabel' not in str(atag) and 'forum' not in str(atag) and 'post' not in str(atag) and 'creativecommons' not in str(atag) and '#' not in str(atag):
            if "details" in str(atag) and '@' not in str(atag) and 'archive.org' not in str(atag) and 'netlabels' not in str(atag):
                dref = 'https://archive.org/' + str(atag)
                if dref not in collist:
                    collist.append(dref)

        return(collist)

    except:
        nost = []
        return nost

def retrieveitems(url):

    try:
            
        html = urllib.request.urlopen(url)
        html = html.read()

        soup = BeautifulSoup(html,"html.parser")

        tags = soup('a')

        itmlist = []

        for tag in tags:
            atag = tag.get('href', None)

            #if '@' not in str(atag) and 'netlabel' not in str(atag) and 'forum' not in str(atag) and 'post' not in str(atag) and 'creativecommons' not in str(atag) and '#' not in str(atag):
            atext = str(atag)
            if "details" in atext and '@' not in atext and 'archive.org' not in atext  and 'sort' not in atext and 'tab' not in atext and 'morf' not in atext and 'opensource' not in atext:
                dref = 'https://archive.org' + str(atag)
                if dref not in itmlist:
                    itmlist.append(dref)

        del itmlist[0]

        return(itmlist)

    except:
        nolst = []
        return(nolst)

def retrievemp3links(url):

    try:

        html = urllib.request.urlopen(url)
        html = html.read()

        soup = BeautifulSoup(html,"html.parser")

        tags = soup('a')

        tracklist = []

        for tag in tags:
            atag = tag.get('href', None)

            if '.mp3' in str(atag):
                dref = 'https://archive.org' + str(atag)
                if dref not in tracklist:
                    tracklist.append(dref)

        return(tracklist)

    except:
        nost = []
        return nost

print("")

print("Welcome to the IAPG2. Links are fetched to tracks in genres you choose.")

print("")

subcoll = input("Please enter the collection: ")

print("")

if not subcoll:
    subcoll = 'netlabels'

suba = input("Please enter the first genre: ")

print("")

subb = input("Please enter the second genre. Please press enter if no second genre: ")

print("")

subc = input("Please enter the number of iterations, from 2 to 10: ")

print("")

if suba and subb:

    collur = 'https://archive.org/details/' + subcoll + '?query=' + suba + '%2C+' + subb + 'sort=-week'

if suba and not subb:

    collur = 'https://archive.org/details/netlabels?query=' + suba 

collst = retrieveitemcollections(collur)

print("")

print(collst)

abrcol = []

iter = int(subc)

for ctr in range(iter):
    abrcol.append(collst[ctr])

print("")

totlst = []

for elem in abrcol:
    print("")
    print(elem)
    ans =  retrieveitems(elem)
    if ans not in totlst and len(ans) > 0:
        totlst.append(ans)
        #print(ans)

print("")
print(totlst)

trklist = []

for elem in totlst:
    for elem2 in elem:
        print("")
        print(elem2)
        trkl = retrievemp3links(elem2)
        if len(trkl) > 0:
            trklist.append(trkl)
            print("")
            print(trkl)

print("")
print(trklist)

oufil = 'IAPG2' + suba + "_" + subb + '_' + tim + ".m3u"

outfile = open(oufil, "w")

for elem in trklist:

    for elem2 in elem:

        outfile.write(elem2 + '\n')

outfile.close()

print("")

print("Your playlist is available in the same folder as the source code. Thank you.")

print("")
