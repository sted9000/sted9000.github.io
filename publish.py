### Imports
from pathlib import Path
import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import subprocess
from os import remove
import glob
import os
# from badge import badges_dict

### Update config file with badge data
# os.system("python3 badge.py")

### Variables
PIPE = subprocess.PIPE
now = datetime.datetime.now()
Path = Path('.')
author = 'Ted'
post_dir = 'daily/_posts/'

### User input for blog to publish

# Select draft
drafts = [x for x in (Path / '_drafts').iterdir()]
print('Drafts: ')
for i, x in enumerate(drafts):
    print(str(i), ' - ', x.parts[1])
user_draft = input('Enter Draft #: ')
draft_to_publish = drafts[int(user_draft)].parts[1]
print()

# Show post option
if input('Show the post(y)?: ') == 'y':
    d = open((Path / '_drafts' / draft_to_publish), 'r')
    for line in d: print(line)
    d.close()

# Tags
filenames = glob.glob(post_dir + '*md')
total_tags = []
for filename in filenames:
    f = open(filename, 'r', encoding='utf8')
    crawl = False
    for line in f:
        if crawl:
            current_tags = line.strip().split()
            if current_tags[0] == 'tags:':
                total_tags.extend(current_tags[1:])
                crawl = False
                break
        if line.strip() == '---':
            if not crawl:
                crawl = True
            else:
                crawl = False
                break
    f.close()
print(total_tags)
tags_for_post = input('Enter the tags: ').split()


# Post time
date = now.strftime('%Y-%m-%d')

# Post layout
layout = 'post'

# Post title
title_list = draft_to_publish[:-3].split('-')
title = ''
for word in title_list:
    title += word
    title += ' '
print()
user_title_input = input(f'Correct Title: {title}(y)? Or enter new title: ')
if user_title_input == 'y':
    new_title = title.strip()
    print(f'The title in the script is: {new_title}')
else:
    new_title = user_title_input.strip()


### Write markdown file

# Header
f = open((Path / 'daily' / '_posts' / f'{date}-{draft_to_publish}'), 'x')
f.write('---\n')
f.write(f'date: {date}\n')
f.write(f'layout: {layout}\n')
f.write(f'author: {author}\n')
f.write(f'title: {new_title}\n')
if tags_for_post != None:
    f.write('tags: ')
    for i, tag in enumerate(tags_for_post):
        if i+1 != len(tags_for_post): f.write(tag + ' ')
        else: f.write(tag + '\n')
f.write('---\n')

# Content
d = open((Path / '_drafts' / draft_to_publish), 'r')
for line in d: f.write(line)
f.close()


### Publish to github

# pull
pull = subprocess.Popen(["git", "pull"], stdout=PIPE, stderr=PIPE)
stdoutput, stderroutput = pull.communicate()
if b'fatal' in stdoutput:
    print("Fatal error in pull, aborting script")
    sys.exit()
else:
    print("Pull successful")

# add
add = subprocess.Popen(["git", "add", (Path / 'daily' / '_posts' / f'{date}-{draft_to_publish}') ])
stdoutput, stderroutput = add.communicate()
add = subprocess.Popen(["git", "add", (Path / 'index.html')])
stdoutput, stderroutput = add.communicate()

# commit
commit = subprocess.Popen(["git", "commit", "-m", f'new post {date}'], stdout=PIPE, stderr=PIPE)
stdoutput, stderroutput = commit.communicate()
if b'fatal' in stdoutput:
    print("Fatal error in commit, aborting script")
    sys.exit()
else:
    print("Commit successful")

# push
push = subprocess.Popen(["git", "push"], stdout=PIPE, stderr=PIPE)
stdoutput, stderroutput = push.communicate()
if b'fatal' in stdoutput:
    print("Fatal error in push, aborting script")
    sys.exit()
else:
    print("Push successful")

### check to see if site built
print("Waiting for Github Pages to build...")
time.sleep(30)

#  Fetch index of blog and check title of post
def LastPostTitle():
    frontpage = urlopen('https://tedslocum.com').read()
    parsed_frontpage = BeautifulSoup(frontpage, 'html.parser')
    a_title = parsed_frontpage.body.find(
        'div', class_='recent-posts-mendokusai').find('a').text
    print(f'The title in the from the scraper is: {a_title}')
    print(f'The titles are a match? {new_title == a_title}')
    return new_title == a_title

def removeDraft():
    remove((Path / '_drafts' / draft_to_publish))

def replaceIndex():
    with open('index.html.bak', 'r') as file :
      filedata = file.read()

    # Write the file out again
    with open('index.html', 'w') as file:
      file.write(filedata)


print("Checking whether new post is on live site")
print("First try...")
if LastPostTitle() == True:
    print("Post published!")
    removeDraft()
else:
    time.sleep(30)
    print("Second try...")
    if LastPostTitle() == True:
        print("Post published!")
        removeDraft()
    else:
        time.sleep(30)
        print("Third try...")
        if LastPostTitle() == True:
            print("Post published!")
            removeDraft()
        else:
            print("Something went wrong. If only you'd written an actual unit test with exceptions!")
