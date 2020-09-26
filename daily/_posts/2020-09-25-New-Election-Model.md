---
date: 2020-09-25
layout: post
author: Ted
title: New Election Model
tags: prediction
---
```
'''
I want to know what are biden's and trump's chances of winning if the election were today.
So I look at the polls in all the states that could go either way.
The methodology is as follows:
1. Take the data from the latest good quality poll in each state
2. Find the margin of error given the poll structure.
3. Find each the candidates likelihood of winning by looking at the area under the curve
4. Propabalistically determine a winner for each state given the likelihood.
5. Add those states to the candidates electoral votes
6. Run the election 100,000 times

Note: I think there is an error in my methodology around the topic of of Margin of Error. In...
    polls with non-binanry options I believe I there is a different method to calculate the...
    margin of error than I used in my analysis. I will update tomorrow.

Results:
    Biden wins 99.5% if election were tomorrow and polls are 'accurate'.  
'''


import random
import math

''' You have 16 swing states '''
swing_states_dict = {
    # "state": [electoral votes, (biden%, trump%, sample size)]
    "nv": [6, (46.5, 41, 500)],
    "az": [11, (48.6, 44.1, 500)],
    "nm": [5, (48.6, 44.1, 500)],
    "co": [9, (51.9, 41.2, 500)],
    "mn": [10, (51.3, 42.1, 500)],
    "ia": [6, (45.9, 47.1, 500)],
    "wi": [10, (50.2, 43.7, 500)],
    "mi": [16, (49.9, 42.2, 500)],
    "oh": [18, (46.5, 48, 500)],
    "pa": [20, (49.7, 45.2, 500)],
    "nh": [4, (49.7, 43, 500)],
    "va": [13, (51.7, 40.7, 500)],
    "nc": [15, (47.7, 46.4, 500)],
    "ga": [16, (46.5, 47.1, 500)],
    "fl": [29, (48.1, 46.1, 500)],
    "tx": [38, (46.6, 47.4, 500)]
}

''' Z-Table of a normal distribution '''
z_table = {
    # "z_score": area under the curve
    "0.1": 0.03983,
    "0.2": 0.07926,
    "0.3": 0.11791,
    "0.4": 0.15542,
    "0.5": 0.19146,
    "0.6": 0.22575,
    "0.7": 0.25804,
    "0.8": 0.28814,
    "0.9": 0.31594,
    "1.0": 0.34134,
    "1.1": 0.36433,
    "1.2": 0.38493,
    "1.3": 0.40320,
    "1.4": 0.41924,
    "1.5": 0.43319,
    "1.6": 0.44520,
    "1.7": 0.45543,
    "1.8": 0.46407,
    "1.9": 0.47128,
    "2.0": 0.47725,
    "2.1": 0.48214,
    "2.2": 0.48610,
    "2.3": 0.48928,
    "2.4": 0.49180,
    "2.5": 0.49379,
    "2.6": 0.49534,
    "2.7": 0.49653,
    "2.8": 0.49744,
    "2.9": 0.49813,
    "3.0": 0.49865,
    "3.1": 0.49903,
    "3.2": 0.49931,
    "3.3": 0.49952,
    "3.4": 0.49966,
    "3.5": 0.49977,
    "3.6": 0.49984,
    "3.7": 0.49989,
    "3.8": 0.49993,
    "3.9": 0.49995,
    "4.0": 0.49997
}

''' What is the margin of error given poll? '''
def margin_of_error(_poll_data):
    z_score = 1.96 # for 95% confidence we use z-score of 1.96
    p_biden = _poll_data[0]
    p_trump = _poll_data[1]
    sample_size = _poll_data[2]
    # formula for MoE is z-score * sqroot(P*(1-P)/sample_size)
    # Note I am using biden% * trump% rather than biden% * (1 - biden%) because the poll numbers don't add up to 1
    MoE = z_score * math.sqrt((p_biden * p_trump) / sample_size)
    return MoE

''' Determine the z-score '''
def z_score(_poll_data, _MoE):
    p_biden = _poll_data[0]
    p_trump = _poll_data[1]
    mean = (p_biden + p_trump) / 2
    std = _MoE / 2
    # formula for z score is z_score = (poll_data - mean) / std
    z_score = (p_biden - mean) / std
    return z_score

''' Area under the curve given a z-score'''
def area_under_curve(_z_score):
    dict_key = str(round(abs(_z_score), 1))
    return z_table[dict_key]

''' Is biden winning in the polls '''
def is_biden_leading(_poll_data):
    p_biden = _poll_data[0]
    p_trump = _poll_data[1]
    if p_biden > p_trump:
        return True
    else:
        return False

''' Bidens propabalistic chances of winning the states '''
def biden_wins_state(_Biden_Leading, _AoC):
    if _Biden_Leading:
        return _AoC + 0.5
    else:
        return 1 - _AoC - 0.5

''' Determine a winner propabalistically '''
def biden_wins(_Chance_Biden_Wins_State):
    rand_number = random.random()
    if rand_number >= _Chance_Biden_Wins_State:
        return False
    else:
        return True

''' Run the elections many times '''
trials = 100000
biden_wins_counter = 0
trump_wins_counter = 0
for trial in range(trials):
    biden = 185 # Locked votes before swing states
    trump = 127 # Locked votes before swing states
    for state, data in swing_states_dict.items():
        MoE = margin_of_error(data[1])
        Z = z_score(data[1], MoE)
        AoC = area_under_curve(Z)
        Biden_Leading = is_biden_leading(data[1])
        Chance_Biden_Wins_State = biden_wins_state(Biden_Leading, AoC)
        Biden_Wins = biden_wins(Chance_Biden_Wins_State)
        if Biden_Wins:
            biden += data[0]
        else:
            trump += data[0]

    if biden > trump:
        biden_wins_counter += 1
    else:
        trump_wins_counter += 1

print(f'Trump wins: {trump_wins_counter/trials * 100}%; Biden wins: {biden_wins_counter/trials * 100}%')
```
