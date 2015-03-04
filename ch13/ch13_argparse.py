

import argparse

parser = argparse.ArgumentParser(description='Count lines in text files')

parser.add_argument(dest='path', metavar='path')

parser.add_argument('-e', dest='extensions', action='append',
                    metavar='extension', required=True,
                    help='filename extensions to process')
                    
parser.add_argument('-b', dest='blankline', action='store_true',
                    help='blank line')
                    
parser.add_argument('-r', dest='recur', action='store_true',
                    help='recursively into subdirectories')
                    
parser.add_argument('-o', dest='outfile', action='store',
                    help='output file')
                    
parser.add_argument('--speed', dest='speed', action='store',
                    choices={'slow','fast'}, default='fast',
                    help='processing speed')

args = parser.parse_args()

print('path', args.path)
print('extensions', args.extensions)
print('blankline', args.blankline)
print('recur', args.recur)
print('outfile', args.outfile)
print('speed', args.speed)

