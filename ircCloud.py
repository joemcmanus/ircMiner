#!/usr/bin/env python3
# File    : ircCloud.py 
# Purpose : A program to create word clouds out of IRC logs from ZNC
# Author  : Joe McManus josephmc@alumni.cmu.edu
# Version : 0.1  03/21/2019 Joe McManus
# Copyright (C) 2018 Joe McManus
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

from wordcloud import WordCloud, STOPWORDS
from PIL import Image
from collections import defaultdict,Counter
import os
import argparse
import matplotlib 
matplotlib.use('Agg') 
import sys
import string


parser = argparse.ArgumentParser(description='DNS  Word Cloud Image Generation')
parser.add_argument('--single', help="Single Source file", type=str, action="store")
parser.add_argument('--multi', help="keyword for multip[le Source files in the current directory", type=str)
parser.add_argument('--outfile', help="Destination image file if not specified will be the name of the input file.png", type=str)
parser.add_argument('--bgimage', help="Optional image file to shape around", type=str)
parser.add_argument('--limit', help="# of words to display, default 100", type=int, default=100)
parser.add_argument('--width', help="Width of image, default 1600", type=int, default=1600)
parser.add_argument('--height', help="Height of image, default 1200", type=int, default=1200)
args=parser.parse_args()


if args.single == None and args.multi == None: 
    print("ERROR:  Must specify a single or keywork for multiple files.")
    quit()

if args.outfile:
    outfile=args.outfile
else:
    if args.single:
        outfile=args.single + ".png"
    else:
        outfile=args.multi + ".png"

if args.single:
    if os.path.exists(args.single):
        print("Source file: " + args.single)
    else:
        print("ERROR: Source file does not exist, exitting.") 
        quit()

if args.multi:
    print("Processing files matching pattern " + args.multi + " *.log")

print("Output file  : {}"  .format(outfile))
print("Result Limit : {}"  .format(args.limit))
print("IMG Width    : {}"  .format(args.width))
print("IMG Height   : {}"  .format(args.height))
if args.bgimage:
    print("BG Image     : {}" .format(args.bgimage))

def parseFile(filename, text):
    fh=open(filename, "r")
    for line in fh:
        if ">" in line:
            words=line.split(">")[1].rstrip("\n")
            for word in words.split():
                if word not in "I bye it its of for this that the and to hey so there in be if you":
                    stripper= str.maketrans('', '', string.punctuation)
                    stripped=word.translate(stripper)
                    if len(stripped) > 0:
                        text.append(stripped)
    return(text)

#empty list
text=[]
if args.single:
    text=parseFile(args.single, text)
if args.multi:
    for filename in os.listdir("."):
        if filename.endswith(".log"):
            if args.multi in filename:
                print("Processing File: " + filename)
                text=parseFile(filename, text)

if len(text) == 0:
    print("Sorry after processing the file no matching lines found. Exiting. ") 
    quit()
    
cnt = Counter()
for item in text:
    cnt[item] += 1
#to change colormaps look at http://matplotlib.org/examples/color/colormaps_reference.html

if args.bgimage:
    import numpy as np
    mask = np.array(Image.open(args.bgimage))
    wc = WordCloud(regexp=r'.*\s', max_words=args.limit, mask=mask, colormap='autumn', max_font_size=200, height=args.height, width=args.width).generate_from_frequencies(cnt)
else: 
    wc = WordCloud(regexp=r'.*\s', max_words=args.limit, colormap='autumn', max_font_size=200, height=args.height, width=args.width).generate_from_frequencies(cnt)

wc.to_file(outfile)


