#!/usr/bin/env python

import glob

def main():
    with open("generated.txt", 'w') as f:
        for fname in glob.glob("???.*.txt"):
            f.write("include::%s[]\n\n" % fname)

if __name__ == "__main__":
    main()

