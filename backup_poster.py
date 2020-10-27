"""
This script will do the following:
- Check to see if a post has been published today.
- If not, then it will post one.
"""

import urllib.request
import bs4 as bs
import datetime

def posted_today():
    """
    See if sites rss feed has a post with today's date
    :return: Boolean
    """
    resp = urllib.request.urlopen("https://tedslocum.com/feed.xml").read()
    soup = bs.BeautifulSoup(resp, "lxml")
    publish_date_string = soup.find('channel').find('item').find('pubdate').text
    publish_date = datetime.datetime.strptime(publish_date_string, '%a, %d %b %Y %H:%M:%S %z').date()
    today_date = datetime.date.today()

    return publish_date == today_date

print(posted_today())


