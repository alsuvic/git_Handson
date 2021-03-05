#!/usr/bin/env python

# import libraries
import sys, re
from argparse import ArgumentParser

# read arguments
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# get arguments
args = parser.parse_args()

# change to uppercase
args.seq = args.seq.upper()                 # Note we just added this line
# indicate the correct NA based on nucleotide T or U
if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq):
        print ('The sequence is DNA')
    elif re.search('U', args.seq):
        print ('The sequence is RNA')
    else:
        print ('The sequence can be DNA or RNA')
else:
    print ('The sequence is not DNA nor RNA')

# search motig
if args.motif:
  # change to uppercase
  args.motif = args.motif.upper()
  print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
  if re.match(args.motif, args.seq):
    print("MOTIF FOUND")
  else:
    print("MOTIF NOT FOUND")
