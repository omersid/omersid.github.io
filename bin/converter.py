import re
import argparse
from pathlib import Path

TITLE = """---
title:  "XXXXXXX"
date:   2020-05-17 17:00:16 -0400
categories: thoughts
layout: post
permalink: /posts/XXXXXXX
--- 
"""

# STUFF TO REMOVE
REMOVE = [ 
    "body {\n\tline-height: 1.5;\n\twhite-space: pre-wrap;\n}",
    "text-decoration: underline;",
    '</html>',
    '</head>'
]



def main():
    parser = argparse.ArgumentParser(description='convert notion --> jekyll whatever')
    parser.add_argument("--input_file", required=True, type=str)
    parser.add_argument("--date", required=True, type=str)
    parser.add_argument("--title", required=True, type=str)
    args = parser.parse_args()

    with open(args.input_file) as infile:
        flist = infile.readlines()
        flist[0] = "<style>"
        fstring = "".join(flist)
        fstring = TITLE + fstring
        for rmv in REMOVE:
            fstring = re.sub(rmv,'', fstring)
        fstring = re.sub('2020-05-17', args.date, fstring)
        fstring = re.sub('XXXXXXX', args.title, fstring)
        newfile = args.date + '-' + args.title + '.md'
        with open(newfile, 'w') as ofile:
            ofile.write(fstring)



if __name__ == "__main__":
    main()