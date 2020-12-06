---
date: 2020-12-05
layout: post
author: Ted
title: Thank-you - Python Love
tags: thank-you
---
```
from notion.client import NotionClient
client = NotionClient(token_v2="<cookie>")
page = client.get_block("<url>")
print(page.collection.get_rows())
```

This is why I love python. The community.

I have been waiting for Notion.so to release its API. Silly me. 

In four lines of simple code from a newly published python library and you have your notion database returned to your command line.

How fun. 
