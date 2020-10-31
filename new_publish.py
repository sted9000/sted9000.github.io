"""
The objectives of this script:
- Take a draft and add the date, title, author, and tags
- Move the draft to post directory
- Push the post to github
"""

from pathlib import Path
from datetime import datetime
from os import remove
from git import Repo

Path = Path('.')


def display_drafts():
    """
    Displays draft and asks user to select one.
    :return: The path object of the user selected draft
    """
    drafts = [x for x in (Path / '_drafts').iterdir()]
    for i, draft in enumerate(drafts):
        print(f'{i} - {draft.name[:-3]}')

    user_choice = input("What draft do you want to publish?: ")

    return drafts[int(user_choice)]


def display_tags():
    """
    Lists tags to choose from and asks user to pick one.
    Tags come from filenames in tag directory.
    :return:  List of tags
    """
    tags = [x for x in (Path / 'tag').iterdir()]
    for i, tag in enumerate(tags):
        print(f'{i} - {tag.name[:-3]}')

    user_choice = input("What tag do you want to use?: ")

    return tags[int(user_choice)].name[:-3]


def write_markdown_file():
    """
    Creates a file in _posts directory, formats the header, and writes the draft
    :return: No return
    """
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


"""
Below we will execute the functions to run the script
"""

# User picking blog to publish today
draft_to_publish = display_drafts()

# Header Data
post_layout = 'post'
post_date = datetime.now().strftime('%Y-%m-%d')
post_author = 'Ted'
post_tag = display_tags()
ff_length = 3 if '.md' in draft_to_publish.name else 4  # accounts for .md and .txt
post_title = post_tag.capitalize() + ' - ' + draft_to_publish.name[:-ff_length].replace('-', ' ')

# create the post
write_markdown_file()

# remove the draft
remove(draft_to_publish)

# add, commit, and push the post
repo = Repo(Path)
repo.index.add([str(Path / 'daily' / '_posts' / f'{post_date}-{draft_to_publish.name}')])
repo.index.commit(f'new post {post_date}')
origin = repo.remote('origin')
origin.push()
