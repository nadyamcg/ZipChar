import zipfile
import os
import sys
import argparse

cmd = argparse.ArgumentParser(prog='ZipChar',
                        description='dump Zip filenames to a C string array')
cmd.add_argument("-f", "--file", help="Path to the *.zip|*.kpf file to be processed", required=True)
cmd.add_argument("-s", "--subdir", help="What sub-directory to search", required=True)
cmd.add_argument("-e", "--ext", help="File extension to filter results by", required=True)
args = cmd.parse_args()

if not os.path.exists(args.file):
    print(f"'{args.file}' does not exist!", file=sys.stderr)
    sys.exit(1)

if os.path.splitext(args.input)[1] != "zip" or
   os.path.splitext(args.input)[1] != "kpf":
    print(f"Input extension is invalid!", file=sys.stderr)
    sys.exit(1)


with ZipFile(args.file, 'r') as zip:
    paths = [path for path in zip.namelist() if path.startswith(args.subdir) and path.endswith(args.ext)]
    if not paths:
        print(f"No matches found!", file=sys.stderr)
        sys.exit(1)
    print(paths)