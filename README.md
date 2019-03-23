# ircCloud
A python script to create word clouds out of ZNC logs

Usage


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



To look and one log and create a single wordcloud:

     ./ircCloud.py --single example.log 
     Source file: example.log
     Output file  : examople.log.png
     Result Limit : 100
     IMG Width    : 1600
     IMG Height   : 1200


To create a word cloud from all ZNC logs with the word "example" in the name use the multi switch. 

    joe$ ./ircCloud.py --multi example
    Processing files matching pattern example *.log
    Output file  : example.png
    Result Limit : 100
    IMG Width    : 1600
    IMG Height   : 1200
    Processing File: joe__#example_20190314.log
    Processing File: joe__#example_20190301.log
    Processing File: joe__#example_20190315.log
    Processing File: joe__#example_20190303.log
    Processing File: joe__#example_20190304.log
    Processing File: joe__#example_20190310.log

To create a word cloud with specified height and width use --width and --height. 
