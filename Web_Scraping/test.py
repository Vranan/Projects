import requests
from bs4 import BeautifulSoup
import time

# We've now imported the two packages that will do the heavy lifting
# for us, reqeusts and BeautifulSoup

# This is the URL that lists the current inmates
# Should this URL go away, and archive is available at
# http://perma.cc/2HZR-N38X
url_to_scrape = 'https://www.investopedia.com/'

# Tell the requests package to retreive the contents our page (it'll be
# grabbing what you see when you use the View Source feature in your browser)
r = requests.get(url_to_scrape)
# We now have the source HTML of the page. Let's ask BeaultifulSoup
# to parse it for us.
soup = BeautifulSoup(r.text)
#print("Soup = ",soup)

for a_val in soup.select(".ticker"):
    print("a_val = ",a_val)
