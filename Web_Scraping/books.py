#C:\Users\b57222\Documents\1-gitVranan\Python_codes
from bs4 import BeautifulSoup as bs
import time
import re
#import urllib2

with open("ex.html","r") as ex:
    soup = bs(ex,"lxml")
print(soup.prettify())
cont = soup.find("ul")

print("\n Printing the string value = %s \n" %cont.li.div.string)
