#!/usr/bin/env python
# -*-coding:Utf-8 -*
from os import listdir
from os.path import isdir, isfile, join, getsize
import argparse

def convert_sizeunit(bytes, unit):
    """
    This function converts a file size in Bytes to the unit
    specified in parameter: (B), kB, MB or GB
    :param bytes: Bytes value
    :type bytes: int
    :param unit: Unit type. Can be (B), kB, MB or GB
    :type unit: str
    :rtype: str
    """
    if unit == "(B)":
        factor = 1
    elif unit == "kB":
        factor = 1000.0
    elif unit == "MB":
        factor = 1000000.0
    elif unit == "GB":
        factor = 1000000000.0
    return "%s %s" % (bytes / factor, unit)

parser = argparse.ArgumentParser(description='Display the name and the size of the files of a given directory')
parser.add_argument('path', type=str, help='Path of the directory to be parsed')
parser.add_argument('--unit', type=str, action='store', default='(B)',
                    help='Size unit to display: (B), kB, MB or GB')

args = parser.parse_args()

path = args.path
unit = args.unit

allowed_units = ['(B)', 'kB', 'MB', 'GB']

try:
    if not unit in allowed_units:
        raise Exception('Unit shall be (B), kB, MB or GB. The value of unit was: %s' % unit)
    if not isdir(path):
        raise Exception('Path shall be a existing directory path. The path %s does not exist' % path)
except Exception as error:
    print error
    print "The script stopped. Please check the argument inputs"
else:
    for file in listdir(path):
        print file + "\t" + convert_sizeunit(getsize(join(path, file)), args.unit)
