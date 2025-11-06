import zipfile
import os
import sys
import argparse

cmd = argparse.ArgumentParser(prog='ZipChar',
                        description='dump Zip filenames to a C string array')
cmd.add_argument("-f", "--file", help="Path to the *.zip file to be processed", required=True)
cmd.add_argument("-s", "--subdir", help="What sub-directory to search", required=True)
cmd.add_argument("-e", "--ext", help="File extension to filter results by", required=True)
args = cmd.parse_args()

