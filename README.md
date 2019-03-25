# ircMiner
A python script to mine data from ZNC logs of IRC. For now it creates bar graphs and word clouds. 

Usage:  

    daneel:logs joe$ ./ircMiner.py --help 
    usage: ircMiner.py [-h] [--single SINGLE] [--multi MULTI] [--outfile OUTFILE]
                       [--bgimage BGIMAGE] [--limit LIMIT] [--width WIDTH]
                       [--height HEIGHT] [--graph] [--cloud] [--title TITLE]
                       [--exclude EXCLUDE]
    
    ZNC Log Miner Image Generation
    
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
      --graph            Create a graph
      --cloud            Create a word cloud
      --title TITLE      Title of Graph
      --exclude EXCLUDE  List of words to exclude, enclose in quotes


To look at one log and create a single wordcloud:

     daneel:logs joe$ ./ircMiner.py --cloud --single example.log 
     Source file: example.log
     Output file  : examople.log.png
     Result Limit : 100
     IMG Width    : 1600
     IMG Height   : 1200


To create a word cloud from all ZNC logs with the word "example" in the name use the multi switch. 

    daneel:logs joe$ ./ircMiner.py --multi example --cloud 
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

To create a bar graph from all ZNC logs with the word "example" in the name use --graph with --multi. `

    daneel:logs joe$ ircCloud.py --multi example  --graph  --limit 50 --title "Example Most Common Words" 
    Processing files matching pattern example*.log
    Result Limit : 50
    Processing File: joe_#example_20190208.log
    Processing File: joe_#example_20190220.log
    Processing File: joe_#example_20190221.log
    Processing File: joe_#example_20190209.log
    Processing File: joe_#example_20190223.log
    Processing File: joe_#example_20190222.log
    Processing File: joe_#example_20190226.log
    Processing File: joe_#example_20190227.log
    Processing File: joe_#example_20190225.log
    Processing File: joe_#example_20190219.log
    Processing File: joe_#example_20190218.log
    Processing File: joe_#example_20190224.log

