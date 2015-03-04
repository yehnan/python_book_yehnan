

import sys

def main(infile, outfile):
    print(infile, outfile)

def proc_argv(argv):
    infile, outfile = None, None
    infile = argv[0]
    try:
        outfile = argv[1]
    except Exception:
        outfile = infile + '.out'
        print("Warning: output filename defaults to " + outfile)
    return infile, outfile

if __name__ == '__main__':
    try:
        inf, outf = proc_argv(sys.argv[1:])
    except Exception:
        print("At least specify input filename")
        sys.exit()
    main(inf, outf)
