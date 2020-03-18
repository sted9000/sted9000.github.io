from pathlib import Path
import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import subprocess
PIPE = subprocess.PIPE
now = datetime.datetime.now()


Path = Path('.')
author = 'Ted'
tags = ['health', 'people', 'random', 'mindfulness', 'attention', 'bullshit', 'compassion', 'beauty', 'freeroll', 'bias', 'wonder', 'tech', 'finance', 'crypto', 'prediction', 'idea', 'language', 'communication', 'relationships', 'books', 'professional', 'emotions', 'reason', 'productivity', 'harris', 'brooks', 'weinstein']

### list drafts
drafts = [x for x in (Path / '_drafts').iterdir()]
print('Drafts: ')
for i, x in enumerate(drafts):
    print(str(i), ' - ', x.parts[1])

### select draft
user_draft = input('Enter Draft #: ')
draft_to_publish = drafts[int(user_draft)].parts[1]
print()
print(draft_to_publish)

### header data
user_use_tags = input('Do you want to add tags(y)? ')
# tags
tags_for_post = None
if user_use_tags == 'y':
    for i, tag in enumerate(tags):
        print(str(i), ' - ', tag)
    user_tags_string = input('Enter Tag # (ex: 2,3,4): ')
    user_tags_list = user_tags_string.split(',')
    tags_for_post = [tags[int(x)] for x in user_tags_list]

# date
date = now.strftime('%Y-%m-%d')
# layout
layout = 'post'
# title
title_list = draft_to_publish[:-3].split('-')
title = ''
for word in title_list:
    title += word
    title += ' '

print()
user_title_input = input(f'Correct Title(y): {title}? ')
if user_title_input == 'y':
    new_title = title
else:
    new_title = input('Please input new title: ')


### write md file
f = open((Path / 'daily' / '_posts' / draft_to_publish), 'x')
f.write('---\n')
f.write(f'layout: {layout}\n')
f.write(f'author: {author}\n')
f.write(f'title: {new_title}\n')
if tags_for_post != None:
    f.write('tags: ')
    for i, tag in enumerate(tags_for_post):
        if i+1 != len(tags_for_post): f.write(tag + ' ')
        else: f.write(tag)
f.write('---\n')
d = open((Path / '_drafts' / draft_to_publish), 'r')
for line in d:
    f.write(line)
f.close()

pull = subprocess.Popen(["git", "pull"], stdout=PIPE, stderr=PIPE)
stdoutput, stderroutput = pull.communicate()

if b'fatal' in stdoutput:
    print("Fatal error in pull, aborting script")
    sys.exit()
else:
    print("Pull successful")

add = subprocess.Popen(["git", "add", (Path / 'daily' / '_posts' / draft_to_publish)])
stdoutput, stderroutput = add.communicate()

commit_message = f'new post {date}'
commit = subprocess.Popen(["git", "commit", "-m", commit_message], stdout=PIPE, stderr=PIPE)
stdoutput, stderroutput = commit.communicate()

if b'fatal' in stdoutput:
    print("Fatal error in commit, aborting script")
    sys.exit()
else:
    print("Commit successful")

push = subprocess.Popen(["git", "push"], stdout=PIPE, stderr=PIPE)
stdoutput, stderroutput = push.communicate()

if b'fatal' in stdoutput:
    print("Fatal error in push, aborting script")
    sys.exit()
else:
    print("Push successful")

print("Waiting for Github Pages to build...")
time.sleep(30)

def LastPostDate():
    frontpage = urlopen('https://tedslocum.com').read()
    parsed_frontpage = BeautifulSoup(frontpage, 'html.parser')
    date_span = parsed_frontpage.body.find(
        'div', class_='recent-posts-mendokusai').find('span').text
    date_today = now.strftime("%d %b %Y")
    print(date_span)
    print(date_today)
    return date_today in date_span

print("Checking whether new post is on live site")
print("First try...")
if LastPostDate() == True:
    print("Post published!")
else:
    time.sleep(30)
    print("Second try...")
    if LastPostDate() == True:
        print("Post published!")
    else:
        time.sleep(30)
        print("Third try...")
        if LastPostDate() == True:
            print("Post published!")
        else:
            print("Something went wrong. If only you'd written an actual unit test with exceptions!")
