# ircCloud
A python script to create word clouds out of ZNC logs

#Usage


    joe$ ./ircCloud.py --help 
    usage: ircCloud.py [-h] [--single SINGLE] [--multi MULTI] [--outfile OUTFILE]
                       [--bgimage BGIMAGE] [--limit LIMIT] [--width WIDTH]
                       [--height HEIGHT]
    
    DNS Word Cloud Image Generation
    
    optional arguments:
      -h, --help         show this help message and exit
      --single SINGLE    Single Source file
      --multi MULTI      keyword for multip[le Source files in the current
                         directory
      --outfile OUTFILE  Destination image file if not specified will be the name
                         of the input file.png
      --bgimage BGIMAGE  Optional image file to shape around
      --limit LIMIT      # of words to display, default 100
      --width WIDTH      Width of image, default 1600
      --height HEIGHT    Height of image, default 1200



