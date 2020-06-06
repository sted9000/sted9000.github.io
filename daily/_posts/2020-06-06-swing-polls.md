---
date: 2020-06-06
layout: post
author: Ted
title: Swing States Polls
tags: prediction
---
```python
import random

# So say you have 15 swing states
nv = 6
az = 11
nm = 5
co = 9
mn = 10
ia = 6
wi = 10
mi = 16
oh = 18
pa = 20
nh = 4
va = 13
nc = 15
ga = 16
fl = 29
swing_states = [nv, az, nm, co, mn, ia, wi, mi, oh, pa, nh, va, nc, ga, fl]

# Latest polling data (biden, trump)
swing_polls = [(49,45), (46,42), (52,40), (53, 40), (49, 44), (46, 48), (49, 40),
(50, 44), (45, 43), (49, 43), (44, 46), (51, 39), (49, 45), (48, 47), (47, 43)]

trials = 10000
biden_wins_counter = 0
trump_wins_counter = 0

for trial in range(trials):
    biden = 185
    trump = 165
    for i, votes in enumerate(swing_states):
        trump_chance = swing_polls[i][1] / (swing_polls[i][0] + swing_polls[i][1])
        random_election = random.random()
        if random_election > trump_chance:
            biden += votes
        else:
            trump += votes

    if biden > trump: biden_wins_counter += 1
    else: trump_wins_counter += 1

print(f'Trump wins: {trump_wins_counter}; Biden wins: {biden_wins_counter}')
```
