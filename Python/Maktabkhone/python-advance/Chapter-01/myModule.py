# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 23:38:08 2020

@author: Hossein Molhem
"""
def init():
    # games table
    gt = [ ['Iran','Spain'], ['Iran', 'Portugal'], ['Iran', 'Morocco'],
           ['Spain','Portugal'], ['Spain','Morocco'], ['Portugal','Morocco'] ]
    
    # result parameter for every county
    rpc = {}
    
    # list of countries
    loc = ['Iran', 'Spain', 'Portugal', 'Morocco']
    
    # dictionary countries result
    dic_cr = {'Iran':{}, 'Spain':{}, 'Portugal':{}, 'Morocco':{}}
    
    return gt, loc, rpc, dic_cr

# python code for reading results games
def rrgs(gt):
    # input:
    # gt is games table
    # output:
    # return list of string include of result games of table
    return [input() for i in range(len(gt))]

# Python code to split string result of a game to list string result 
def ssr(str):
    # input:
    # str is every items of list of result games
    # output:
    # return list of string that split it base on dash or - 
    return str.split("-")

# python code for convert list string to int
def s2i(x):
    # input:
    # x is list of strings
    # output
    # return list of ints same list strings
    return [int(i) for i in x]

# python code for convert list to tuple    
def l2t(x):
    # input:
    # x is list int of result games
    # output:
    # return list tuple of result games
    return tuple(x)

# python code for getting designeted country index
def get_dci(dc, gt):
    # input:
    # dc is Designeted Country that we want getting it's games
    # gt is games table
    # output:
    # return list of all designeted country index in games group
    return [k for k,v in enumerate(gt) if dc in v]

# python code for getting list of designeted country
def get_dc(dc, gt):
    # input:
    # dc is Designeted Country that we want getting it's games
    # gt is games table
    # output:
    # return list of all designeted country in games group
    return [v for k,v in enumerate(gt) if dc in v]

# python code for getting list of all results for designeted country
def get_rdc(li, lr):
    # input:
    # li is list of all designeted country index in games group
    # r is list of all result designeted country in games group
    # output:
    # list of all result games for designeted country games in group
    return [ lr[i] for i in li]

# python code for getting list of peculiarities designeted country
def get_peculiarities(gt,dc):
    # input:
    # gt is games table
    # dc is Designeted Country that we want getting it's games
    # output:
    # return list of index of position in inner and outer designeted country
    return [[i, c.index(dc)] for i, c in enumerate(gt) if dc in c] 


def get_cga(dc, ldci, lcr, ldc):
    # input:
    # dc is Designeted Country in group we consider stand for c
    # ldci (country index) is list of outer index in index of designeted country games in group
    # lcr (country result) is list of result of designeted country games in group
    # ldc is list of designeted country
    # ouput:
    # list of ga (goal against) for country and sum that
    ga = [r for i in range(len(ldci)) for li, r in zip(ldc[i], lcr[i]) if li != dc]
    return sum(ga), ga
    
def get_cgf(dc, ldci, lcr, ldc):
    # input:
    # dc is Designeted Country in group we consider stand for c
    # ldci (country index) is list of outer index in index of designeted country games in group
    # lcr (country result) is list of result of designeted country games in group
    # ldc is list of designeted country
    # ouput:
    # list of gf (goal for) for country and sum that
    gf = [r for i in range(len(ldci)) for li, r in zip(ldc[i], lcr[i]) if li == dc]
    return sum(gf), gf

# python code to determine win, draw and lose
def detwld(lgf, lga):
    win, draw, lose = 0, 0, 0
    for i,j in zip(lgf,lga):
        if i>j:
            win+=1
        elif i==j:
            draw+=1
        else:
            lose+=1
    return win, draw, lose

# python code to determine goal difference
def detgd(gf,ga):
    # input:
    # gf is goal for
    # ga is goal against
    # output:
    # return goal difference
    return gf-ga

# python code to determine score of team
def detscore(win,draw,lose):
    # input:
    # number of win
    # number of draw
    # number of lose
    # output:
    # return score of team
    return win*3 + draw*1
    