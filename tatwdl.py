#!/usr/bin/python

# Download podcasts from Trance around the World

# Usage:
# ./tatwdl.py <podcast_number> -- downloads 1 podcast
# ./tatwdl.py <start_num> <end_num> -- downloads all podcasts in range inclusive

import subprocess
import sys

def usage():
    print("Usage: ./temp.py <start_num> [<end_num>]")
    sys.exit(1)

def main():
    
    # Verify arguments
    argc = len(sys.argv)
    if argc < 2 or argc > 3:
        usage()
    start = int(sys.argv[1])
    if argc == 2:
        end = start
    else:
        end = int(sys.argv[2])
    if start > end:
        usage()
    
    # Loop starting from 'start'
    dlstring = "http://tatw-archives.anjunabeats.com/TATW{0}.mp3".format(start)
    while start <= end:
        # Subprocess call to wget
        subprocess.call(["wget", dlstring])
        start = start + 1
        dlstring = "http://tatw-archives.anjunabeats.com/TATW{0}.mp3".format(start)

if __name__ == "__main__":
    main()

