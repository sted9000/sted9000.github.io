---
date: 2020-06-05
layout: post
author: Ted
title: Random Election
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

trials = 10000
biden_wins_counter = 0
trump_wins_counter = 0

for trial in range(trials):
    biden = 185
    trump = 165
    for i in swing_states:
        if random.choice([0, 1]) == 0:
            biden += i
        else:
            trump += i
    if biden > trump: biden_wins_counter += 1
    else: trump_wins_counter += 1

print(f'Trump wins: {trump_wins_counter}; Biden wins: {biden_wins_counter}')

```
