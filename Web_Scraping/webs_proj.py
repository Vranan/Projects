#C:\Users\b57222\Documents\1-gitVranan\Python_codes

from bs4 import BeautifulSoup as bs
import time
import re
import urllib3 as ul3
import re

site = ul3.PoolManager()
# url1 = 'https://en.wikipedia.org/wiki/Tourism_in_India_by_state/'
url = 'http://www.thrillophilia.com/blog/beautiful-places-in-india/'
response = site.request('GET',url)
soup = bs(response.data,"lxml")
# site_r = site.read()


# spn = soup.name
# print("Printing the name of the soup -- %s\n" %spn)
# sph = soup.head.contents
# print("Soup head contents- \n%s \n\n" %(sph))
# print("length of the soup.head.contents -- %d \n\n" %(len(sph)))
# print(soup.prettify())
# with open("wiki.html","r") as wk:
#    soup = bs(wk,"lxml")
# print(soup.prettify())
states = soup.find_all("b")
# st = states.find_all(class_="mw-headline")
#print(states)
#for st in states:
#    print(st)
print("------------------------------------------------------------------- \n")
print(type(states))
print("------------------------------------------------------------------- \n")
#print(st)
print(states[1])
print("------------------------------------------------------------------- \n")
for st in states:
    #ln = len(list(st.contents))
    #print("length = %d \n" %ln)
    stri = st.get_text()
    for s in stri.split():
        if regexm(s,"*[a-zA-Z]*")==True:
            print(s)
        #if isinstance(s,str)==True:
        #    print(s)
    #print(type(st.get_text()))
    #if st.get_text() != "":
    #    print(st.get_text())
        #print(st['img'])
    #if (st.img == True):
        #print("The child is an image.")
    #print(st)

# print("\n\n printing the states = %s " %states)


#a = soup.get_text()
#print("Type of soup.get_text() = %s \n\n" %type(a))
#print("printing the text %s \n\n" %a)
#for tag in soup.findAll("p"):
#    print(tag)


# for child in soup.head.children:
#    print(child)
# var = soup.find("li",{"id":"title"})
# print(var)
b = soup.findAll('script')
#print(b)
#for link in b:
#    print(link)

# -------------------------------------------------------------------
# Some trials in the process.
# -------------------------------------------------------------------

# Redirecting the output to an output file
# from pprint import pprint as pp
# with open('output.txt','wt') as out:
# pprint(soup.prettify(), stream=out)

# Using response for extracting the information from a package
# import requests
# r = requests.get(url_to_scrape)
# soup1 = BeautifulSoup(r.text)

# Using regular expressions in the soup.finall command.
# for tag in soup.find_all(re.compile("^a")):
#    tgn = tag.children[0]
#    print("tag = %s and tag.name = %s" %(tag, tgn))
