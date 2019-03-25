#!/usr/bin/env python3
# File    : ircMiner.py 
# Purpose : A program mine some data from ZNC/IRC logs
# Author  : Joe McManus josephmc@alumni.cmu.edu
# Version : 0.2  03/24/2019 Joe McManus
# Copyright (C) 2019 Joe McManus
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with 

from collections import defaultdict,Counter
import os
import argparse
import sys
import string


parser = argparse.ArgumentParser(description='ZNC Log Miner Image  Generation')
parser.add_argument('--single', help="Single Source file", type=str, action="store")
parser.add_argument('--multi', help="keyword for multip[le Source files in the current directory", type=str)
parser.add_argument('--outfile', help="Destination image file if not specified will be the name of the input file.png", type=str)
parser.add_argument('--bgimage', help="Optional image file to shape around", type=str)
parser.add_argument('--limit', help="# of words to display, default 100", type=int, default=100)
parser.add_argument('--width', help="Width of image, default 1600", type=int, default=1600)
parser.add_argument('--height', help="Height of image, default 1200", type=int, default=1200)
parser.add_argument('--graph', help="Create a graph", action="store_true")
parser.add_argument('--cloud', help="Create a word cloud", action="store_true")
parser.add_argument('--title', help="Title of Graph", action="store", default="IRC Cloud")
parser.add_argument('--exclude', help="List of words to exclude, enclose in quotes", type=str )
args=parser.parse_args()


if args.single == None and args.multi == None: 
    print("ERROR:  Must specify a single or keywork for multiple files.")
    quit()

if not args.cloud and not args.graph:
    print("ERROR:  Must specify a grapg or cloud, otherwise it is like a circle, pointless.")
    quit()

if args.single:
    if os.path.exists(args.single):
        print("Source file: " + args.single)
    else:
        print("ERROR: Source file does not exist, exitting.") 
        quit()

if args.multi:
    print("Processing files matching pattern " + args.multi + "*.log")

#ignore some common words 
excludeList="I Its Im bye it its of for this that the and to was its here hey so there in be you on have with are if " 
if args.exclude:
    excludeList=excludeList +  args.exclude
    print("Exclude additoinal word list: {}".format(args.exclude))

if args.graph:
    import plotly
    import plotly.graph_objs as go

if args.cloud:
    from wordcloud import WordCloud, STOPWORDS
    from PIL import Image

if args.cloud:
    if args.outfile:
        outfile=args.outfile
    else:
        if args.single:
            outfile=args.single + ".png"
        else:
            outfile=args.multi + ".png"
    print("Output file  : {}"  .format(outfile))
    print("IMG Width    : {}"  .format(args.width))
    print("IMG Height   : {}"  .format(args.height))
    if args.bgimage:
        print("BG Image     : {}" .format(args.bgimage))

print("Result Limit : {}"  .format(args.limit))

def parseFile(filename, text, excludeList):
    fh=open(filename, "r")
    for line in fh:
        if ">" in line:
            words=line.split(">")[1].rstrip("\n")
            for word in words.split():
                stripper= str.maketrans('', '', string.punctuation)
                stripped=word.translate(stripper)
                if len(stripped) > 0:
                    if stripped  not in excludeList: 
                        text.append(stripped)
    return(text)

def createCloud(text, width, height, bgimage):
    #to change colormaps look at http://matplotlib.org/examples/color/colormaps_reference.html
    if args.bgimage:
        import numpy as np
        mask = np.array(Image.open(args.bgimage))
        wc = WordCloud(regexp=r'.*\s', max_words=args.limit, mask=mask, colormap='autumn', max_font_size=200, height=args.height, width=args.width).generate_from_frequencies(cnt)
    else: 
        wc = WordCloud(regexp=r'.*\s', max_words=args.limit, colormap='autumn', max_font_size=200, height=args.height, width=args.width).generate_from_frequencies(cnt)

    wc.to_file(outfile)

def createGraph(xData, yData, title):
    plotly.offline.plot({

        "data":[ go.Bar( x=xData, y=yData) ],
        "layout": go.Layout(title=title)
    },filename=makeFilename(title))

def makeFilename(title):
    #first remove spaces 
    title=title.replace(" ","-")
    #next remove slashes 
    title=title.replace("/","")
    #return the title with .html on the end so we don't get alerts
    return title + ".html"

#empty list
text=[]
if args.single:
    text=parseFile(args.single, text, excludeList)
if args.multi:
    for filename in os.listdir("."):
        if filename.endswith(".log"):
            if args.multi in filename:
                print("Processing File: " + filename)
                text=parseFile(filename, text, excludeList)

if len(text) == 0:
    print("Sorry after processing the file no matching lines found. Exiting. ") 
    quit()
    
cnt = Counter()

if args.cloud:
    for word in text:
        cnt[word] += 1
    createCloud(text, args.width, args.height, args.bgimage)

if args.graph:
    xData=[]
    yData=[]
    for word in text:
        cnt[word] += 1
    i=0
    for word, count in cnt.most_common():
        yData.append(count)
        xData.append(word)

        if args.limit:
             if i >= args.limit:
                break

        i+=1 
    createGraph(xData, yData, args.title) 
