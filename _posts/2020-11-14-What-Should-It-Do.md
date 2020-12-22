---
title: Professional - What Should It Do?
date: 2020-11-14 00:00:00 Z
categories:
- daily
tags:
- professional
layout: post
author: Ted
---

> But the hard work in software is figuring out what it should do, not how to make it work. - DHH

This idea has been popping up a lot lately.

For example, in a project I have been working on, I initially had 1000 lines of tedious and fragile conditionals statements coloring the grid. I was focused on _making it work_. In a re-write, I realized that the front-end _should only do_ the simple task of applying CSS classes returned from the database. 1000 lines became 20. 

In the same project, I wanted a new feature and _made it work_ without much problem -- 4 hours tops, only to realize that I had not even considered what the feature _should do_. Luckily in this case it was simple enough that it worked out, but one shouldn't rely on luck. 

All this is to say I should start replacing _how do I make this work_ with _what should this do_ when starting or stuck on a problem. 
