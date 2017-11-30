#!/usr/bin/env python
# ADF2MP3 - converts adf files to mp3 and vice versa.  
#           This will allow you to extract radio stations from Vice City/GTA3

import sys
import os
import getopt
import struct

debug = 0


class ADF2MP3:
    def __init__(self):
        """initialise with some details which set will use
        """
        self.adf_modifier = 34
    
    def usage(self):
        print "\nADF2MP3 Converter"
        print "-----------------\n"
        print " -h | --help             Show this help"
        print " -d | --decode <file>    Convert adf file to mp3"
        print " -e | --encode <file>    Convert mp3 to adf"

    def convert_adf(self, filename):
        """Convert adf file to mp3"""
        new_filename = filename.split(".adf")[0] + ".mp3"
        self.convert_file(filename, new_filename)

    def convert_mp3(self, filename):
        """Convert mp3 file to adf"""
        new_filename = filename.split(".mp3")[0] + ".adf"
        self.convert_file(filename, new_filename)

    def convert_file(self, in_file, out_file):
        """save values from file"""
        if os.path.isfile(in_file):
            dest_file = open(out_file, 'wb+')
            with open(in_file, 'rb+') as sourcefile:
                data = sourcefile.read(1)
                while data:
                    moddata = ord(data) ^ self.adf_modifier
                    dest_file.write(struct.pack("=B", moddata))
                    data = sourcefile.read(1)
            sourcefile.close()
        else:
            print "ERROR: Cannot open file!"
            sys.exit(1)


# Main
adf_file = ADF2MP3()
opts, args = getopt.getopt(sys.argv[1:], "hde", ["help", "decode", "encode"])
if debug:
    print "Options:", opts
    print "Args:", args

for o, a in opts:
    if debug:
        print "O:", o
    if o in ("-h", "--help"):
        adf_file.usage()
        sys.exit(0)
    elif o in ("-d", "--decode"):
        if len(args) > 0:
            # list
            adf_file.convert_adf(args[0])
            sys.exit()
    elif o in ("-e", "--encode"):
        if len(args) > 0:
            # edit
            adf_file.convert_mp3(args[0])
            sys.exit(0)
    else:
        # assume garbage so exit
        print "ERROR: Unknown, please read the help page"
adf_file.usage()
