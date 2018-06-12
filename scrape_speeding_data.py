"""
Scrape speeding data from a website

Python 3 only
"""

import urllib
from bs4 import BeautifulSoup

url = "https://ontariospeeding.com/speeding-ticket-penalties/speeding-ticket-fines/"

# Site hates bots, so pretend we are using firefox
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
page = urllib.request.urlopen(req)
soup = BeautifulSoup(page)
with open("speeding_data.csv", "w") as f:
    fmt_str = "{},{},{}\n"
    f.write(fmt_str.format("speed", "fine", "demerit_pts"))
    for tr in soup.find_all('tr')[1:]:
        tds = tr.find_all('td')
        f.write(fmt_str.format(*[t.text for t in tds]))

# Note: a tiny bit of manual cleanign was done for this file afterwards
