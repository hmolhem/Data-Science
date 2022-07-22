# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 23:38:08 2020

@author: Hossein Molhem
"""

# stand for of variables and methods in this project is following bellow:
# variables:
# gt is game table
# loc is list of countries
# rpc is result parameter for every county
# dic_cr is dictionary countries result
# dc is designated country
# ldci is list of designeted country index in games table
# ldc is all designeted country in games group
# lrdc list of all result games for designeted country games in group
# gf is total goal for for country
# lgf is list of goal for for country
# ga is total goal against for country
# lga is list of goal against for country
# win is number of win game
# draw is number of draw game
# lose is number of lose game
# gd is goal difference

# methods:
# ssr() is split string result 
# get_rrg() is method that is reading results games
# gsr is games result
# get_dci is getting designeted country index in games table
# get_dc() is getting all designeted country in games group
# get_rdc() is list of all result games for designeted country games in group
# get_cgf() is determine list of goal for and sum it
# get_cga() is determine list of goal against and sum it
# detwld() is determine win, draw and lose
# detgd() is determine goal difference
#%%
import myModule as m
gt, loc, rpc, dic_cr = m.init()  # initializing structure
gsr = m.rrgs(gt) # reading result games
gsr = list(map(m.ssr, gsr)) # split string result for all items in games result
gsr = list(map(m.s2i, gsr)) # convert string to int for all items games result
#%%
for dc in loc:
# dc = 'Morocco' # Iran is designeted country
    ldci = m.get_dci(dc, gt) # designated country index in list of games tabled
    ldc = m.get_dc(dc, gt) # getting list of all designeted country in games table
    lrdc = m.get_rdc(ldci,gsr) # list of all result designeted country games in group
    gf, lgf = m.get_cgf(dc, ldci, lrdc, ldc) # list of gf and sum it
    ga, lga = m.get_cga(dc, ldci, lrdc, ldc) # list of ga and sum it
    win, draw, lose = m.detwld(lgf,lga) # win, draw, lose for every team
    gd = m.detgd(gf,ga) # determine goal difference
    points = m.detscore(win,draw,lose) # determine score of team
    dic_cr[dc]['wins'] = win
    dic_cr[dc]['loses'] = lose
    dic_cr[dc]['draws'] = draw
    dic_cr[dc]['goal difference'] = gd
    dic_cr[dc]['points'] = points

final = sorted(dic_cr.keys())