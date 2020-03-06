from pathlib import Path
import datetime

Path = Path('.')
tags = ['Health', 'Mindfulness', 'Beauty', 'Freeroll']

### list drafts
drafts = [x for x in (Path / '_drafts').iterdir()]
for i, x in enumerate(drafts):
    print(str(i), x.parts[1])

### select draft
user_draft = input('What draft do you want to publish today? ')
draft_to_publish = drafts[int(user_draft)].parts[1]
print(draft_to_publish)

### header data
user_use_tags = input('Do you want to add tags to this post(y for yes, enter for no)? ')
# tags
if len(user_use_tags) > 0:
    for i, tag in enumerate(tags):
        print(str(i), tag)
    user_tags_string = input('Enter the number of the tag separated by commas: ')
    user_tags_list = user_tags_string.split(',')
    tags_for_post = [tags[int(x)] for x in user_tags_list]
# date
date = datetime.date.today().strftime('%Y-%m-%d')
# layout
layout = 'post'
# title
title_list = draft_to_publish[:-3].split('-')
title = ''
for word in title_list:
    title += word
    title += ' '

### write md file
f = open((Path / 'daily' / '_posts' / draft_to_publish), 'x')
f.write('---\n')
f.write('layout: ' + layout + '\n')
f.write('author: Ted Slocum\n')
f.write('title: ' + title[:-1] + '\n')
# f.write('tags: [ ' + tags + ' ]\n')
# f.write('---\n')
# format fileName
# move to daily posts
# git add
# git commit
# git push
# checks




# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import time
# import datetime
# import subprocess
# PIPE = subprocess.PIPE
# now = datetime.datetime.now()
# commitMessage = 'dp' + now.strftime('%y%m%d')
#
# pull = subprocess.Popen(["git", "pull"], stdout=PIPE, stderr=PIPE)
# stdoutput, stderroutput = pull.communicate()
#
# if b'fatal' in stdoutput:
#     print("Fatal error in pull, aborting script")
#     sys.exit()
# else:
#     print("Pull successful")
#
# add = subprocess.Popen(["git", "add", "-A"])
# stdoutput, stderroutput = add.communicate()
#
# commit = subprocess.Popen(["git", "commit", "-m", commitMessage], shell=True, stdout=PIPE, stderr=PIPE)
# stdoutput, stderroutput = commit.communicate()
#
# if b'fatal' in stdoutput:
#     print("Fatal error in commit, aborting script")
#     sys.exit()
# else:
#     print("Commit successful")
#
# push = subprocess.Popen(["git", "push"], stdout=PIPE, stderr=PIPE)
# stdoutput, stderroutput = push.communicate()
#
# if b'fatal' in stdoutput:
#     print("Fatal error in push, aborting script")
#     sys.exit()
# else:
#     print("Push successful")
#
# print("Waiting for Github Pages to build...")
#
# time.sleep(30)
#
# def LastPostDate():
#     frontpage = urlopen('https://sted9000.github.io').read()
#     parsed_frontpage = BeautifulSoup(frontpage, 'html.parser')
#     date_span = parsed_frontpage.body.find(
#         'div', class_='recent-posts-mendokusai').find('span').text
#     date_today = now.strftime("%d %b %Y")
#     return date_today in date_span
#
# print("Checking whether new post is on live site")
# print("First try...")
# if LastPostDate() == True:
#     print("Post published!")
# else:
#     time.sleep(30)
#     print("Second try...")
#     if LastPostDate() == True:
#         print("Post published!")
#     else:
#         time.sleep(30)
#         print("Third try...")
#         if LastPostDate() == True:
#             print("Post published!")
#         else:
#             print("Something went wrong. If only you'd written an actual unit test with exceptions!")
