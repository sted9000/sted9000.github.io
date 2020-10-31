"""
This script will do the following:
- Check to see if a post has been published today.
- If not, then it will post one.
"""

import urllib.request
import bs4 as bs
import datetime
from git import Repo
from pathlib import Path

Path = Path('.')


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


def publish_post():
    """
    Pushes a new post
    :return: No return
    """
    repo = Repo(Path)
    repo.index.add([str(Path / 'daily' / '_posts' / f'{post_date}-{draft_to_publish.name}')])
    repo.index.commit(f'new post {post_date}')
    origin = repo.remote('origin')
    origin.push()


def choose_draft():
    drafts = [x for x in (Path / '_drafts').iterdir()]

    return drafts[0]


def format_draft():
    with open((Path / 'daily' / '_posts' / f'{post_date}-{draft_to_publish.name}'), 'x') as f:
        f.write('---\n')
        f.write(f'date: {post_date}\n')
        f.write(f'layout: {post_layout}\n')
        f.write(f'author: {post_author}\n')
        f.write(f'title: {post_title}\n')
        f.write(f'tags: {post_tag}\n')
        f.write('---\n')

        with open((Path / draft_to_publish), 'r') as d:
            for line in d:
                f.write(line)


draft_to_publish = choose_draft()
post_date = datetime.datetime.now().strftime('%Y-%m-%d')
post_layout = 'post'
post_author = 'Ted'
ff_length = 3 if '.md' in draft_to_publish.name else 4  # accounts for .md and .txt
post_title = 'Backup Post' + ' - ' + draft_to_publish.name[:-ff_length].replace('-', ' ')
post_tag = 'backup'

if __name__ == '__main__' and not posted_today():
    format_draft()
    publish_post()
    print('Backup published')
