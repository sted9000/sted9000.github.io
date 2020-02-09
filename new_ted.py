import datetime
import re
import os
import sys
import subprocess

# which blog (daily or essays)
blog_strings = ['daily','essays']
blog_set = False
while blog_set != True:
    flavour = input('Which blog are you writing in today?')
    flavour = flavour.lower()
    if flavour in blog_strings: blog_set = True

print('done')

#
# # title
#
# # tags
#
# # queue placement
#
# # create and open file
#
# # Set date
# # Input - userInput (today, tomorrow, or add to queue)
# # Output - string (%Y-%m-%d)
# def setDate(_input_string):
#     if _input_string == 'today':
#         return datetime.date.today().strftime('%Y-%m-%d')
#     elif _input_sting == "tomorrow":
#         return (datetime.date.today() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
#     elif _input_string = 'queue':
#         return endQueueDate()
#     else:
#         print('Not an option. Please start over.')
#
# def endQueueDate():
#     # get dates in queue dir
#     # add one day to last date
#
#
#
#
#
#
# def get_all_substrings(input_string):
#     length = len(input_string)
#     return [input_string[0:i+1] for i in range(length)]
#
# blog_strings = get_all_substrings('daily') + get_all_substrings('essays')
#
# blog_set = False
# while blog_set != True:
#     flavour = input('Which blog are you writing in today?')
#     flavour = flavour.lower()
#     if flavour in blog_strings:
#         blog_set = True
#         if flavour in get_all_substrings('daily'):
#             flavour = 'daily'
#         elif flavour in get_all_substrings('essays'):
#             flavour = 'essays'
#
# name = input('What\'s the title of your blog post?')
# tags = input('What topics are you writing about today (separated by a comma)?')
#
# title_name = re.sub('[^a-zA-Z\s\d]', '', name)
# title_name = re.sub('\s', '-', title_name).lower()
#
# title = date + '-' + title_name + '.md'
#
# if flavour == 'daily':
#     path = os.getcwd() + '/daily/_posts/' + title
#     if not os.path.exists(path):
#         open(path, 'w')
# elif flavour == 'essays':
#     path = os.getcwd() + '/essays/_posts/' + title
#     if not os.path.exists(path):
#         open(path, 'w')
#
# if os.path.exists(path):
#     f = open(path, 'a')
#     f.write('---\n')
#     f.write('layout: ' + flavour + '\n')
#     f.write('author: Jonny Spicer\n')
#     f.write('title: ' + name + '\n')
#     f.write('tags: [ ' + tags + ' ]\n')
#     f.write('---\n')
#     if sys.platform == "win32":
#         os.startfile(path, 'open')
#     else:
#         opener = "open" if sys.platform == "darwin" else "xdg-open"
#         subprocess.call([opener, path])
